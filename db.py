import pymysql

def printdb():
    try: 
        conn = pymysql.connect(
            user = 'root',
            password = 'Ferrari@69',
            host = '127.0.0.1',
            database = 'gulam',
            )

        cur = conn.cursor()
        query = ("select * from gulam.inventory")
        cur.execute(query)
        rows = cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        for s in field_names:
            print(s, end='   ')
        for s in rows :
            print(s, end='   ')
            # print(f'%s  %s %s' %(s[0], s[1], s[2]), end='   ')
    except Exception as e:
        print("Error occured. Please rectify : " + str(e))
    
    finally:
        conn.close()



if __name__ == '__main__':
    printdb()