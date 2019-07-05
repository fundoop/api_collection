# 使用前需要启动hbase和thrift服务器
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol,TCompactProtocol
from hbase import Hbase
from hbase.ttypes import Mutation,BatchMutation,ColumnDescriptor

from FZ import *


def hbase_connect():
            
    # thrift默认端口是9090
    socket = TSocket.TSocket('192.168.109.172',9090)
    socket.setTimeout(5000)

    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Hbase.Client(protocol)
    socket.open()
    return client

def put_hbase(dataframe,table,rowid):
    head=dataframe.columns.values.tolist()
    if rowid in head:
        head=[i for i in head if i!=rowid]
    else:rowid=False
    client=hbase_connect()
    alltable = client.getTableNames()
    print(alltable)
    if table not in alltable:
        columns=[]
        for i in head:
            columns.append(ColumnDescriptor(name=i))
        client.createTable(table, columns)
    for i in range(len(dataframe)):
        mutations=[]
        for j in head:
            mutations.append(Mutation(column=j+':a', value=str(dataframe.loc[i,j])))
            
        if rowid:batchMutation = [BatchMutation(str(dataframe.loc[i,rowid]),mutations)]
        else:batchMutation = [BatchMutation(str(i),mutations)]
        try:
            tmp=client.mutateRows(table,batchMutation)
        except:
            client=hbase_connect()
            client.mutateRows(table,batchMutation)
##        print('成功：'+str(dataframe.loc[i,rowid]))
##    print('成功:'+table+str(len(dataframe)))


##sql="""select * from link_etcexpenses limit 100"""
##df=get_data(sql,connect('cat_link'))
##a=put_hbase(df,'link_expenses','id')
####client=hbase_connect()
####print(client.isTableEnabled('link_expenses'))
####client.disableTable('link_expenses')
####client.deleteTable('link_expenses')
import datetime
i=0
now = datetime.datetime.now()
fail=[]
while True:
    tmp=(now-datetime.timedelta(days=i)).strftime('%Y-%m-%d')
    try:
        sql="""select * from link_etcexpenses where createdate='"""+tmp+"""'"""
        df=get_data(sql,connect('cat_link'))
        a=put_hbase(df,'link_expenses','id')
        print(tmp+'成功：'+str(len(df)))
    except:
        print(tmp+'失败')
        fail.append(tmp)
        with open('fail.txt','w') as f:
            f.write(str(fail))
    i+=1
