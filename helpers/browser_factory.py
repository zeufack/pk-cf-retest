from helpers.chrome_browser import ChromeBrowser
from helpers.chrome_proxy_browser import ChromeProxyBrowser
from helpers.firefox_browser import FirefoxBrowser


def get_browser(browser):
    if browser == 'chrome':
        return ChromeBrowser()
    elif browser == 'chrome_proxy':
        return ChromeProxyBrowser()
    else:
        return FirefoxBrowser()
