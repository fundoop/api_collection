from pyspark.sql import SQLContext,HiveContext
from pyspark import SparkContext,SparkConf
import os,sys
os.environ["JAVA_HOME"] =r"C:\Program Files\Java\jdk1.8.0_121"
os.environ["SPARK_HOME"] =r"C:\Users\fz\AppData\Local\Programs\spark"
sys.path.append(r"C:\Users\fz\AppData\Local\Programs\spark")
conf = SparkConf().setAppName("abc")
sc = SparkContext(conf=conf)
sqlcontext = HiveContext(sc)
sqlcontext.sql("SET hive.mapred.supports.subdirectories=true")
sqlcontext.sql("SET mapreduce.input.fileinputformat.input.dir.recursive=true")
a=sqlcontext.sql("select * from link_expenses limit 1")
sqlcontext.sql("show databases").toPandas()
sqlcontext.sql("use default")
sqlcontext.sql("show tables").toPandas()





#sqlcontext.sql("drop table if exists link_expenses")
sql="""
CREATE EXTERNAL TABLE `link_expenses`(
  `rowkey` string COMMENT 'from deserializer',
  `orgroot` string COMMENT 'from deserializer',
  `orgcode` string COMMENT 'from deserializer',
  `uid` string COMMENT 'from deserializer',
  `cardno` string COMMENT 'from deserializer',
  `billid` string COMMENT 'from deserializer',
  `extime` string COMMENT 'from deserializer',
  `lastmoney` string COMMENT 'from deserializer',
  `factorage` string COMMENT 'from deserializer',
  `dealaddr_in` string COMMENT 'from deserializer',
  `dealaddr_out` string COMMENT 'from deserializer',
  `dealaddr_intime` string COMMENT 'from deserializer',
  `dealaddr_outtime` string COMMENT 'from deserializer',
  `dealaddr_weight` string COMMENT 'from deserializer',
  `dealaddr_overweight` string COMMENT 'from deserializer',
  `vehinfo_color` string COMMENT 'from deserializer',
  `vehinfo_carnum` string COMMENT 'from deserializer',
  `vehinfo_type` string COMMENT 'from deserializer',
  `vehinfo_desc` string COMMENT 'from deserializer',
  `ordersn` string COMMENT 'from deserializer',
  `createtime_remote` string COMMENT 'from deserializer',
  `createdate` string COMMENT 'from deserializer',
  `createtime` string COMMENT 'from deserializer',
  `lasttime` string COMMENT 'from deserializer',
  `paystatus` string COMMENT 'from deserializer',
  `repaymenttime` string COMMENT 'from deserializer',
  `syncstatus` string COMMENT 'from deserializer',
  `synccode` string COMMENT 'from deserializer',
  `syncmessage` string COMMENT 'from deserializer',
  `g7s_sync` string COMMENT 'from deserializer',
  `synctime` string COMMENT 'from deserializer',
  `remote_data` string COMMENT 'from deserializer',
  `cardorgs` string COMMENT 'from deserializer',
  `orgname` string COMMENT 'from deserializer',
  `carnum` string COMMENT 'from deserializer',
  `is_record` string COMMENT 'from deserializer',
  `read_card_time` string COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.apache.hadoop.hive.hbase.HBaseSerDe'
STORED BY
  'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES (
  'hbase.columns.mapping'=':key,orgroot:a,orgcode:a,uid:a,cardno:a,billid:a,extime:a,lastmoney:a,factorage:a,dealaddr_in:a,dealaddr_out:a,dealaddr_intime:a,dealaddr_outtime:a,dealaddr_weight:a,dealaddr_overweight:a,vehinfo_color:a,vehinfo_carnum:a,vehinfo_type:a,vehinfo_desc:a,ordersn:a,createtime_remote:a,createdate:a,createtime:a,lasttime:a,paystatus:a,repaymenttime:a,syncstatus:a,synccode:a,syncmessage:a,g7s_sync:a,synctime:a,remote_data:a,cardorgs:a,orgname:a,carnum:a,is_record:a,read_card_time:a',
  'serialization.format'='1')
TBLPROPERTIES (
  'COLUMN_STATS_ACCURATE'='false',
  'hbase.mapred.output.outputtable'='link_expenses',
  'hbase.table.name'='link_expenses',
  'numFiles'='0',
  'numRows'='-1',
  'rawDataSize'='-1',
  'totalSize'='0',
  'transient_lastDdlTime'='1558102258')
"""
##sqlcontext.sql(sql)
