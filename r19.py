import pyodbc as pd
import datetime as dt
from config import *
import requests as rq

# код даты для таблицы
date_format = dt.datetime.now().strftime('%Y%m')

# максимальная дата TS
bd_max_date = cursor.execute("select max(TS) as t_s  from FACT_AVG_RR").fetchone()
bd_max_date.t_s = dt.datetime.date(bd_max_date.t_s)

# max data file.txt
data = []
file_open = open(filename, "r")

# узнаем максимальную дату txt файла
txt_max_date = []
for j in file_open:
    txt_max_date.append(j.split()[0])
txt_max_date = max(txt_max_date)
txt_max_date = dt.datetime.strptime(txt_max_date, '%d.%m.%Y').date()


# формируем список заполняемых дат
lst_date = [txt_max_date]

for j in range(15):

    list_date = cursor_support.execute(
        "select WORKING as workdays_working, DATE as workdays_date from WORKDAYS WHERE  DATE = ?",
        (txt_max_date + dt.timedelta(days=j + 1))).fetchone()

    if not list_date.workdays_working:
        lst_date.append(dt.datetime.date(list_date.workdays_date))
    else:
        break

# print(lst_date)

file_open_r = open(filename, "r")


for j in file_open_r:

    BANK = j.split()[1]
    FACT_AVG_RR = j.split()[5]
    FACT_AVG_RR = float(FACT_AVG_RR)/1000000
    TS = dt.datetime.now()

    for i in lst_date:
        MP_CODE = dt.datetime.strftime(i, '%Y%m')
        MP_DATE = i
        print(type(MP_DATE))


            # cursor.execute(
            #     'insert into FACT_AVG_RR(MP_CODE,)'
            #)








# for i in lst_date:
#     MP_DATE = i
#     for j in file_open_r:
#         MP_CODE = dt.datetime.strptime(j.split()[0], '%d.%m.%Y').date()
#         MP_CODE = dt.datetime.strftime(MP_CODE, '%Y%m')
#
#         BANK = j.split()[1]
#         MP_DATE = MP_DATE
#
#
#     print(MP_DATE)





# date_format = dt.datetime.now().strftime('%Y%m')

# for q in file_open_r:
#
#     print(q.split()[1])







# print(txt_max_date)
# print(list_date.ddd)


# for i in list_date:
#     print(i)

# print(list_date)


# print(txt_max_date)


# print(bd_max_date.t_s)
