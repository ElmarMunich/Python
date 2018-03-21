# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.


def leapyear(year,month,day):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False


def endOfMonth(year,month,day):
    ''' Calculates the number of dys for a certain month'''
    if month == 4 or month == 6 or month == 9 or month == 11:
        eom = 30
        return eom
    elif month == 2:
        if leapyear(year,month,day) == True:
            eom = 29
        else:
            eom = 28
        return eom
    else:
        eom = 31
        return eom

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < endOfMonth(year,month,day):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((1900,1,1,1901,1,1),365),
                  ((1900,1,1,1925,1,1),9131),
                  ((1900,1,1,1950,1,1),18262),
                  ((1900,1,1,1999,12,31),36523),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data: ", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)


test()
