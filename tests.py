import random
import unittest

from esd import ESDParser

class TestESDParserFunctions(unittest.TestCase):

    def test_WinBlueParse(self):
        esd = ESDParser()
        esd.setEsdName('9600.17053.winblue_refresh.140923-1144_x86fre_client_professional_en-us-ir4_cpra_x86frer_en-us_esd.esd')
        esd.parse()
        
        self.assertEqual(esd.toBuildString(), '6.3.9600.17053 (winblue_refresh.140923-1144)')
        self.assertEqual(esd.getMajor(), 6)
        self.assertEqual(esd.getMinor(), 3)
        self.assertEqual(esd.getBuild(), 9600)
        self.assertEqual(esd.getDelta(), 17053)
        self.assertEqual(esd.getBranch(), 'winblue_refresh')
        self.assertEqual(esd.getDateTime(), '140923-1144')
        self.assertEqual(esd.getLicense(), 'r')
        self.assertEqual(esd.getArchitecture(), 'x86')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'professional')
        self.assertEqual(esd.getLanguage(), 'en-us')

    def test_WinThresholdParse(self):
        esd = ESDParser()
        esd.setEsdName('9836.0.140906-2314.fbl_release_CLIENTENTERPRISE_VOL_x64fre_en-us.esd')
        esd.parse()

        self.assertEqual(esd.toBuildString(), '6.4.9836.0 (fbl_release.140906-2314)')
        self.assertEqual(esd.getMajor(), 6)
        self.assertEqual(esd.getMinor(), 4)
        self.assertEqual(esd.getBuild(), 9836)
        self.assertEqual(esd.getDelta(), 0)
        self.assertEqual(esd.getBranch(), 'fbl_release')
        self.assertEqual(esd.getDateTime(), '140906-2314')
        self.assertEqual(esd.getLicense(), 'VOL')
        self.assertEqual(esd.getArchitecture(), 'x64')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'CLIENTENTERPRISE')
        self.assertEqual(esd.getLanguage(), 'en-us')

    def test_Win10Parse(self):
        esd = ESDParser()
        esd.setEsdName('9888.0.141113-2137.fbl_release_CLIENTPRO_RET_x64fre_en-us.esd')
        esd.parse()
        
        self.assertEqual(esd.toBuildString(), '10.0.9888.0 (fbl_release.141113-2137)')
        self.assertEqual(esd.getMajor(), 10)
        self.assertEqual(esd.getMinor(), 0)
        self.assertEqual(esd.getBuild(), 9888)
        self.assertEqual(esd.getDelta(), 0)
        self.assertEqual(esd.getBranch(), 'fbl_release')
        self.assertEqual(esd.getDateTime(), '141113-2137')
        self.assertEqual(esd.getLicense(), 'RET')
        self.assertEqual(esd.getArchitecture(), 'x64')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'CLIENTPRO')
        self.assertEqual(esd.getLanguage(), 'en-us')

    def test_WinBlueSet(self):
        esd = ESDParser()

        esd.setMajor(6)
        esd.setMinor(3)
        esd.setBuild(9600)
        esd.setDelta(17053)
        esd.setBranch('winblue_refresh')
        esd.setDateTime('140923-1144')
        esd.setLicense('r')
        esd.setArchitecture('x86')
        esd.setCompileState('fre')
        esd.setSku('professional')
        esd.setLanguage('en-us')
        
        self.assertEqual(esd.toBuildString(), '6.3.9600.17053 (winblue_refresh.140923-1144)')
        self.assertEqual(esd.getMajor(), 6)
        self.assertEqual(esd.getMinor(), 3)
        self.assertEqual(esd.getBuild(), 9600)
        self.assertEqual(esd.getDelta(), 17053)
        self.assertEqual(esd.getBranch(), 'winblue_refresh')
        self.assertEqual(esd.getDateTime(), '140923-1144')
        self.assertEqual(esd.getLicense(), 'r')
        self.assertEqual(esd.getArchitecture(), 'x86')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'professional')
        self.assertEqual(esd.getLanguage(), 'en-us')

    def test_WinThresholdSet(self):
        esd = ESDParser()

        esd.setMajor(6)
        esd.setMinor(4)
        esd.setBuild(9836)
        esd.setDelta(0)
        esd.setBranch('fbl_release')
        esd.setDateTime('140906-2314')
        esd.setLicense('VOL')
        esd.setArchitecture('x64')
        esd.setCompileState('fre')
        esd.setSku('CLIENTENTERPRISE')
        esd.setLanguage('en-us')

        self.assertEqual(esd.toBuildString(), '6.4.9836.0 (fbl_release.140906-2314)')
        self.assertEqual(esd.getMajor(), 6)
        self.assertEqual(esd.getMinor(), 4)
        self.assertEqual(esd.getBuild(), 9836)
        self.assertEqual(esd.getDelta(), 0)
        self.assertEqual(esd.getBranch(), 'fbl_release')
        self.assertEqual(esd.getDateTime(), '140906-2314')
        self.assertEqual(esd.getLicense(), 'VOL')
        self.assertEqual(esd.getArchitecture(), 'x64')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'CLIENTENTERPRISE')
        self.assertEqual(esd.getLanguage(), 'en-us')

    def test_Win10Set(self):
        esd = ESDParser()
        esd.setEsdName('9888.0.141113-2137.fbl_release_CLIENTPRO_RET_x64fre_en-us.esd')
        
        esd.setMajor(10)
        esd.setMinor(0)
        esd.setBuild(9888)
        esd.setDelta(0)
        esd.setBranch('fbl_release')
        esd.setDateTime('141113-2137')
        esd.setLicense('RET')
        esd.setArchitecture('x64')
        esd.setCompileState('fre')
        esd.setSku('CLIENTPRO')
        esd.setLanguage('en-us')
        
        self.assertEqual(esd.toBuildString(), '10.0.9888.0 (fbl_release.141113-2137)')
        self.assertEqual(esd.getMajor(), 10)
        self.assertEqual(esd.getMinor(), 0)
        self.assertEqual(esd.getBuild(), 9888)
        self.assertEqual(esd.getDelta(), 0)
        self.assertEqual(esd.getBranch(), 'fbl_release')
        self.assertEqual(esd.getDateTime(), '141113-2137')
        self.assertEqual(esd.getLicense(), 'RET')
        self.assertEqual(esd.getArchitecture(), 'x64')
        self.assertEqual(esd.getCompileState(), 'fre')
        self.assertEqual(esd.getSku(), 'CLIENTPRO')
        self.assertEqual(esd.getLanguage(), 'en-us')

if __name__ == '__main__':
    unittest.main()