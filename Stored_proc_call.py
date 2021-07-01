from mysql.connector import MySQLConnection, Error

def call_find_all_sp():
    try:
        conn = MySQLConnection(user='root', password='Ferrari@69',
                                 host='127.0.0.1',
                                 database='gulam')
        cursor = conn.cursor()
        
        #provide stored proc here
        cursor.callproc('find_all')

        # print out the result
        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    call_find_all_sp()