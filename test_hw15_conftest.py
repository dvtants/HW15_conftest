import pytest
from selenium.webdriver.common.by import By

link = "https://rozetka.com.ua/ua/"


class TestPage1():  # тест суіти знаходяться в класах
    # викликаємо фікстуру в тесті, передавши її як параметр
    @pytest.mark.smoke
    def test_is_button_search_1(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@id='fat-menu']")
        print("Шукаємо шлях на кнопку 'Каталог'")

    @pytest.mark.smoke
    def test_is_button_search_2(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH,
                             "//button[@class='button button_color_green button_size_medium search-form__submit']")
        print("Шукаємо шлях на кнопку 'Знайти'")

    @pytest.mark.smoke
    def test_is_button_search_3(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class='header__button ng-tns-c814534352-1']")
        print("Шукаємо шлях на кнопку 'Меню'")

    @pytest.mark.regression
    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//rz-cart[@class='header-actions__component']")
        print("Шукаємо шлях до 'Кошика'")

    @pytest.mark.chrome_117
    @pytest.mark.regression
    def test_is_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//rz-cart[@class='header-actions__component']")
        print("Шукаємо шлях до 'Вхід з авторизацією'")

# В терміналі PyCharm:
# pytest -s -v test_hw15_conftest.py
# pytest -s -v -m "smoke" test_hw15_conftest.py - виконується один тест тільки смоук, а саме: @pytest.mark.smoke
# pytest -s -v -m "regression" test_hw15_conftest.py - виконується два тести де є рігрешн, а саме: @pytest.mark.regression
# pytest -s -v -m " not regression" test_hw15_conftest.py - виконується все окрім рігрешн.
# pytest -s -v -m "not smoke" test_hw15_conftest.py - виконується все окрім смоук.
# pytest -s -v -m "regression or smoke" test_hw15_conftest.py - все виконується.
# pytest -s -v -m "regression and smoke" test_hw15_conftest.py - нічого не виконується.
# pytest -s -v -m "regression and chrome_117" test_hw15_conftest.py - проходить тест де є і regression і chrome_117, а саме: @pytest.mark.chrome_117 і @pytest.mark.regression
# дивись файл pytest.ini - зникає warnings - попередження.
# дивись файл conftest.py - назва цього файла саме така і не повинна змінюватися.
# pytest -s -v test_hw15_conftest.py
# pytest -s -v --browser_mode='gui' test_hw15_conftest.py
