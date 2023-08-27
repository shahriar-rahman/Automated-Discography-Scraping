import selenium
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from time import sleep
import bs4


class ScrapingUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_driver(options):
        options_type = type(options)

        if options_type is selenium.webdriver.chrome.options.Options:
            options.add_experimental_option("detach", True)
            options.add_argument("--headless=new")
            driver = Chrome(options=options)
            driver.maximize_window()
            return driver

        else:
            raise ValueError("! Invalid 'Option' type. Expected: 'selenium.webdriver.chrome.options.Options'. Got:",
                             options_type)

    @staticmethod
    def open_url(driver, url):
        driver_type = type(driver)

        if driver_type is selenium.webdriver.chrome.webdriver.WebDriver:
            driver.get(url)
            driver.implicitly_wait(5)
            sleep(5)

        else:
            raise ValueError("! Invalid 'Driver' type. Expected: 'selenium.webdriver.chrome.webdriver.WebDriver'. Got:",
                             driver_type)

    @staticmethod
    def bs4_scrape(soup, selector, keyword, attr=False):
        soup_type = type(soup)

        if soup_type is bs4.BeautifulSoup or soup_type is bs4.element.Tag:
            try:
                if selector == 'findAll' or selector == 'find_all':
                    if attr:
                        data = soup.findAll(keyword, attrs=attr)
                        return data

                    else:
                        data = soup.findAll(keyword)
                        return data

                elif selector == 'find':
                    if attr:
                        data = soup.find(keyword, attrs=attr)
                        return data

                    else:
                        data = soup.find(keyword)
                        return data

                elif selector == 'find_next' or selector == 'findNext':
                    if attr:
                        data = soup.find_next(keyword, attrs=attr)
                        return data

                    else:
                        data = soup.find_next(keyword)
                        return data

            except Exception as exc:
                print("! ", exc)
                return ''

            else:
                print("> Attribute successfully scraped.")

        else:
            raise ValueError("! Invalid object. Expected: 'bs4.BeautifulSoup'. Got:", soup_type)


if __name__ == "__main__":
    main = ScrapingUtils()
