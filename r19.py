import pyodbc as pd
import datetime as dt
from config import *
import config


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


# формируе список действующих банков
list_bank_prepare = cursor_support.execute(
    "select HQ_code as BANK from bank_HQ_codes where FOR = ?",
    True
).fetchall()

list_bank = []
for i in list_bank_prepare:
    if i[0]:
        list_bank.append(i[0])

file_open_r = open(filename, "r")

# connection to access
driver_a = config.driver
con_a = pd.connect(driver_a)
cursor_a = con_a.cursor()

if bd_max_date.t_s < dt.datetime.now().date() and txt_max_date == (dt.datetime.now().date() - dt.timedelta(days=1)):
    for j in file_open_r:

        BANK = int(j.split()[1])
        FACT_AVG_RR = j.split()[5]
        FACT_AVG_RR = float(FACT_AVG_RR) / 1000000
        TS = dt.datetime.now()

        if BANK in list_bank:
            for i in lst_date:
                MP_CODE = int(dt.datetime.strftime(i, '%Y%m'))

                MP_DATE = dt.datetime.strftime(i, '%d.%m.%Y')
                MP_DATE = dt.datetime.strptime(MP_DATE, '%d.%m.%Y')

                cursor_a.execute('insert into FACT_AVG_RR(MP_CODE, BANK, MP_DATE, FACT_AVG_RR, TS) values(?, ?, ?, ?, ?)', MP_CODE, BANK, MP_DATE, FACT_AVG_RR, TS)
                con_a.commit()

print('Финиш')