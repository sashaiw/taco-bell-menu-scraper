# Taco Bell Menu Scraper
Scrapes the Taco Bell menu and returns as a PANDAS dataframe as such:

```
                                          name  price  min_cals  max_cals
0    Shredded Beef Grilled Cheese Dipping Taco   3.69     360.0     360.0
1                                    Soft Taco   1.79     180.0     180.0
2                           Soft Taco Supreme®   2.69     210.0     210.0
3                       Spicy Potato Soft Taco   1.00     240.0     240.0
4                                 Crunchy Taco   1.79     170.0     170.0
..                                         ...    ...       ...       ...
203                 Breakfast Crunchwrap Bacon   3.79     670.0     670.0
204               Breakfast Crunchwrap Sausage   3.79     760.0     760.0
205                 Breakfast Crunchwrap Combo   5.99     840.0    1120.0
206                                 Hash Brown   1.49     160.0     160.0
213                            Breakfast Salsa   0.00       0.0       0.0
```

## Example usage
```python
from tbms import TBMenuScraper

tbms = TBMenuScraper()
df = tbms.scrape_all()
```