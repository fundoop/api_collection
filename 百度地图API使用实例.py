from urllib.parse import quote_plus,quote
from hashlib import md5
 
def get_urt(address):
 
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=你的ak
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=gtPDdzQ9HhXotFGG58mgvqMmjtMvlqhN' % address
 
    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
 
    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'GCkFGWfMX4uhHUoA5LiD90Afp6Kbrdj5'
 
    #计算sn
    sn = (md5(quote_plus(rawStr).encode("utf8")).hexdigest())
     
    #由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
    url = quote("http://api.map.baidu.com"+queryStr+"&sn="+sn, safe="/:=&?#+!$,;'@()*[]")  
     
    return url
print(get_urt('信达大厦'))
