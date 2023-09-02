import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
sys.path.append(os.path.abspath('../config'))
sys.path.append(os.path.abspath('../crawler_utils'))
from scraping_utils import ScrapingUtils as su
from discography_utils import DiscographyUtils as du
from common_utils import GenericUtils as gu

root_link = 'https://www.azlyrics.com'
div_tag = 'div'
a_tag = 'a'
div_attr = {'class': 'col-sm-6'}
pages = 28


class AllArtists:
    def __init__(self):
        self.scraped_data = {}

    def scrape_all_artists(self):
        for index in range(1, pages):
            # Scraping Mechanism
            contents = gu.read_contents(f'../../webpage/all_artists/page{index}.html')
            soup = BeautifulSoup(contents, 'lxml')

            scraped_cols = su.bs4_scrape(soup, 'find_all', div_tag, div_attr)

            for col in scraped_cols:
                scraped_col = su.bs4_scrape(col, 'find_all', a_tag)

                for r in scraped_col:
                    self.scraped_data[r.text] = r.get('href')

        # Storage
        artists_dict = {'Artists': self.scraped_data}
        gu.save_json('../../dataset/artists_data.json', artists_dict)

        columns = ['Artists', 'URLs']
        artists_df = pd.DataFrame(artists_dict).reset_index()
        artists_df.columns = columns
        gu.save_df(artists_df, '../../dataset/artists_data.xlsx', 'xlsx')
        gu.save_df(artists_df, '../../dataset/artists_data.csv', 'csv')


if __name__ == "__main__":
    main = AllArtists()
    main.scrape_all_artists()
