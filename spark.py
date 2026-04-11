from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit
from datetime import date
from pyspark.sql.types import StructType, DateType, DoubleType, StringType
from database import conn

cursor=conn.cursor()
today_date=date.today()

spark = SparkSession.builder \
    .appName("Data Analysis") \
    .getOrCreate()

df_schema=StructType().\
    add("Date",DateType(),True).\
    add("Amount",DoubleType(),False).\
    add("Type",StringType(),False).\
    add("Note",StringType(),True)

data_df=spark.read.option("header","true").schema(df_schema).csv(r"data/data.csv")
data_df.createTempView("data")
filter_data=spark.sql(f"select * from data where Date<=('{today_date}') order by Date desc")
filter_data=filter_data.withColumn("User",lit('Kiran'))
filter_data.show()
cursor.execute("""CREATE TABLE IF NOT EXISTS daily_money_flow(id int AUTO_INCREMENT PRIMARY KEY,
                Date_of_flow DATE NOT NULL,
                Amount DOUBLE NOT NULL,
                Type CHAR(10) NOT NULL,
                Note VARCHAR(10000),
                User VARCHAR(40)
                )""")
conn.commit()
for row in filter_data.collect():
    cursor.execute("INSERT INTO daily_money_flow(Date_of_flow,Amount,Type,Note,User) VALUES(%s,%s,%s,%s,%s)",
                   (row[0], row[1], row[2], row[3], row[4]))
    conn.commit()
total_income=0
total_expenditure=0
total_balance=0

