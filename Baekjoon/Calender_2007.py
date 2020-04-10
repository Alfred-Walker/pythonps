# 입력: 첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다.
# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지,
# 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 출력: 첫째 줄에 x월 y일이 무슨 요일인지에 따라
# SUN, MON, TUE, WED, THU, FRI, SAT 중 하나를 출력한다.
#

DayOfWeek = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
ref = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Month, Day = input("").split()
Month, Day = [int(Month), int(Day)]

passedDay = 0
for i in range(0, Month - 1):
    passedDay += ref[i]

passedDay += Day
passedDay = int(passedDay % 7)
print(DayOfWeek[passedDay])
