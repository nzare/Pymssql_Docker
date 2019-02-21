import pymssql
import pandas as pd
con = pymssql.connect('DRIVER=;SERVER={};PORT:{};DATABASE={};UID={};PWD={}'.format(self.db_config['driver'],
self.db_config['server'],
self.db_config['port'],
self.db_config['database'],
self.db_config['uid'],
self.db_config['pwd']))
con.execute("USE TEST")

df=pd.read_sql('SELECT * FROM [TEST]', self.con)

driver: 'ODBC Driver 17 for SQL Server' # change to what you found in libsqlvdi.so
port: 1433 # default MSSQL port. 
server: localhost # default path of MSSQL server
database: DATABASE # change to the name of target database
uid: sa # default user name of MSSQL. Change if necessary
pwd: ********** # change to password