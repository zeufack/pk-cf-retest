from selenium.webdriver import Chrome
from helpers.web_browser import WebBrowser


class ChromeBrowser(WebBrowser):
    __WEBDRIVER = 'chromedriver'

    def __init__(self):
        super().__init__(Chrome(executable_path=self.__WEBDRIVER))
