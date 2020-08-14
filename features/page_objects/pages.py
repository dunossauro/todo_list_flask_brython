import selenium.webdriver.support.expected_conditions as EC
from page_objects import MultiPageElement, PageElement, PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class task:
    def __init__(self, driver):
        self.driver = driver
        self.load()

    def load(self):
        header = self.driver.find_element_by_tag_name('header').text.split('#')
        self.id = header[1]
        self.name = header[0].strip()
        self.desc = self.driver.find_element_by_tag_name('div').text


class CreateTodo(PageObject):
    name = PageElement(name='name')
    description = PageElement(name='desc')
    urgent = PageElement(name='urgent')
    submit = PageElement(id_='submit')


class Todo(PageObject):
    tasks = MultiPageElement(css='.terminal-timeline.todo .terminal-card')

    def get_tasks(self):
        return [task(element) for element in self.tasks]


class Login(PageObject):
    email = PageElement(name='email')
    password = PageElement(name='senha')
    submit = PageElement(css='input[value="Login"]')

    def wait_form(self, name='email'):
        WebDriverWait(self.w, 20).until(
            EC.element_to_be_clickable((By.NAME, name))
        )
