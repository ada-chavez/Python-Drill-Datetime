## Version: Python 2.7
##
## Date: 03/16/17
##
## Author: Ada Chavez http://adachavez.com
##
## Purpose: (Drill given by The Tech Academy) A program to determine the local times in New York City and London
## using Portland as the base time. Also to determine if those locations are open or closed.


from datetime import datetime,timedelta

def start():
    # Calculate current time assuming user is in Portland already
    portlandTime = datetime.now()

    # Convert Portland time to New York City time and London time
    newyorkTime = datetime.now() + timedelta(hours=3)
    londonTime = datetime.now() + timedelta(hours=7)

    # Hours of operation
    openTime = portlandTime.replace(hour=9, minute=0)
    closeTime = portlandTime.replace(hour=21,minute=0)

    # Compare Portland time to hours of operation
    print 'The time in Portland is {:%H:%M}'.format(portlandTime)
    if openTime < portlandTime and closeTime > portlandTime:
        print 'The office in Portland is OPEN\n'
    else:
        print 'The office in Portland is CLOSED\n'

    # Compare New York City time to hours of operation
    print 'The time in New York City is {:%H:%M}'.format(newyorkTime)

    if openTime < newyorkTime and closeTime > newyorkTime:
        print 'The office in New York City is OPEN\n'
    else:
        print 'The office in New York City is CLOSED\n'
    
    # Compare London time to hours of operation
    print 'The time in London is {:%H:%M}'.format(londonTime)

    if openTime < londonTime and closeTime > londonTime:
        print 'The office in London is OPEN'
    else:
        print 'The office in London is CLOSED'




if __name__ == '__main__':
    start()

