from selenium import webdriver
from helpers.web_browser import WebBrowser
from selenium.webdriver import Chrome


class ChromeProxyBrowser(WebBrowser):
    # 51.222.67.222	32768
    PORT = '178.32.129.31:3128'
    # PORT = '51.158.123.35:9999'
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PORT)
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    __WEBDRIVER = 'chromedriver'

    def __init__(self):
        super().__init__(
            Chrome(options=self.options, executable_path=self.__WEBDRIVER))
