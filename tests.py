import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test1(self):
        """Empty"""
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """length 14"""
        self.assertFalse(credit_card_validator("451525354553437"))

    def test3(self):
        """Doesnt pass algot"""
        self.assertFalse(credit_card_validator("340000000000000"))

    def test4(self):
        """3 instead 4"""
        self.assertFalse(credit_card_validator("3411111111111118"))

    def test5(self):
        """2721 not 2720      """
        self.assertFalse(credit_card_validator("56123456789012345"))

    def test6(self):
        """"""
        self.assertFalse(credit_card_validator("222040534324887"))

    def test820(self):
        """Just prefix"""
        self.assertFalse(credit_card_validator("371234567890123"))

    def test899(self):
        """prefix"""
        self.assertFalse(credit_card_validator("37"))

    def test111(self):
        """doesnt pas algorithm"""
        self.assertFalse(credit_card_validator("38345678901234"))

    def test121(self):
        """length 20"""
        self.assertFalse(credit_card_validator("342222222222333"))

    def test1121(self):
        """length 10"""
        self.assertFalse(credit_card_validator("343734373437343"))

    def test1321(self):
        """invalid"""
        self.assertFalse(credit_card_validator("5634567890123456"))

    def test13221(self):
        """invalid"""
        self.assertFalse(credit_card_validator("6212345678901234"))

    def test112(self):
        """invalid"""
        self.assertFalse(credit_card_validator("5712345678901238"))
        
    def test1124(self):
        """invalid"""
        self.assertFalse(credit_card_validator("37123456789012346"))
        
    def test112774(self):
        """invalid"""
        self.assertFalse(credit_card_validator("7812345678901230"))


if __name__ == '__main__':
    unittest.main()
