from pages.base_page import BasePage


class PromotionError(BasePage):

    URL = 'https://www.carrefour.fr/r'
    SEARCH = '//*[@id="search-bar-input"]'
    SEARCH_BTN = '/html/body/header/div[2]/div[1]/div[3]/form/div[1]/input[2]'
    RESULT_FOUND = '/html/body/main/div[3]/section/div/div[3]/ul/li'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def serch_product(self, product):
        search_input = self.browser.find_by_xpath(self.SEARCH)
        search_input.clear()
        search_input.send_keys(product)
        search_btn = self.browser.find_by_xpath(self.SEARCH_BTN)
        search_btn.click()
        found = False
        try:
            results = self.browser.find_all_by_xpath(self.RESULT_FOUND)
            found = True
        except NoSuchElementException:
            found = False
        return found

    def add_product(self, product_number):
        
        pass
