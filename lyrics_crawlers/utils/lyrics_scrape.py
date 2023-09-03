import string


class LyricsScrape:
    def __init__(self):
        pass

    @staticmethod
    def generate_links(root_link):
        # alphabets a to z and #
        alphabets = [letter for letter in string.ascii_lowercase]
        alphabets.append('19')

        start_urls = []
        for letter in alphabets:
            start_urls.append(root_link+letter+'.html')

        return start_urls


if __name__ == "__main__":
    main = LyricsScrape()
    main.generate_links()

