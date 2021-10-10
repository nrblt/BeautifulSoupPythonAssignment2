from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

#
class ParseArticle:
    def scrapInformation(self,nameOfCurrency):

        URL='https://coinmarketcap.com/currencies/'+nameOfCurrency+'/news/'
        r = requests.get(URL, 'html.parser').text
        soup= BeautifulSoup(r,'lxml')
        header=soup.h2.text
        print(header,'\n')
        allText=soup.text.strip()
        cnt=0
        for i in range(len(allText)):
            print(allText[i],end='')
            if allText[i]==' ':
                cnt+=1
            if cnt==8:
                print('\n',end='')
                cnt=0
        print()
        print('----------------------------------------------------------------------')
        print('\n\n\n')






