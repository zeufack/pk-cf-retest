from pages.base_page import BasePage


class TranslationError(BasePage):

    ERROR_TEXT_SELECTOR = ".push-store-delivery-block__box li:nth-child(1)"

    def __init__(self, browser):
        super().__init__(browser)

    def scrooll_down(self):
        self.browser.execute_js("window.scrollTo(0,2989)")
        self.browser.wait(10)

    def verify_test(self):
        text = self.browser.find_by_selector(self.ERROR_TEXT_SELECTOR).text
        print(text)
        return text
