from mysql import connector
import xlwt
import sys



def connet_DB():
    # 定义数据库信息
    db_name = 'algorithm'
    conn = connector.connect(user='test',password='***',host='10.20.0.20',database=db_name,charset='utf8')
    cursor = conn.cursor()
    return conn,cursor

def close_DB(conn,cursor):
    cursor.close()
    conn.close()

def query_to_excel():
    # 选择车辆编号
    bus_id = '1211'
    # 建立连接
    conn,cursor = connet_DB()
    index = 1
    time = 1
    row = 1
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('table_message',cell_overwrite_ok=True)
    while True:
        if index<10:
            query_sql = 'SELECT SUM(cnt_up),SUM(cnt_down) FROM `uits_cnt_log_t_2018-07-0{}` WHERE dev_id = {};'.format(index,bus_id)
        else:
            query_sql = 'SELECT SUM(cnt_up),SUM(cnt_down) FROM `uits_cnt_log_t_2018-07-{}` WHERE dev_id = {};'.format(index, bus_id)
        # 字符串格式查询
        try:
            cursor.execute(query_sql)
            print(query_sql)
        except:
            if index>30:
                break
            index = index + 1
            continue
        # 取出的字段名集合
        columns = cursor.column_names
        # 取出全部数据
        result = cursor.fetchall()
        # 获取字段名
        fileds = cursor.description
        # 写上字段信息
        if not time > 1:
            for filed in range(1,len(fileds)+1):
                sheet.write(0,filed,columns[filed-1])
            time = time + 1
        # format: 左边填充0，宽度为2位数
        sheet.write(row, 0, '2018-07-{:0>2d}'.format(index))
        for col in range(1,len(fileds)+1):
            sheet.write(row, col, result[0][col-1])
        row = row + 1
        index = index+1
        if index > 30:
            break
    workbook.save(r'./dbResult.xls')
    # 关闭连接
    close_DB(conn,cursor)

def main():
    query_to_excel()

if __name__ == '__main__':
    main()
