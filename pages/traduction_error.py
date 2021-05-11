from pages.base_page import BasePage


class TraductionError(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def verify_test(self):
        text = self.browser.find_by_xpath()
        pass
