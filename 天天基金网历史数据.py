# -*- coding: utf-8 -*-

import requests
import bs4
import pandas as pd
from sqlalchemy import create_engine
from pandas.io import sql
from sqlite3 import connect

def obtain_info_of_data(symbol):
    response = requests.get('http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=' + str(symbol))
    # return format: var apidata={...};
    # filter the tag
    content = str(response.text.encode('utf8')[13:-2])
    content_split = content.split(',')
    # obtain the info of data, curpage, pages, records
    curpage = content_split[-1].split(':')[-1]
    pages = content_split[-2].split(':')[-1]
    records = content_split[-3].split(':')[-1]
    return {'curpage': curpage, 'pages': pages, 'records': records}



def obtain_data(symbol,engine):
    dict_data_info = obtain_info_of_data(symbol)
    cur_pages = int(dict_data_info['pages'])
    pages = dict_data_info['pages']
    records = dict_data_info['records']

    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&page=%s'
    data_return=[]
    for cp in range(int(pages), 0, -1):
        
        response = requests.get(url % (symbol, str(cp)))
        data=bs4.BeautifulSoup(response.text, 'lxml')
        head=[j.get_text() for j in data.find_all('th')]
        for i in data.find_all('tr'):
            tmp=[j.get_text() for j in i.find_all('td')]
            if len(tmp)==len(head):data_return.append([symbol]+tmp)
            elif len(tmp)!=0:print('Fail:'+str(tmp))
    rs=pd.DataFrame(data_return,columns=['编码']+head)
    
    print(rs)
    rs.to_sql('tablea'+str(symbol),engine,if_exists='append',index=False)

    print ('Finished '+symbol+"  "+str(dict_data_info))


if __name__ == '__main__':
    SYMBOL_LIST=eval(requests.get('http://fund.eastmoney.com/js/fundcode_search.js').text[8:-1])
    engine = create_engine('sqlite:///stock.db', echo = False)
    for i in SYMBOL_LIST:
        if i[0] in ['000198','003042']:obtain_data(i[0],engine)
        
