import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="user",
  password="4444",
  database="bancodados"
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (2,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros excluídos")
