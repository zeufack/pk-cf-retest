from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebBrowser(object):
    __TIMEOUT = 10

    def __init__(self, browser):
        super().__init__()
        self.__browser = browser
        self.__browser_wait = WebDriverWait(self.__browser, self.__TIMEOUT)

    def open(self, url):
        self.__browser.get(url)

    def use_frame(self, frame):
        self.__browser.switch_to.frame(frame)

    def source(self):
        return self.__browser.page_source

    def find_by_xpath(self, xpath):
        return self.__browser_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_all_by_xpath(self, xpath):
        return self.__browser_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self.__browser_wait.until(EC.presence_of_element_located((By.NAME, name)))

    def find_by_class_name(self, class_name):
        return self.__browser_wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    def find_by_id(self, id):
        return self.__browser_wait.until(EC.presence_of_element_located((By.ID, id)))

    def execute_js(self, js_code):
        return self.__browser.execute_script(js_code)

    def find_by_selector(self, css_selector):
        return self.__browser_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def get_browser(self):
        return self.__browser

    def wait(self, time):
        self.__browser.implicitly_wait(time)

    def quit(self):
        self.__browser.quit()
