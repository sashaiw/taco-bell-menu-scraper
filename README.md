# Taco Bell Menu Scraper
Scrapes the Taco Bell menu and returns as a PANDAS dataframe as such:

```
                                       name  price       calories
0                  Chipotle Cheddar Chalupa  $3.59        420 Cal
1     Chipotle Cheddar Chalupa - Black Bean  $3.59        400 Cal
2            Chipotle Cheddar Chalupa Combo  $7.59  1000-1420 Cal
3                      Black Bean Soft Taco  $1.39        170 Cal
4                   Veggie Burrito Supreme®  $3.89        320 Cal
..                                      ...    ...            ...
188  Grande Toasted Breakfast Burrito Steak  $3.69        560 Cal
189        Grande Toasted Breakfast Burrito  $2.99        560 Cal
191                    Breakfast Crunchwrap  $2.99        670 Cal
198  Mountain Dew® Kickstart™ Orange Citrus  $2.29     70-130 Cal
199                         Breakfast Salsa  $0.00          0 Cal
```

## Example usage
```python
from tbms import TBMenuScraper

tbms = TBMenuScraper()
df = tbms.scrape_all()
```