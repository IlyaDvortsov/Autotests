from selenium.webdriver.common.by import By
import time


# Тест для проверки наличия кнопки "Добавить в корзину" на странице товара
def test_check_add_to_cart_button(browser):
    # Задаем ссылку на страницу с товаром
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Открываем страницу товара в браузере
    browser.get(link)
    time.sleep(30)

    # Ищем кнопку "Добавить в корзину" на странице по её CSS-селектору
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверяем, что кнопка найдена на странице
    assert add_to_cart_button, "Add to cart button not found"




