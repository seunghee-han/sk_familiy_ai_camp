
import pymysql
import requests

def get_stock(code, s_date, e_date):
    data = eval(requests.get(f"https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={code}&requestType=1&startTime={s_date}&endTime={e_date}&timeframe=day").text.strip())
    conn=pymysql.connect(host='127.0.0.1',user='play',passwd='123',database='sk17',port=3306)
    cur=conn.cursor()
    sql = "insert into  naver_day_stock values (%s,%s,%s,%s,%s,%s,%s)"
    for x in data[1:]:
        try:
            cur.execute(sql, [code]  + x[:-1])
        except Exception as e:
            print(e)
    conn.commit()
