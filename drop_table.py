import sqlite3

# 修改為你的資料庫文件路徑
db_path = 'db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 刪除資料表
cursor.execute("DROP TABLE IF EXISTS item_item")

conn.commit()
conn.close()

print("Table item_item has been dropped.")
