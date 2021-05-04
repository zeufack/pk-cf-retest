from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from pages.base_page import BasePage


class ConnectionError(BasePage):
    URL = 'https://www.carrefour.fr'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def connect(self):
        account_btn = self.browser.find_by_xpath(
            '//*[@id="data-account"]')
        account_btn.click()
        connect_btn = self.browser.find_by_xpath(
            '/html/body/header/div[2]/div[1]/div[1]/div[2]/div/a[1]')
        connect_btn.click()

    def get_connexion_error(self):
        error_box = self.browser.find_by_xpath('//*[@id="main-iframe"]')

        self.browser.use_frame(error_box)
        error_text = self.browser.find_by_xpath(
            '/html/body/div[1]/div[1]/div[1]/div/div[2]')

        return error_text.text
