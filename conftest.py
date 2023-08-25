import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Объявление опции командной строки для выбора языка
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose the language for the browser")


# Создание фикстуры для браузера
@pytest.fixture(scope="function")
def browser(request):
    # Получение выбранного пользователями языка из опции командной строки
    user_language = request.config.getoption("language")

    # Настройка опций браузера для установки выбранного языка
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализация экземпляра браузера Chrome с настроенными опциями
    browser = webdriver.Chrome(options=options)

    # Возврат браузера как объекта фикстуры для использования в тестах
    yield browser

    # Завершение работы браузера после выполнения тестов
    browser.quit()

