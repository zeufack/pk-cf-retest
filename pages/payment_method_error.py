from pages.base_page import BasePage
from bs4 import BeautifulSoup


class PaymentMethodError(BasePage):
    URL = "https://www.carrefour.fr/"
    payment_div = ""

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def navigate_to_payment_method(self):
        self.browser.wait(5)
        self.handle_advertising()
        account_btn = self.browser.find_by_xpath(self.ACCOUNT_BTN)
        account_btn.click()

        info_btn = self.browser.find_by_xpath(
            "//div[@id='data-nav']/div/div[2]/div/ul/li[5]/a/span")
        info_btn.click()

        info_link = self.browser.find_by_xpath(
            "//a[contains(text(),'Mes moyens de paiement')]")
        info_link.click()

    def test_payment_input(self):
        self.browser.wait(20)
        self.handle_advertising()
        soup = BeautifulSoup(
            self.browser.get_browser().page_source, features="html.parser")
        payment_div = soup.find_all(
            "div", {"id": "pl-pm-cards_6-cardNumberContainer"})[0]
        print(payment_div)

        return False if payment_div.find_all("input") is None else True
