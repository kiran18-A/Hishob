import os
import mysql.connector
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()
url=os.getenv("url")
parsed=urlparse(url)
conn=mysql.connector.connect(
    host=parsed.hostname,
    port=parsed.port,
    user=parsed.username,
    password=parsed.password,
    database=parsed.path.lstrip("/")
)
