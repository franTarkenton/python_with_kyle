
import datetime
class gribFile:

    def __init__(self, name):
        self.gribName = name
        print(self.gribName)

    def addDateToName(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%y')
        self.gribName = self.gribName + now_str
        return self.gribName



myGrib = gribFile(name='mygrib')
myGribName = myGrib.addDateToName()
print(myGrib.gribName)