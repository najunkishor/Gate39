
from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import BytesIO
import urllib.parse
import requests
import math
import datetime
import urllib.parse




class ExportExcelToCsv:

    def __init__(self):
        self.baseurl = "https://www.cftc.gov"

    def Excel_to_csv(self,current_excel_href,filenamevalue):
        try:
           
            excel_file = xlds =BytesIO(requests.get(self.baseurl+current_excel_href).content)
            df = pd.read_excel(excel_file,index_col = None)
            df2=df.dropna()
            
            renamed_column1=df2.columns[1]
            renamed_column2=df2.columns[4]
           
            
            df1 =df2.rename(columns={renamed_column1:"FCM",renamed_column2:"TradeDate"})
            first_column = df1.columns[0]
            df = df1.drop([first_column], axis=1)
            df['FCM_FileName'] = df.apply(lambda row: filenamevalue, axis = 1)
            
            
            export_csv = df.to_csv(index_label="idx", encoding = "utf-8")
            return export_csv
        except Exception as e:
            print(str(e))
            raise

