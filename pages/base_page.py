from selenium.common.exceptions import NoSuchElementException


class BasePage:

    ACCEPT_COOKIE_BTN = '//button[@id="onetrust-accept-btn-handler"]'
    PUB_BTN = '/html/body/div[9]/div/div[2]/div[3]/span'

    def __init__(self, browser, url):
        self.url = url
        self.browser = browser

    def load(self):
        self.browser.get(self.url)
        try:
            cookie_accept = self.find(self.ACCEPT_COOKIE_BTN)
            cookie_accept.click()
            # self.clos_pub()
        except NoSuchElementException:
            pass

    def clos_pub(self):
        try:
            pub_btn = self.find(self.PUB_BTN)
            pub_btn.click()
        except NoSuchElementException:
            pass

    def find(self, element):
        return self.browser.find_element_by_xpath(element)
