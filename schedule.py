
class Schedule:
    schedule_page = 'http://www.espn.com/college-football/team/schedule/_/id/130'
    def __init__(self):
        page = urllib2.urlopen(schedule_page)
        soup = BeautifulSoup(page, 'html.parser')
        games = []
        generateSchedule()

    # TODO
    def isGameInProgress(self):
        return false

    def nextGame(self):
        return

    def generateSchedule(self):



class Game:
    def __init__(self, date, time, opponent, status):
        stringDate = date
        stringTime = time
        self.opponent = opponent
        self.status = status
