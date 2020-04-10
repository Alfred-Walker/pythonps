import datetime as dt
# https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/

time_now = dt.datetime.now()
print(time_now)
print(time_now.weekday())  # (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)

time_now = dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M")
print(time_now)