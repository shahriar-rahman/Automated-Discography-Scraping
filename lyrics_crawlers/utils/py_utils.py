import json
import os


class GenericUtils:
    def __init__(self):
        pass

    @staticmethod
    def load_json(file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path) as json_file:
                    data = json.load(json_file)

            except Exception as exc:
                print("! Failed to load Json File !\n", exc)

            else:
                print("Successfully loaded json file")
                return data

        else:
            raise FileNotFoundError(f"JSON file not found: {file_path}")

    @staticmethod
    def save_json(file_path, data_dict):
        try:
            with open(file_path, 'w') as file:
                json.dump(data_dict, file)

        except Exception as exc:
            print(f"! Failed to save data. !\n", exc)

        else:
            print("Json storage is successful.")

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
            print("Dataframe storage is successful.")

    @staticmethod
    def load_separator(*arg):
        if arg == 'dash':
            print('-' * 150)

        elif arg == 'underscore':
            print('_' * 150)

        else:
            print('-' * 150)

    @staticmethod
    def str_convert(text):
        if text is None:
            return ''
        else:
            return ''.join(text)

    def generic_output(self, output):
        self.load_separator('underscore')
        print('◘ ', output)
        self.load_separator('dash')

    def display_dict(self, text, data_dict):
        self.generic_output(text)
        for column in data_dict:
            print(column, data_dict[column])


if __name__ == "__main__":
    main = GenericUtils()
