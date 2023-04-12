import pytest
from pages.product_page import ProductPage 

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"

class TestUserAddToCartFromProductPage:
#    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                           "?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#    def test_guest_can_add_product_to_basket(self, browser, link):
#        product_page = ProductPage(browser, link) # Страница продукта
#        product_page.open()                       # Открываем страницу
#        product_page.add_to_cart(True)            # Добавить в корзину
#        product_page.should_be_present_in_cart()  # Проверка нахождения товара в корзине
#        product_page.should_check_overall_cost()  # Проверка стоимости

    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
        page = ProductPage(browser, link)
        page.open()                                 # Открываем страницу товара 
        page.add_to_cart(True)                      # Добавляем товар в корзину 
        page.should_not_be_success_message()        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def test_guest_cant_see_success_message(browser): 
        page = ProductPage(browser, link)
        page.open()                                 # Открываем страницу товара 
        page.should_not_be_success_message()        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def test_message_disappeared_after_adding_product_to_basket(browser): 
        page = ProductPage(browser, link)
        page.open()                                 # Открываем страницу товара 
        page.add_to_cart(True)                      # Добавляем товар в корзину 
        page.should_disappear_success_message()     # Проверяем, что нет сообщения об успехе с помощью  is_disappeared
        
        
        
