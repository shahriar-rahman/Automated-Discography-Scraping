import os
import json
import codecs
import selenium
from selenium.webdriver import Chrome
from time import sleep


class GenericUtils:
    def __init__(self):
        pass

    @staticmethod
    def acquire_html(driver, directory, index):
        driver_type = type(driver)

        if driver_type is selenium.webdriver.chrome.webdriver.WebDriver:
            try:
                html_path = os.path.join(directory, f"page{index}.html")
                new_file = codecs.open(html_path, "w", "utf−8")
                page_source = driver.page_source

            except Exception as exc:
                print("! ", exc)

            else:
                new_file.write(page_source)
                new_file.close()
                print("> HTML extraction successful for index", index)

        else:
            raise ValueError("! Invalid 'Driver' type. Expected: 'selenium.webdriver.chrome.webdriver.WebDriver'. Got:",
                             driver_type)

    @staticmethod
    def read_contents(directory):
        try:
            with open(directory, 'r', encoding="utf-8") as new_file:
                contents = new_file.read()

        except Exception as exc:
            print("! ", exc)

        else:
            print("> Contents accessed.")
            return contents

    @staticmethod
    def create_dict(key_list, values_list):
        new_dict = {}

        for i in range(len(key_list)):
            new_dict[key_list[i]] = values_list[i]

        return new_dict

    @staticmethod
    def save_json(file_path, data_dict):
        try:
            with open(file_path, 'w') as file:
                json.dump(data_dict, file)

        except Exception as exc:
            print(f"! Failed to save data. !\n", exc)

        else:
            print("> Json storage is successful.")

    @staticmethod
    def save_df(df, path, ext):
        try:
            if ext == 'csv':
                df.to_csv(path, sep=',')

            elif ext == 'xlsx':
                df.to_excel(path)

        except Exception as exc:
            print(f"! Failed to save data. !\n", exc)

        else:
            print("> Dataframe storage is successful.")

    @staticmethod
    def separator():
        print('\n')
        print('-' * 150)
        print('\n')


if __name__ == "__main__":
    main = GenericUtils()