from page_objects import MultiPageElement, PageElement, PageObject


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


class CreateUser(PageObject):
    name = PageElement(name='nome')
    email = PageElement(name='email')
    email_label = PageElement(css='.form-group:nth-child(2) > label')
    password = PageElement(name='senha')
    submit = PageElement(css='.btn')

    def create_user(self, data_json: dict) -> None:
        self.name = data_json.get('nome')
        self.email = data_json.get('email')
        self.password = data_json.get('senha')
        self.submit.click()
