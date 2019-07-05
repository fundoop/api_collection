from pyhive import hive

conn = hive.Connection(host='192.168.109.172', port=10000,auth='NOSASL', username='root', database='default')
cursor=conn.cursor()
cursor.execute('select * from link_expenses limit 1')
for result in cursor.fetchall():
     print(result)
conn.close()
