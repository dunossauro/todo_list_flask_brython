import selenium.webdriver.support.expected_conditions as EC
from page_objects import MultiPageElement, PageElement, PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def be_blank(driver, css):
    """Espera elemento estar em branco."""
    WebDriverWait(driver, 20).until(
        lambda element: driver.find_element_by_css_selector(css).text == ''
    )


def wait_task(driver, css):
    """Aguarda as taks serem carregadas."""
    WebDriverWait(driver, 20).until(
        lambda element: driver.find_element_by_css_selector(css)
    )


class Task:
    def __init__(self, driver):
        self.driver = driver
        self.load()

    def load(self):
        header = self.driver.find_element_by_tag_name('header').text.split('#')
        self.id = header[1]
        self.name = header[0].strip()
        self.desc = self.driver.find_element_by_tag_name('div').text
        self.urgent = ''

    def do(self):
        self.driver.find_element_by_css_selector('.btn-ghost.do').click()

    def cancel(self):
        self.driver.find_element_by_css_selector('.btn-ghost.cancel').click()


class CreateTodo(PageObject):
    name = PageElement(name='name')
    description = PageElement(name='desc')
    urgent = PageElement(name='urgent')
    submit = PageElement(id_='submit')

    def create_todo(self, name, description, urgent):
        be_blank(self.w, 'input[name="name"]')
        be_blank(self.w, 'textarea[name="desc"]')
        self.name = name
        self.description = description
        if urgent:
            self.urgent.click()

        self.submit.click()


class TaskColumn(PageObject):
    def __init__(self, driver):
        self.tasks = MultiPageElement(css=self.selector)
        PageObject.__init__(self, driver)

    def get_tasks(self, wait=False):
        if not wait:
            wait_task(self.w, self.selector)
        return [Task(element) for element in self.tasks.find(self.w)]


class Todo(TaskColumn):
    selector = '.terminal-timeline.todo .terminal-card'


class Doing(TaskColumn):
    selector = '.terminal-timeline.doing .terminal-card'


class Done(TaskColumn):
    selector = '.terminal-timeline.done .terminal-card'


class Login(PageObject):
    email = PageElement(name='email')
    password = PageElement(name='senha')
    submit = PageElement(css='input[value="Login"]')
    error = PageElement(css='.terminal-alert-error')

    def wait_form(self, name='email'):
        WebDriverWait(self.w, 20).until(
            EC.element_to_be_clickable((By.NAME, name))
        )

    def wait_error_message(self):
        WebDriverWait(self.w, 20).until(
            lambda driver: 'terminal-alert-error' in driver.page_source
        )


class CreateUser(PageObject):
    name = PageElement(name='nome')
    email = PageElement(name='email')
    email_label = PageElement(css='.form-group:nth-child(2) > label')
    password = PageElement(name='senha')
    submit = PageElement(css='.btn')
    error = PageElement(css='.terminal-alert-error')

    def create_user(self, nome, email, senha) -> None:
        self.name = nome
        self.email = email
        self.password = senha
        self.submit.click()

    def wait_error_message(self):
        WebDriverWait(self.w, 20).until(
            lambda driver: 'terminal-alert-error' in driver.page_source
        )
