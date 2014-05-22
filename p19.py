days = {1:31, 2:28, 3:31, 4:31, 5:31, 6:30, 7:31, 8:31, 9:30, 10:30, 11:31, 12:31}
month = 1
date = 1
day = 1
year = 1900
c = 0
while(year < 2001):
	date += 1
	day += 1
	m = days[month]
	if(month == 2)&(year%4==0):
		m = 29
	if(date > m):
		date = 1
		month += 1
	if(month > 12):
		year += 1
		month = 1
	if(day == 8):
		day = 1
	if(year > 1900)&(day == 7)&(date == 1):
		c += 1

print(c)