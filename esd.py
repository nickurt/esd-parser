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
        self.setMajor(6 if self.getBuild() in range(9200, 9888) else 10);
        self.setMinor(3 if self.getBuild() in range(9200, 9600) else 4 if self.getBuild() in range(9600, 9888) else 0);
    
    def setEsdName(self, esdName):
        self.esdName = esdName
        return self

    def checkEsdPattern(self):
        pattern = re.compile("[0-9]{6}-[0-9]{4}")

        # Check the pattern of the esd
        if pattern.match(self.getEsdName().split('.')[3][:11]):
            # Matched with build.delta.branch.dateTime (8.x)
            self.setBranch(self.getEsdName().split('.')[2])
            self.setDateTime(self.getEsdName().split('.')[3][:11])

            # Sku, License, Arch, Language
            skuLicenseArchLang = self.getEsdName().split('.')[3].split('_')
            self.setSku(skuLicenseArchLang[3]).setLicense(skuLicenseArchLang[6][6]).setArchitecture(skuLicenseArchLang[1][:3]).setCompileState(skuLicenseArchLang[1][3:]).setLanguage(skuLicenseArchLang[4][:5])
        else:
            # Matched with build.delta.dateTime.branch.* (Threshold Development)
            self.setBranch(self.getEsdName().split('.')[3][:self.getEsdName().split('.')[3].find('CLIENT')-1])
            self.setDateTime(self.getEsdName().split('.')[2])

            # Sku, License, Arch, Language
            skuLicenseArchLang = self.getEsdName().split('.')[3][self.getEsdName().split('.')[3].find('CLIENT'):].split('_')
            self.setSku(skuLicenseArchLang[0]).setLicense(skuLicenseArchLang[1]).setArchitecture(skuLicenseArchLang[2][:3]).setCompileState(skuLicenseArchLang[2][3:]).setLanguage(skuLicenseArchLang[3])

    def setMajor(self, major):
        self.major = int(major)
        return self

    def setMinor(self, minor):
        self.minor = int(minor)
        return self

    def setBuild(self, build):
        self.build = int(build)
        return self

    def setDelta(self, delta):
        self.delta = int(delta)
        return self

    def setBranch(self, branch):
        self.branch = branch
        return self

    def setDateTime(self, dateTime):
        self.dateTime = dateTime
        return self

    def setSku(self, sku):
        self.sku = sku
        return self

    def setLicense(self, license):
        self.license = license
        return self

    def setCompileState(self, compileState):
        self.compileState = compileState
        return self

    def setArchitecture(self, architecture):
        self.architecture = architecture
        return self

    def setLanguage(self, language):
        self.language = language
        return self

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

    # toESD
    # Return as a valid ESD
    def toESD(self):
        # 9888.0.141115-2224.fbl_mobs_dev02_CLIENTENTERPRISE_VOL_x86fre_en-us.esd
        esd = '%d.%d.%s.%s_%s_%s_%s%s_%s.esd' % (self.getBuild(), self.getDelta(), self.getDateTime(), self.getBranch(), self.getSku(), self.getLicense(), self.getArchitecture(), self.getCompileState(), self.getLanguage())
       
        #   9778.0.fbl_marketplace.140619-1430_x64fre_client_EnterpriseVL_en-us-IR3_CENA_X64FREV_EN-US_ESD.esd
        #   esd = '%d.%d.%s.%s_%s%s_%s_%s_%s%s%s_%s_ESD.esd' % (self.getBuild(), self.getDelta(), self.getBranch(), self.getDateTime(), self.getArchitecture(), self.getCompileState(), self.getSku(), self.getLanguage(), self.getArchitecture(), self.getCompileState(), self.getLicense(), self.getLanguage())

        return esd

    # toBuildString
    # Return as a valid buildstring
    def toBuildString(self):
        return '%d.%d.%d.%d.%s.%s' % (self.getMajor(), self.getMinor(), self.getBuild(), self.getDelta(), self.getBranch(), self.getDateTime())