#!/usr/bin/python
import string, sys, re

class ESDParser:
    def parse(self):
        exploded = self.getEsdName().split('.')
        self.checkEsdPattern()

        # Set Build & Delta
        self.setBuild(int(exploded[0]));
        self.setDelta(int(exploded[1]));

        # Set Major & Minor
        self.setMajor();
        self.setMinor();
    
    def setEsdName(self, esdName):
        self.esdName = esdName

    def checkEsdPattern(self):
        pattern = re.compile("[0-9]{6}-[0-9]{4}")

        # Check the pattern of the esd
        if pattern.match(self.getEsdName().split('.')[3][:11]):
            # Matched with build.delta.branch.dateTime (8.x)
            self.setBranch(self.getEsdName().split('.')[2])
            self.setDateTime(self.getEsdName().split('.')[3][:11])
        else:
            # Matched with build.delta.dateTime.branch.* (Threshold Development)
            self.setBranch(self.getEsdName().split('.')[3][:self.getEsdName().split('.')[3].find('CLIENT')-1])
            self.setDateTime(self.getEsdName().split('.')[2])

    def setMajor(self):
        self.major = 6;

    def setMinor(self):
        if self.build > 9200 and self.build <= 9600:
            self.minor = 3;
        else:
            self.minor = 4;

    def setBuild(self, build):
        self.build = build

    def setDelta(self, delta):
        self.delta = delta

    def setBranch(self, branch):
        self.branch = branch

    def setDateTime(self, dateTime):
        self.dateTime = dateTime

    def getEsdName(self):
        return self.esdName

    def getMajor(self):
        return self.major

    def getMinor(self):
        return self.minor

    def getBuild(self):
        return self.build

    def getDelta(self):
        return self.delta

    def getBranch(self):
        return self.branch

    def getDateTime(self):
        return self.dateTime

    # toBuildString
    # Return as a valid buildstring
    def toBuildString(self):
        return '%d.%d.%d.%d.%s.%s' % (self.getMajor(), self.getMinor(), self.getBuild(), self.getDelta(), self.getBranch(), self.getDateTime())

if __name__ == "__main__":
   esd = ESDParser()
   esd.setEsdName(sys.argv[1])
   esd.parse()
   print esd.toBuildString()