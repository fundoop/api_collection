#coding=utf-8
#今日头条
from lxml import etree
import requests
import urllib
from pandas import DataFrame
#京东查询接口

url='https://search-x.jd.com/Search?keyword=%E7%94%B5%E8%84%91&ad_ids=292%3A100'
headers={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
jd=[url,headers]

url='https://landing.toutiao.com/api/pc/feed/?category=news_world'

headers={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
toutiao=[url,headers]
url = 'http://news.163.com/special/0001220O/news_json.js'
headers = {
'Host': 'news.163.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'Connection': 'Keep-Alive',
'Content-Type': 'text/plain; Charset=UTF-8',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Upgrade-Insecure-Requests': '1'}
wangyi=[url,headers]

def get_url(source):
    url = source[0]
    headers = source[1]
    response = requests.get(url,headers = headers)
    print (response.status_code)
    return response

if __name__ == '__main__':

##    a=eval(get_url(wangyi).content.decode('gbk').replace('var data=','').replace(';',''))
##    wangyi_df=DataFrame()
##    for i in range(len(a['category'])):
##        news_type=a['category'][i]['n']
##        type_link=a['category'][i]['l']
##        for j in range(len(a['news'][i])):
##            title=a['news'][i][j]['t']
##            link=a['news'][i][j]['l']
##            createtime=a['news'][i][j]['p']
##            wangyi_df.append({'news_type':news_type,'type_link':type_link,'title':title,'link':link,'createtime':createtime},ignore_index=True)


##    a=eval(get_url(toutiao).content.decode('unicode_escape').replace('false','False').replace('true','True'))
##    next_news=a['next']['max_behot_time']
##    next_url='https://www.toutiao.com/api/pc/feed/?category=news_world&max_behot_time='+next_news+'&max_behot_time_tmp='+next_news
##    a=a['data']
##    toutiao_df=DataFrame()
##    for i in a:toutiao_df=toutiao_df.append(i,ignore_index=True)
    a=eval(get_url(jd).content.decode('utf-8'))
