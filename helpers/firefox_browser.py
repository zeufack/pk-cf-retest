from selenium.webdriver import Firefox
from helpers.web_browser import WebBrowser


class FirefoxBrowser(WebBrowser):
    __WEBDRIVER = 'geckodriver'

    def __init__(self):
        super().__init__(Firefox(executable_path=self.__WEBDRIVER))
