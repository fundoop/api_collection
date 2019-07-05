from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14953014'
API_KEY = 'ldERsm2tTwHhsUwTVP8LAkfG'
SECRET_KEY = 'pB8K9g6eNK5Np7bxQkZgdnaY2442vOdz'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
img=open('9BF2B3C1-6F57-466d-979D-41CDD13B6200.png','rb').read()
print(client.idcard(img,idCardSide))
