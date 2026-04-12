from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit
from datetime import date
from pyspark.sql.types import StructType, DateType, DoubleType, StringType
from database import conn

# today_date=date.today()
#
# spark = SparkSession.builder \
#     .appName("Data Analysis") \
#     .getOrCreate()

# df_schema=StructType().\
#     add("Date",DateType(),True).\
#     add("Amount",DoubleType(),False).\
#     add("Type",StringType(),False).\
#     add("Note",StringType(),True)

total_income=0
total_expenditure=0
total_balance=0

