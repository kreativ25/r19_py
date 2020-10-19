import pyodbc as pd

# блок подключения к БД Бюджета
driver = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=d:\_BIG_DATA\base_backap\BASE_RR.mdb;'
)
con = pd.connect(driver)
cursor = con.cursor()

filename = r"\\rootfs3\Data\GUOFR\URL\ABS_UOR\F3607.TXT"


# база с рабочими/выходными днями
driver_support = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=d:\R\00_common\Support001.mdb;'
)

con_support = pd.connect(driver)
cursor_support = con_support.cursor()