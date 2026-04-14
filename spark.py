from database import conn
import pandas as pd

def spark_calculations(name):
    query="select * from daily_money_flow where User=%s"
    data=pd.read_sql(query,conn,params=(name,))
    print(data["Amount"])
spark_calculations('Kiran')