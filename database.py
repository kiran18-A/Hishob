import mysql.connector
from dotenv import load_dotenv
from urllib.parse import urlparse
import os

load_dotenv()
url=os.getenv("url")

parsed=urlparse(url)
conn=mysql.connector.connect(
    host=parsed.hostname,
    port=parsed.port,
    user=parsed.username,
    password=parsed.password,
    database=parsed.path.lstrip("/") if isinstance(parsed.path, str) else parsed.path.decode().lstrip("/")
)

cursor=conn.cursor()
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS daily_money_flow(id int AUTO_INCREMENT PRIMARY KEY,
                    Date_of_flow DATE NOT NULL,
                    Amount DOUBLE NOT NULL,
                    Type CHAR(10) NOT NULL,
                    Note VARCHAR(10000),
                    User VARCHAR(40)
                    )""")
    conn.commit()
    return True

def enter_new_entry(today_date,amount,types,note,user):
    create_table()
    cursor.execute("INSERT INTO daily_money_flow (Date_of_flow,Amount,Type,Note,User) VALUES (%s,%s,%s,%s,%s)",
                   (today_date,amount,types,note,user))
    conn.commit()
    return True

def calculations(user):
    cursor.execute(
        "SELECT SUM(Amount) FROM daily_money_flow WHERE User=%s AND Type='Income'",
        (user,)
    )
    total_income = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(Amount) FROM daily_money_flow WHERE User=%s AND Type='Expense'",
        (user,)
    )
    total_expenditure = cursor.fetchone()[0] or 0

    total_balance = float(total_income) - float(total_expenditure)

    cursor.execute(
        "SELECT * FROM daily_money_flow WHERE User=%s ORDER BY id DESC",
        (user,)
    )
    data = cursor.fetchmany(10)

    return total_income, total_expenditure, total_balance, data
