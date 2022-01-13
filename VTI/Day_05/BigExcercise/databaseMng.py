import pymysql.cursors
from datetime import datetime

# connection database : studentscores
def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 db='studentscores',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection

# def exec : insert, update, delete
def exec(sql, val):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()

# search & return list
def ExecSearch(sql, val):
    list_export = []
    try:
        connection = getConnection()
        print("connect successful!!")
        cursor = connection.cursor()
        cursor.execute(sql, val)
        r = cursor.rowcount
        if r == 0:
            return 0
        else:
            for row in cursor:
                list_tmp = []
                for i in row.keys():
                    list_tmp.append(row[i])
                list_export.append(list_tmp)
            return list_export
    finally:
       connection.close()


