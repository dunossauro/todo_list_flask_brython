from pytest import fixture
from selenium.webdriver import Firefox


@fixture
def browser():
    browser = Firefox()
    yield browser
    browser.quit()


def test_deve_registrar_uma_task(browser):
    browser.get('http://localhost:5000/todo')

    browser.find_element_by_name('name').send_keys('dormir')
    browser.find_element_by_name('desc').send_keys('pq é bom')
    browser.find_element_by_id('submit').click()

    ...
