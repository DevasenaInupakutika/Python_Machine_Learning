import unittest
import datetime

#class FooTests(unittest.TestCase):

#    def testFoo(self):
#        self.failUnless(False)

class DatePattern:

    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def matches(self, date):
        return ((self.year and self.year == date.year or True) and
  		(self.month and self.month == date.month or True) and
  		self.day == date.day)

    def testMatchesYearAsWildCard(self):
        p = DatePattern(0,4,10)
  	d = datetime.date(2005,4,10)
        self.failUnless(p.matches(d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
