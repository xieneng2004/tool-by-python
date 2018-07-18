from mysql import connector

def connet_DB():
    db_name = 'algorithm'
    conn = connector.connect(user='test',password='xzy123',host='10.20.0.20',database=db_name,charset = 'utf8mb4')
    cursor = conn.cursor()
    return conn,cursor

def close_DB(conn,cursor):
    cursor.close()
    conn.close()

def query():
    # 建立连接
    conn,cursor = connet_DB()
    index = 1
    while True:
        query_sql = 'SELECT SUM(cnt_up),SUM(cnt_down) FROM `uits_cnt_log_t_2018-07-0{}` WHERE dev_id = 1211;'.format(index)
        # 字符串格式查询
        try:
            cursor.execute(query_sql)
        except:
            continue
        # 取出的字段名集合
        columns = cursor.column_names
        # 取出全部数据
        result = cursor.fetchall()
        print('2018-07-0{}:'.format(index))
        print('字段名:{}'.format(columns))
        print('结果:{}'.format(result))
        index = index+1
        if index > 10:
            break

    # 关闭连接
    close_DB(conn,cursor)

def main():
    query()

if __name__ == '__main__':
    main()
