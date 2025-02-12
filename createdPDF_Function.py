import datetime as dt

fecha_Actual = dt.datetime.today().date()

fecha_Formateada = fecha_Actual.strftime("%d-%b-%Y")

print(fecha_Formateada)