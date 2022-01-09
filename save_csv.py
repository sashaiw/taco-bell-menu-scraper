from tbms import TBMenuScraper

if __name__ == "__main__":
    tbms = TBMenuScraper()
    df = tbms.scrape_all()
    df.to_csv("taco_bell_menu.csv")
