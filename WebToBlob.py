from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import BytesIO
import urllib.parse
import requests
import math



class AzureBlobStoage:

    def __init__(self):
        self.account_name = 'fiasourcefiles'
        self.account_key = '0CIeDTnJl7b1ehEV4TclQ9jOr3KtUDEEALJrkLEh2QuJ/I1yrsiGZTejKACB1rH+zdZSSiWceCxi41kJO9rf7g=='
        

    def LocalToBlob(self,export_csv,filenamevalue):


        try:
          
            

            block_blob_service = BlockBlobService(account_name=self.account_name,account_key=self.account_key)
            block_blob_service.create_blob_from_text(
                'fcmcontainer',
                filenamevalue+'.csv',
                export_csv
                )
            return "success"

        except Exception as e:
            print(str(e))
            raise

