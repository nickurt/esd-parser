#!/usr/bin/python
import string, re

class ESDParser:
    def parse(self):
        exploded = self.getEsdName().split('.')
        self.checkEsdPattern()

        # Set Build & Delta
        self.setBuild(exploded[0]);
        self.setDelta(exploded[1]);

        # Set Major & Minor
        self.setMajor(6);
        self.setMinor(3 if self.build > 9200 and self.build <= 9600 else 4);
    
    def setEsdName(self, esdName):
        self.esdName = esdName

    def checkEsdPattern(self):
        pattern = re.compile("[0-9]{6}-[0-9]{4}")

        # Check the pattern of the esd
        if pattern.match(self.getEsdName().split('.')[3][:11]):
            # Matched with build.delta.branch.dateTime (8.x)
            self.setBranch(self.getEsdName().split('.')[2])
            self.setDateTime(self.getEsdName().split('.')[3][:11])

            # Sku, License, Arch, Language
            skuLicenseArchLang = self.getEsdName().split('.')[3].split('_')
            self.setSku(skuLicenseArchLang[3])
            self.setLicense(skuLicenseArchLang[6][6])
            self.setArchitecture(skuLicenseArchLang[1][:3])
            self.setCompileState(skuLicenseArchLang[1][3:])
            self.setLanguage(skuLicenseArchLang[4][:5])
        else:
            # Matched with build.delta.dateTime.branch.* (Threshold Development)
            self.setBranch(self.getEsdName().split('.')[3][:self.getEsdName().split('.')[3].find('CLIENT')-1])
            self.setDateTime(self.getEsdName().split('.')[2])

            # Sku, License, Arch, Language
            skuLicenseArchLang = self.getEsdName().split('.')[3][self.getEsdName().split('.')[3].find('CLIENT'):].split('_')
            self.setSku(skuLicenseArchLang[0])
            self.setLicense(skuLicenseArchLang[1])
            self.setArchitecture(skuLicenseArchLang[2][:3])
            self.setCompileState(skuLicenseArchLang[2][3:])
            self.setLanguage(skuLicenseArchLang[3])

    def setMajor(self, major):
        self.major = int(major);

    def setMinor(self, minor):
        self.minor = int(minor)

    def setBuild(self, build):
        self.build = int(build)

    def setDelta(self, delta):
        self.delta = int(delta)

    def setBranch(self, branch):
        self.branch = branch

    def setDateTime(self, dateTime):
        self.dateTime = dateTime

    def setSku(self, sku):
        self.sku = sku

    def setLicense(self, license):
        self.license = license

    def setCompileState(self, compileState):
        self.compileState = compileState

    def setArchitecture(self, architecture):
        self.architecture = architecture

    def setLanguage(self, language):
        self.language = language

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

    def getSku(self):
        return self.sku

    def getLicense(self):
        return self.license

    def getCompileState(self):
        return self.compileState

    def getArchitecture(self):
        return self.architecture

    def getLanguage(self):
        return self.language

    # toBuildString
    # Return as a valid buildstring
    def toBuildString(self):
        return '%d.%d.%d.%d.%s.%s' % (self.getMajor(), self.getMinor(), self.getBuild(), self.getDelta(), self.getBranch(), self.getDateTime())