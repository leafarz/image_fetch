import re, calendar

def parse_month(m):
	length = len(m)
	if length == 2:
		return m
	
	# assume abbreviated month
	else:
		return calendar.month_abbr[m[0:3]]
		
def parse_date(string):
	m, d, y, *_ = re.split(",|-|/|\n", string)
	
	# m = parse_month(m.islower)
	# m = [m for month in calendar.month_abbr if m.islower() == month.islower()]
	return (m, d, y)