import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='*********',
                                    database='company')

cursor = connection.cursor()

# 新增
# cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL)")


# 修改
# cursor.execute('UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 4;')


# 刪除
cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")


cursor.close()
connection.commit() #動到資料,需要commit提交資料
connection.close()