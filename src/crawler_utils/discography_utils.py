from common_utils import GenericUtils as gu
from scraping_utils import ScrapingUtils as su


class DiscographyUtils:
    def __init__(self):
        pass

    @staticmethod
    def discard_prefix(arg_list, keyword):
        mod_list = []

        if len(arg_list) > 0:
            for item in arg_list:
                item = item.lower()

                if keyword in item.split(' ')[0]:
                    item = item.replace('the ', '')

                item = item.replace(' ', '')
                mod_list.append(item)
            return mod_list

        else:
            raise IndexError("! The list parameter is empty.")

    @staticmethod
    def generate_link(root_link, artist):
        post_slash = ''

        if root_link.startswith("https:") or root_link.startswith("http:"):
            if root_link[-1] != '/':
                post_slash = '/'
            return root_link + post_slash + artist[0] + '/' + artist + '.html'

        else:
            raise ValueError("! The Root link does not contain a valid url.")

    @staticmethod
    def filter_tracks(scraped_data, list_tracks, list_href, root_link=False):
        for i, data in enumerate(scraped_data):
            try:
                list_tracks.append(su.bs4_scrape(data, 'find', 'a').text)

            except Exception as exc:
                print("! ", exc)
                list_tracks.append('n/a')

            try:
                list_href.append(root_link + su.bs4_scrape(data, 'find', 'a')['href'])

            except Exception as exc:
                print("! ", exc)
                list_href.append('n/a')

        return i

    @staticmethod
    def sort_albums(scraped_albums, list_album, list_counts, album_class, track_class):
        count = 0

        # Correctly organize sequence
        for tag in scraped_albums:
            class_tag = tag.get('class')
            if class_tag is not None:
                if class_tag == album_class:
                    list_album.append(' '.join(tag.text.split(' ')[1:]))
                    if count != 0:
                        list_counts.append(count)
                    count = 0

                elif class_tag == track_class:
                    count += 1
        list_counts.append(count)

    @staticmethod
    def compare_length(list_1, list_2):
        size_list_1 = len(list_1)
        size_list_2 = len(list_2)

        if size_list_1 == size_list_2:
            print(f"> Compatible lists size. ({size_list_1})")

        else:
            raise IndexError(f"! Incompatible List Size. List1 = {size_list_1}, List_2 = {size_list_2}")

    @staticmethod
    def create_album_list(list_album, list_album_len, scraped_album, scraped_counts):
        counter = 0
        scraped_index = 0

        for row in range(list_album_len):
            counter += 1

            if counter > scraped_counts[scraped_index]:
                counter = 1
                scraped_index += 1

            list_album.append(scraped_album[scraped_index])

    @staticmethod
    def populate_artist(artist, list_artist, iteration):
        postfix_checker = artist.split(' ')

        if postfix_checker[-1] == "Lyrics":
            artist = ' '.join(postfix_checker).replace(' Lyrics', '')

        for i in range(iteration + 1):
            list_artist.append(artist)


if __name__ == "__main__":
    main = DiscographyUtils()

