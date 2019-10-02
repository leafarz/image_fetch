import re, calendar, datetime

def parse_month(m):
	length = len(m)
	if length == 2:
		return m
	
	# assume abbreviated month
	else:
		return calendar.month_abbr[m[0:3]]
		
def parse_date(string):
	m, d, y, *_ = [el for el in re.split(",|-|/| |\n", string) if el != '']
	
	# convert to number
	if len(m) > 2:
		m = [str(i) for i, month in enumerate(calendar.month_abbr) if month.lower()==m[0:3].lower()]
		m = ''.join(m)

	if len(m) == 1:
		m = '0' + m

	# append 0 before day if 1 digit
	if len(d) == 1:
		d = '0' + d

	# convert 2 digit year to 4 digits
	if len(y) < 3:
		curr_year = datetime.datetime.now().year % 100
		year = int(y)
		
		# if last 2 digits <= last 2 digits of today's year,
		# we assume the year to be in the 2000s, else in the 1900s
		if year <= curr_year:
			y = str(2000 + int(y))
		else:
			y = str(1900 + int(y))

	try:
		datetime.datetime.strptime(f'{y}-{m}-{d}', '%Y-%m-%d')
		return (True, m, d, y)
	except:
		return (False, '0','0','0')