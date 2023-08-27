import os
import sys
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
sys.path.append(os.path.abspath('../config'))
sys.path.append(os.path.abspath('../crawler_utils'))
from chrome_config import ChromeConfig
from scraping_utils import ScrapingUtils as su
from discography_utils import DiscographyUtils as du
from common_utils import GenericUtils as gu

root_link = 'https://www.azlyrics.com'
user_input = ['ThE BeatlEs', 'LinkIn Park', 'Metallica', 'Black Sabbath', 'Led Zeppelin']
path = 'C:/Users/pc/PycharmProjects/Discography-Scraping/webpage/artist'

div_key = 'div'
artist_key = 'title'
href_attr = {'class': 'listalbum-item'}
album_attr = {'class': 'album'}
parent_tag_attr = {'id': 'listAlbum'}
album_class = ['album']
track_class = ['listalbum-item']


class GetDiscography:
    def __init__(self):
        # Chrome Set-ups
        self.options = webdriver.ChromeOptions()
        # ChromeConfig.configure(self.options)   INSTALLER

        # Link Generation
        self.start_urls = []
        filtered_input = du.discard_prefix(user_input, 'the')
        for artist in filtered_input:
            self.start_urls.append(du.generate_link(root_link, artist))

    def selenium_html(self):
        for i, url in enumerate(self.start_urls):
            driver = su.create_driver(self.options)
            su.open_url(driver, url)
            gu.acquire_html(driver, path, i)
            driver.quit()

    def scrape_html(self):
        list_href = []
        list_tracks = []
        list_artist = []
        scraped_album = []
        scraped_counts = []
        max_items = len(self.start_urls)

        for index in range(max_items):
            contents = gu.read_contents(f'../../webpage/artist/page{index}.html')
            soup = BeautifulSoup(contents, 'lxml')

            # Scrape tracks + href
            scraped_tracks = su.bs4_scrape(soup, 'findAll', div_key, href_attr)
            iteration = du.filter_tracks(scraped_tracks, list_tracks, list_href, root_link)

            # Artist
            artist = su.bs4_scrape(soup, 'find', artist_key).text
            du.populate_artist(artist, list_artist, iteration)

            # Scrape & Systemize Albums
            parent_tag = su.bs4_scrape(soup, 'find', div_key, parent_tag_attr)
            scraped_albums = su.bs4_scrape(parent_tag, 'findAll', div_key)
            du.sort_albums(scraped_albums, scraped_album, scraped_counts, album_class, track_class)
            gu.separator()

        # Debugging
        du.compare_length(list_href, list_tracks)
        du.compare_length(scraped_album, scraped_counts)

        # Populate albums
        list_album = []
        du.create_album_list(list_album, len(list_href), scraped_album, scraped_counts)

        # Storage
        key_list = ['Tracks', 'Artist', 'Albums', 'Links']
        values_list = [list_tracks, list_artist, list_album, list_href]
        discography_dict = gu.create_dict(key_list, values_list)

        gu.save_json('../../dataset/discography_data.json', discography_dict)
        df = pd.DataFrame(discography_dict, columns=key_list)
        gu.save_df(df, '../../dataset/discography_data.xlsx', 'xlsx')
        gu.save_df(df, '../../dataset/discography_data.csv', 'csv')


if __name__ == "__main__":
    main = GetDiscography()
    # main.selenium_html()
    main.scrape_html()
