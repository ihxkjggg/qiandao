import os.path

import pandas as pd
import sqlite3
import datetime
import matplotlib.pyplot as plt

now = datetime.datetime.today().strftime('%Y/%m/%d')
conn = sqlite3.connect('database.db')
df = pd.read_excel('D:\R3拦截索赔\R3JETTA拦截2024.xlsm',sheet_name='2024Jetta数据')
df = df.drop_duplicates(subset='索赔单号')
df = df[df['R3处理日期']==now]
# df = df[df['R3处理日期']>"2024-02-21"]
df.to_sql('R3', conn, index=False,if_exists='append')
conn.close()
