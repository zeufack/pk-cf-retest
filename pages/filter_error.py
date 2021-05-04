from bs4 import BeautifulSoup

from pages.base_page import BasePage


class FilterError(BasePage):
    URL = 'https://www.carrefour.fr/marques/carrefour-bio'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def set_filter_decroissant(self):
        cat_btn = self.browser.find_by_xpath(
            '/html/body/main/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/span')
        cat_btn.click()
        cat = self.browser.find_by_xpath(
            '/html/body/main/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div/div/div[3]/ul/li[2]/span')
        cat.click()

    def get_categorie_sort_status(self):
        self.set_filter_decroissant()
        soup = BeautifulSoup(self.browser.source, features="html.parser")
        list_of_product = soup.find_all("ul", {"id": "data-plp_produits"})[1]
        prices = []
        for child in list_of_product.find_all('li'):
            if child.find("span", {"class": "ds-title"}) != None:
                prices.append(child.find(
                    "span", {"class": "ds-title"}).text.strip().replace(',', '.').replace('€', ''))
        isSorted = True
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[i] > prices[j]):
                    isSorted = False

        return isSorted
