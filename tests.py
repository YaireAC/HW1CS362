import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    
    def test1(self):
        """Empty"""
        self.assertFalse(credit_card_validator(""))
        
    def test2(self):
        """length 14"""
        self.assertFalse(credit_card_validator("34345678901234"))

    def test3(self):
        """Doesnt pass algot"""
        self.assertFalse(credit_card_validator("5234567890123456"))

    def test4(self):
        """3 instead 4"""
        self.assertFalse(credit_card_validator("3123457890123456"))

    def test5(self):
        """2721 not 2720"""
        self.assertFalse(credit_card_validator("2721567890123456"))

    def test6(self):
        """length 15"""
        self.assertFalse(credit_card_validator("222140534324887"))

    def test820(self):
       """Just prefix"""
        self.assertFalse(credit_card_validator("34"))

    def test899(self):
        """prefix"""
        self.assertFalse(credit_card_validator("37"))
    
    def test111(self):
        """doesnt pas algorithm"""
        self.assertFalse(credit_card_validator("341111111111111"))
    
    def test121(self):
        """length 20"""
        self.assertFalse(credit_card_validator("34345678901234567890"))

    def test1121(self):
        """length 10"""
        self.assertFalse(credit_card_validator("3434567890"))

    def test1321(self):
        """invalid"""
        self.assertFalse(credit_card_validator("12345678901234"))

    
if __name__ == '__main__':
    unittest.main()
