from pages.main_page import MainPage
import pytest

#@pytest.mark.login_guest                                                                             #Группировка тестов запускать через -m login_guest
#class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # иници    ализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем с  траницу
        page.go_to_login_page()          # выполняем метод с    траницы — переходим на страницу 

    def test_guest_should_see_login_link(self, browser):          # &&&
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()    

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):                                              # Проверить!!!
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)  
        page.open()                                                # Гость открывает страницу товара
        page.go_to_basket()                                        # Переходит в корзину по кнопке в шапке сайта
        basket_page = BasketPage(browser, browser.current_url)  # Ожидаем, что в корзине нет тов    аров
        basket_page.should_be_empty_basket()                    # Ожидаем, что есть текст о том, чт о корзина пуста
