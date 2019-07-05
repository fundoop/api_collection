def getpois(cityname, keywords):  
    from urllib.parse import quote  
    from urllib import request  
    import json  
    import xlwt  
    from time import sleep
    def getpoi_page(cityname, keywords, page):  
        req_url = 'http://restapi.amap.com/v3/place/text?key=3f89c2ba1ad72586fd5bcb7b581a4e40&extensions=all&keywords=' + quote(keywords) + '&city=' + quote(cityname) + '&citylimit=false&offset=25' + '&page=' + str(page) + '&output=json'  
        data = ''
        print(req_url)
        with request.urlopen(req_url) as f:  
            data = f.read()  
            data = data.decode('utf-8')  
        return data  
      
    def hand(poilist, result):  
        #result = json.loads(result)  # 将字符串转换为json  
        pois = result['pois']  
        for i in range(len(pois)) :  
            poilist.append(pois[i])  
    i = 1  
    poilist = []  
    while True : #使用while循环不断分页获取数据  
        result = getpoi_page(cityname, keywords, i)  
        result = json.loads(result)  # 将字符串转换为json
        if result['count'] == '0':  
            break  
        hand(poilist, result)  
        i = i + 1
        sleep(3)
    return poilist  
  
#获取城市分类数据  
cityname = "上海"  
classfiled = "顺丰"  
pois = getpois(cityname, classfiled)  
for i in pois:print(i['location'])
