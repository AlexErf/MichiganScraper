
class Schedule:
    schedule_page = 'http://www.espn.com/college-football/team/schedule/_/id/130'
    def __init__(self):
        page = urllib2.urlopen(schedule_page)
        soup = BeautifulSoup(page, 'html.parser')
        games = []

    # TODO
    def isGameInProgress(self):
        return false

    def nextGame(self):
        return


class Game:
    def __init__(self, date, time, opponent, status):
        self.date = date
        self.time = time
        self.opponent = opponent
        self.status = status
