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
        if not isinstance(soup, (bs4.BeautifulSoup, bs4.element.Tag, bs4.element.ResultSet)):
            raise ValueError(
                f"Invalid object type provided as 'soup': {type(soup)}. Expected: bs4.BeautifulSoup or Tag.")

        try:
            if selector in {'findAll', 'find_all', 'find', 'find_next', 'findNext'}:
                if attr:
                    data = getattr(soup, selector)(keyword, attrs=attr)
                else:
                    data = getattr(soup, selector)(keyword)
                return data

        except Exception as exc:
            print(f"Error during scraping: {exc}")

        return None


if __name__ == "__main__":
    main = ScrapingUtils()
