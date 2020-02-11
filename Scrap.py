from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import BytesIO
import urllib.parse
import requests
import math


class WebScrap:

    def __init__(self):
        self.url = "https://www.cftc.gov/MarketReports/financialfcmdata/index.htm"
        
        

    def WebScrapFunction(self,current_excel_month):

        try:
       
            year=current_excel_month.split(" ")[1]
         
            
           
            url_response = requests.get(self.url)
            soup = BeautifulSoup(url_response.content)
            lst_of_url=[]

            # selects all tables
            for table in soup.find_all("table"):
                # selects all tables containing the specified year
                if table.find_all(text=year) != []:
                    # selects all a tags with the url containing ".xlsx"
                    lst_of_url= table.select("a[href*='.xlsx']")


            # select the first xlsx sheet url      
            # first_row=lst_of_url[1]
            for raw_href in lst_of_url:
                if current_excel_month.split(" ")[0] in raw_href["href"]:
                    current_excel_href=raw_href["href"]

        

            return current_excel_href

        except Exception as e:
            print(str(e))
            raise
