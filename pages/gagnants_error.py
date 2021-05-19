from pages.base_page import BasePage


class GagnantsError(BasePage):
    URL = "https://carrefour.fr/jeux-concours"
    gagnat_btn_xpath_first = "/html/body/main/div/section/div/div/a[2]"
    gagnats_btn_xpath_second = "/html/body/main/div/div[2]/article[1]/div/a"

    def __init__(self, browser):
        super().__init__(browser, url=self.URL)

    def nav_to_gagnants(self):
        btn_first = self.browser.find_by_xpath(self.gagnat_btn_xpath_first)
        btn_first.click()
        btn_second = self.browser.find_by_xpath(self.gagnats_btn_xpath_second)
        btn_second.click()

    def get_list_gagnants(self):
        self.browser.mv_to_ltab()
        return self.browser.find_by_tag('h1').text
