from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR,
                           "#messages>div:first-child .alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")    

class BasketPageLocators:
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    LBL_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6")
    LBL_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
