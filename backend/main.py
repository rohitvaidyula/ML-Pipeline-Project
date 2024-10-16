#All the necessary imports 
import os
import pandas as pd
import matplotlib
import seaborn 
import requests
from datetime import datetime
from bs4 import BeautifulSoup


#Importing the Lending Dataset 
lending_df = pd.read_csv('path_to_csv', low_memory=False) 
#We're using low_memory = False because the lending_club dataset is quite large (700MB)! 

#Importing the monthly unemployment dataset
unemp_df = pd.read_excel('path_to_xlsx')

#Importing the Inflation Dataset 
def scrape():
    url = "https://www.usinflationcalculator.com/inflation/current-inflation-rates/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    inflation_csv = 'scraped_file_'+ datetime.today().strftime('%Y_%m_%d') + '.csv' #Setting the title of the CSV file
    tabled_titles = soup.select("div[class = 'td-pb-span8 td-main-content'] > div[class = 'td-ss-main-content'] > div[class = 'td-page-content tagdiv-type'] > p > strong") #Getting the table title
    print(tabled_titles[0].get_text())    
    with open(inflation_csv, 'w') as r:
       print(tabled_titles[0].get_text(), file=r)
       #Using the HTML table > tbody > tr > td to get the 
       for item in soup.find('table').find_all('tr'): 
        row_data = ','.join([td.text for td in item.find_all('td')])
        print(row_data, file=r)
            
        
if __name__ == '__main__':
    scrape() 