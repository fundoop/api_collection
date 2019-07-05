#!/usr/local/bin/python3
#coding:utf-8

import requests
import xlrd
import xlwt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def locatebyLatLng(lat, lng, pois=0):
    '''
    根据经纬度查询地址
    '''
    #这里使用了网上找到的一个ak，百度上注册使用需要身份证号码，暂时就算了
    info = '正在查询' + str(lat) + ', ' + str(lng)
    runInfo.set(info)
    root.update()

    items = {'location': str(lat) + ',' + str(lng), 'ak': 'A9f77664caa0b87520c3708a6750bbdb', 'output': 'json'}
    res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    result = res.json()
    result = result['result']['formatted_address'] + ',' + result['result']['sematic_description']
    return result

def latlngReader(excelFile):
	'''
	这个函数读取excle数据，并根据经纬度调取其它函数以获得地址，最后写入文件
	'''
	#小的代码片段，用来更新界面信息显示，后面不再备注
	info = '读取文件中...'
	runInfo.set(info)
	root.update()

	#打开报表
	data = xlrd.open_workbook(excelFile)
	try:
		table = data.sheet_by_name('经纬度')
	except:
		info = '注意：请把文件中的对应页面命名为“经纬度”，以便识别！'
		runInfo.set(info)
		root.update()
		return None
	row_num = table.nrows
	i = 0
	#建立新的报表以存储结果
	nwb = xlwt.Workbook()
	nws = nwb.add_sheet('result')

	info = '正在问度娘...'
	runInfo.set(info)
	root.update()

	for i in range(row_num):
		if i == 0:
			nws.write(0,0,'经度')
			nws.write(0,1,'纬度')
			nws.write(0,2,'地址')
		else:
			row = table.row_values(i)
			lat = row[1]
			lng = row[0]
			location = locatebyLatLng(lat,lng)
			nws.write(i,0,lng)
			nws.write(i,1,lat)
			nws.write(i,2,location)
			i += 1
	#这里根据上传文件的地址确定查询结果存储地址		
	path = excelFile.split('/')
	pathStr = ''
	i = 0
	for i in range(len(path)-1):
		pathStr = pathStr + path[i] + '/'
	outputPath = pathStr + '地址结果.xls'

	info = ('结果存储在：' + outputPath)
	runInfo.set(info)
	root.update()
	nwb.save(outputPath)

def locatebyAddress(address):
	'''
	根据地址确定经纬度
	'''
	info = '正在查询' + str(address)
	runInfo.set(info)
	root.update()

	items = {'output': 'json', 'ak': 'A9f77664caa0b87520c3708a6750bbdb', 'address': address}
	try:
		res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items, timeout=5)
		result = res.json()
		result = result['result']['location']
	except:
		result = {lng: '抱歉，度娘说她不知道！', lat: ''}
	return result

def addressReader(excelFile):
	'''
	这个函数读取地址，获得经纬度，并保存在新的文件中
	'''
	info = '读取文件中...'
	runInfo.set(info)
	data = xlrd.open_workbook(excelFile)
	try:
		table = data.sheet_by_name('地址')
	except:
		info = '注意：请把文件中的对应页面命名为“地址”，以便识别！'
		runInfo.set(info)
		return None
	row_num = table.nrows
	i = 0
	nwb = xlwt.Workbook()
	nws = nwb.add_sheet('result')
	info = '正在问度娘...'
	runInfo.set(info)
	root.update()

	for i in range(row_num):
		if i == 0:
			nws.write(0,0,'地址')
			nws.write(0,1,'经度')
			nws.write(0,2,'纬度')
		else:
			row = table.row_values(i)
			address = row[0]
			location = locatebyAddress(address)
			nws.write(i,0,address)
			nws.write(i,1,location['lng'])
			nws.write(i,2,location['lat'])
			i += 1
	path = excelFile.split('/')
	pathStr = ''
	i = 0
	for i in range(len(path)-1):
		pathStr = pathStr + path[i] + '/'
	outputPath = pathStr + '经纬度结果.xls'
	info = ('结果存储在：' + outputPath)
	runInfo.set(info)
	root.update()

	nwb.save(outputPath)

#-------------------------------------------------------

#后期增加了操作界面，方便使用，因此主函数就重新写过了
# handleType = input('请选择转换方式：\n1. 经纬度转换为地址；\n2. 地址转换为经纬度；\n(直接输入序号并回车)\n')
# filePath = input('请输入文件地址并回车：')
# print('读取文件地址为：' + filePath)
# print('处理中...')
# if handleType == '1':
# 	latlngReader(filePath)
# elif handleType == '2':
# 	addressReader(filePath)
# else:
# 	print('好像输入有点问题呢！')

#-------------------------------------------------------

def get_filename():
	fpath = str(filedialog.askopenfilename(title = "choose your file",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),('all files','*.*'))))
	fp.set(fpath)

def to_address():
	filePath = fp.get()
	latlngReader(filePath)

def to_latlngs():
	filePath = fp.get()
	addressReader(filePath)

root = tk.Tk()
root.title('经纬度地址转换工具')
root.geometry('600x400')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = ('W' + 'E' + 'N' + 'S'))
mainframe.columnconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.columnconfigure(2, weight = 1)
mainframe.rowconfigure(0, weight = 1)
# mainframe.rowconfigure(1, weight = 1)
# mainframe.rowconfigure(2, weight = 1)
# mainframe.rowconfigure(3, weight = 1)
# mainframe.rowconfigure(4, weight = 1)
# mainframe.rowconfigure(5, weight = 1)
mainframe.rowconfigure(6, weight = 1)
# mainframe.rowconfigure(7, weight = 1)
# mainframe.rowconfigure(8, weight = 1)

fp = tk.StringVar()
runInfo = tk.StringVar()

ttk.Button(mainframe,text = '选择文件', command = get_filename).grid(column = 1, row = 2, sticky = ('W' , 'E'))
ttk.Label(mainframe,textvariable = fp,width = 40).grid(column = 1, row = 1, sticky = ('W' , 'E'))
ttk.Button(mainframe,text = '经纬度转换为地址', command = to_address).grid(column = 1, row = 3, sticky = ('W' , 'E'))
ttk.Button(mainframe,text = '地址转换为经纬度', command = to_latlngs).grid(column = 1, row = 4, sticky = ('W' ,  'E'))
ttk.Label(mainframe,textvariable = runInfo,width = 40).grid(column = 1, row = 5, sticky = ('W' + 'E'))
ttk.Label(mainframe,text = 'V0.4  数据来源：百度地图',font='helvetica 11').grid(column = 1, row = 7)
ttk.Label(mainframe,text = '').grid(column = 1, row = 8, sticky = ('W' , 'E'))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
