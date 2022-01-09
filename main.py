import requests
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


class TBMenuScraper:
    def __init__(self):
        self.agent = {"User-Agent": "Mozilla/5.0"}

    def scrape_all(self):
        """
        scrape all pages found by ``get_all_pages()``
        :return: PANDAS dataframe containing all Taco Bell menu items
        """
        menu_item_list = []

        for url in self.get_all_pages():
            print(f"Scraping {url}...")
            for name, price, calories in self.scrape_page(url):
                menu_item_list.append([name, price, calories])

        return pd.DataFrame(menu_item_list, columns=("name", "price", "calories")).drop_duplicates()

    def get_all_pages(self):
        """
        return urls of all menu pages scraped from main page
        :return: all menu pages
        :rtype: Iterator[str]
        """
        page = requests.get("https://www.tacobell.com/food", headers=self.agent)
        soup = BeautifulSoup(page.content, "html.parser")

        tiles = soup.find_all("div", class_=re.compile("menu-tile___3x64l menu-tile___weSh0"))
        for tile in tiles:
            link = tile.find("a")
            yield "https://tacobell.com" + link.get("href")

    def scrape_page(self, url):
        """
        scrape a menu page for name, price, and calories
        :return: tuples of menu items containing (name, price, calories)
        :rtype: Iterator[str]
        """
        page = requests.get(url, headers=self.agent)
        soup = BeautifulSoup(page.content, "html.parser")

        product_items = soup.find_all("div", class_="product-item")
        for product_item in product_items:
            # get product name
            product_name = product_item.find("div", class_="product-name").text.strip()

            # get product price
            product_price = product_item.find("div", class_="product-price").text.strip()

            # get product calories
            product_calorie = product_item.find("div", class_="product-calorie").text.strip()

            yield product_name, product_price, product_calorie


if __name__ == "__main__":
    tbms = TBMenuScraper()
    print(tbms.scrape_all())
