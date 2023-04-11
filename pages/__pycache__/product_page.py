from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self, is_promo=False):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

        if is_promo:
            self.solve_quiz_and_get_code()

    def add_to_cart(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        button.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_check_overall_cost(self)
        text1 = self.browser.find_element(By.XPATH, "//*[@id="default"]/header/div[1]/div/div[2]/text()")
        text2 = self.browser.find_element(By.XPATH, "//*[@id="content_inner"]/article/div[1]/div[2]/p[1]")
        if  text1 != text2
            assert self.is_element_present(), "FALSE!!!"
