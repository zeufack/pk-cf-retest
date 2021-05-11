from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    ACCEPT_COOKIE_BTN = '//button[@id="onetrust-accept-btn-handler"]'
    PUB_BTN = '/html/body/div[9]/div/div[2]/div[3]/span'
    POPUP_XPATH = "//div[@id='by_r_5cad67066e424bdd9c18a49393802c5b']/div"
    CLOSE_ADVERTISING = '.by_close'
    CLOSE_ADVERTISING_XPATH = "//span[@onclick='by_Hide_og0001('5cad67066e424bdd9c18a49393802c5b');']"
    USEREMAIL = "ndorichnel@gmail.com"
    PASSWRD = "Nd0r|chnel"
    USEREMAIL_INPUT_ID = "idToken1"
    PASSWRD_INPUT_ID = "idToken2"
    NEXT_BTN_ID = 'next'
    CONNECT_BTN_ID = 'loginButton_0'
    ACCOUNT_BTN = '//*[@id="data-account"]'

    def __init__(self, browser, url='https://www.carrefour.fr/'):
        self.url = url
        self.browser = browser

    def load(self):
        self.browser.open(self.url)
        try:
            cookie_accept = self.browser.find_by_xpath(self.ACCEPT_COOKIE_BTN)
            cookie_accept.click()
        except (NoSuchElementException, TimeoutException):
            pass

    def connect(self):
        # self.handle_advertising()
        account_btn = self.browser.find_by_xpath(self.ACCOUNT_BTN)
        account_btn.click()
        connect_btn = self.browser.find_by_xpath(
            '/html/body/header/div[2]/div[1]/div[1]/div[2]/div/a[1]')
        connect_btn.click()

    def fill_connection_form(self):
        useremail_input = self.browser.find_by_id(
            self.USEREMAIL_INPUT_ID)
        useremail_input.send_keys(
            self.USEREMAIL)
        next_btn = self.browser.find_by_id(self.NEXT_BTN_ID)
        next_btn.click()
        passwrd_iput = self.browser.find_by_id(self.PASSWRD_INPUT_ID)
        ActionChains(self.browser.get_browser()).move_to_element(
            passwrd_iput).click(passwrd_iput).perform()
        passwrd_iput.send_keys(self.PASSWRD)

        connect_btn = self.browser.find_by_id(self.CONNECT_BTN_ID)
        connect_btn.click()

    def handle_advertising(self):
        try:
            popup = self.browser.find_by_xpath(self.POPUP_XPATH)
            close_advertising = self.browser.find_by_selector(
                self.CLOSE_ADVERTISING).click()
        except (NoSuchElementException, TimeoutException):
            pass
