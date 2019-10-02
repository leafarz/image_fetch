import unittest
from util import helper

class TestDates(unittest.TestCase):
	# original test case
	def test_data(self):
		self.assertEqual(helper.parse_date('02/27/17')			,(True, '02', '27', '2017'), "Date not equal!")
		self.assertEqual(helper.parse_date('June 2, 2018')		,(True, '06', '02', '2018'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jul-13-2016')		,(True, '07', '13', '2016'), "Date not equal!")
		self.assertEqual(helper.parse_date('April 31, 2018')	,(False, '0', '0', '0'), "Date should be invalid!")

	def test_invalid_dates(self):
		self.assertEqual(helper.parse_date('0/1/01')			,(False, '0', '0', '0'), "Date should be invalid!")
		self.assertEqual(helper.parse_date('1-0-01')			,(False, '0', '0', '0'), "Date should be invalid!")
		self.assertEqual(helper.parse_date('1-50/01')			,(False, '0', '0', '0'), "Date should be invalid!")
		self.assertEqual(helper.parse_date('13/1-01')			,(False, '0', '0', '0'), "Date should be invalid!")

	# test per months
	def test_months(self):
		self.assertEqual(helper.parse_date('01/01/01') 			,(True, '01', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('01-01-01') 			,(True, '01', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('January 1, 2001')	,(True, '01', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('January 01, 2001')	,(True, '01', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jan-1, 01')			,(True, '01', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jan-1, 19')			,(True, '01', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jan-1, 20')			,(True, '01', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('02/01/01') 			,(True, '02', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('02-01-01') 			,(True, '02', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('February 1, 2001')	,(True, '02', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('February 01, 2001')	,(True, '02', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Feb-1, 01')			,(True, '02', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Feb-1, 19')			,(True, '02', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Feb-1, 20')			,(True, '02', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('03/01/01') 			,(True, '03', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('03-01-01') 			,(True, '03', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('March 1, 2001')		,(True, '03', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('March 01, 2001')	,(True, '03', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Mar-1, 01')			,(True, '03', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Mar-1, 19')			,(True, '03', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Mar-1, 20')			,(True, '03', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('04/01/01') 			,(True, '04', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('04-01-01') 			,(True, '04', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('April 1, 2001')		,(True, '04', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('April 01, 2001')	,(True, '04', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Apr-1, 01')			,(True, '04', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Apr-1, 19')			,(True, '04', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Apr-1, 20')			,(True, '04', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('05/01/01') 			,(True, '05', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('05-01-01') 			,(True, '05', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('May 1, 2001')		,(True, '05', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('May 01, 2001')		,(True, '05', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('May-1, 01')			,(True, '05', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('May-1, 19')			,(True, '05', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('May-1, 20')			,(True, '05', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('06/01/01') 			,(True, '06', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('06-01-01') 			,(True, '06', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('June 1, 2001')		,(True, '06', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('June 01, 2001')		,(True, '06', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jun-1, 01')			,(True, '06', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jun-1, 19')			,(True, '06', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jun-1, 20')			,(True, '06', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('07/01/01') 			,(True, '07', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('07-01-01') 			,(True, '07', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('July 1, 2001')		,(True, '07', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('July 01, 2001')		,(True, '07', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jul-1, 01')			,(True, '07', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jul-1, 19')			,(True, '07', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Jul-1, 20')			,(True, '07', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('08/01/01') 			,(True, '08', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('08-01-01') 			,(True, '08', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('August 1, 2001')	,(True, '08', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('August 01, 2001')	,(True, '08', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Aug-1, 01')			,(True, '08', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Aug-1, 19')			,(True, '08', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Aug-1, 20')			,(True, '08', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('09/01/01') 			,(True, '09', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('09-01-01') 			,(True, '09', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('September 1, 2001')	,(True, '09', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('September 01, 2001'),(True, '09', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Sept-1, 01')		,(True, '09', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Sept-1, 19')		,(True, '09', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Sept-1, 20')		,(True, '09', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('10/01/01') 			,(True, '10', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('10-01-01') 			,(True, '10', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('October 1, 2001')	,(True, '10', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('October 01, 2001')	,(True, '10', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Oct-1, 01')			,(True, '10', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Oct-1, 19')			,(True, '10', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Oct-1, 20')			,(True, '10', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('11/01/01') 			,(True, '11', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('11-01-01') 			,(True, '11', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('November 1, 2001')	,(True, '11', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('November 01, 2001')	,(True, '11', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Nov-1, 01')			,(True, '11', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Nov-1, 19')			,(True, '11', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Nov-1, 20')			,(True, '11', '01', '1920'), "Date not equal!")

		self.assertEqual(helper.parse_date('12/01/01') 			,(True, '12', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('12-01-01') 			,(True, '12', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('December 1, 2001')	,(True, '12', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('December 01, 2001')	,(True, '12', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Dec-1, 01')			,(True, '12', '01', '2001'), "Date not equal!")
		self.assertEqual(helper.parse_date('Dec-1, 19')			,(True, '12', '01', '2019'), "Date not equal!")
		self.assertEqual(helper.parse_date('Dec-1, 20')			,(True, '12', '01', '1920'), "Date not equal!")

if __name__ == '__main__':
	unittest.main()