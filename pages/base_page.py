from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    ACCEPT_COOKIE_BTN = '//button[@id="onetrust-accept-btn-handler"]'
    PUB_BTN = '/html/body/div[9]/div/div[2]/div[3]/span'
    POPUP_ID = 'by_r_31a0722a70a443548d74efe6ba34e122'
    CLOSE_ADVERTISING = 'by_close'

    def __init__(self, browser, url):
        self.url = url
        self.browser = browser

    def load(self):
        self.browser.get(self.url)
        try:
            cookie_accept = self.find(self.ACCEPT_COOKIE_BTN)
            cookie_accept.click()
        except NoSuchElementException:
            pass

    def handle_advertising(self, browser):
        try:
            popup = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, self.POPUP_ID)))
            close_advertising = popup.find_element_by_class_name(
                self.CLOSE_ADVERTISING).click()
        except (NoSuchElementException, TimeoutException):
            pass

    def find(self, element):
        return self.browser.find_element_by_xpath(element)
