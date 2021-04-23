from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class ScrollToTopError(BasePage):
    URL = 'https://www.carrefour.fr/marques/carrefour-bio'

    def __init__(self, browser):
        super().__init__(browser, self.URL)



    def mouve_to_filter(self):
        element = self.find(
            '/html/body/main/div/div[3]/aside/div[2]/div[2]/form/ul/li[10]/div')
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()

    def listen_to_scroll(self):
        offset_before_click = self.browser.execute_script(
            "return window.pageYOffset"
        )

        las_check = self.find(
            '/html/body/main/div/div[3]/aside/div[2]/div[2]/form/ul/li[10]/div/fieldset/div/div/ul/li[5]/div/label'
        )

        las_check.click()

        offset_after_click = self.browser.execute_script(
            "return window.pageYOffset"
        )

        return offset_after_click < offset_before_click
