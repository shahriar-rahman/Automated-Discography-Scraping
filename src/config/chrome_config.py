import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions, ActionChains


class ChromeConfig:
    def __init__(self):
        print('> Configuring Chrome Web-Manager.')

    @staticmethod
    def configure(options):
        options_type = type(options)
        if options_type is selenium.webdriver.chrome.options.Options:
            try:
                service = Service()
                driver = webdriver.Chrome(service=service, options=options)
                time.sleep(5)
                driver.quit()

            except Exception as exc:
                print("! ", exc)

            else:
                print("> Chrome configuration is successful.")
                print('Session id:', driver.session_id)

        else:
            raise ValueError("! Invalid parameter type. Expected: 'selenium.webdriver.chrome.options.Options'. Got:",
                             options_type)


if __name__ == "__main__":
    main = ChromeConfig()
