import pytest
from pages.product_page import ProductPage

link =  "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToCartFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize(link)
    def test_user_can_add_product_to_cart(self, browser, link: str):
        product_page = ProductPage(browser, link) # Страница продукта
        product_page.open()                       # Открываем страницу
        product_page.add_to_cart(True)            # Добавить в корзину
        product_page.should_be_present_in_cart()  # Проверка нахождения товара в корзине
        product_page.should_check_overall_cost()  # Проверка стоимости




