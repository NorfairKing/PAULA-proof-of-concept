try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time

class CalendarExample:
    
  def __init__(self, email, password):
    """Creates a CalendarService and provides ClientLogin auth details to it.
    The email and password are required arguments for ClientLogin.  The
    CalendarService automatically sets the service to be 'cl', as is
    appropriate for calendar.  The 'source' defined below is an arbitrary
    string, but should be used to reference your name or the name of your
    organization, the app name and version, with '-' between each of the three
    values.  The account_type is specified to authenticate either
    Google Accounts or Google Apps accounts.  See gdata.service or
    http://code.google.com/apis/accounts/AuthForInstalledApps.html for more
    info on ClientLogin.  NOTE: ClientLogin should only be used for installed
    applications and not for multi-user web applications."""
    
    self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
    self.cal_client.ClientLogin(email, password, self.cal_client.source);
 
  def _PrintUserCalendars(self):
    """Retrieves the list of calendars to which the authenticated user either
    owns or subscribes to.  This is the same list as is represented in the
    Google Calendar GUI.  Although we are only printing the title of the
    calendar in this case, other information, including the color of the
    calendar, the timezone, and more.  See CalendarListEntry for more details
    on available attributes."""

    feed = self.cal_client.GetAllCalendarsFeed()
    print 'Printing allcalendars: %s' % feed.title.text
    for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, a_calendar.title.text,) 
      print i.__class__.__name__
      print a_calendar.__class__.__name__

  def Run(self):
    """Runs each of the example methods defined above.  Note how the result
    of the _InsertSingleEvent call is used for updating the title and the
    result of updating the title is used for inserting the reminder and
    again with the insertion of the extended property.  This is due to the
    Calendar's use of GData's optimistic concurrency versioning control system:
    http://code.google.com/apis/gdata/reference.html#Optimistic-concurrency
    """

    # Getting feeds and query results
    self._PrintUserCalendars()
    

def main():
    c = CalendarExample('syd.kerckhove@gmail.com','pandemic')
    c.Run()

if __name__ == '__main__':
    main()
