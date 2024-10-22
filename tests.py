import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test1(self):
        """Verifies if an empty input returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """Verifies if an American Express of length 14 returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("34345678901234"))

    def test3(self):
        """Verifies if a MasterCard with invalid check bit returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("5234567890123456"))

    def test4(self):
        """Verifies if a Visa with an incorrect prefix returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("3123457890123456"))

    def test5(self):
        """Verifies if a MasterCard with an incorrect prefix returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("2721567890123456"))

    def test6(self):
        """Verifies if a MasterCard with a length of 15 returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("222140534324887"))

    def test7(self):
        """Verifies if an American Express with incorrect length & checksum returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("34"))

    def test8(self):
        """Verifies if an American Express with incorrect length & checksum returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("37"))

    def test9(self):
        """Verifies if an American Express with invalid check bit returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("341111111111111"))

    def test10(self):
        """Verifies if an American Express with incorrect length & checksum returns False
    Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("34345678901234567890"))

    def test11(self):
        """length 10"""
        self.assertFalse(credit_card_validator("3434567890"))

    def test12(self):
        """invalid"""
        self.assertFalse(credit_card_validator("12345678901234"))
        
    def test13(self):
        """length 10"""
        self.assertFalse(credit_card_validator("411111111111111"))
        
    def test13(self):
        """length 10"""
        self.assertFalse(credit_card_validator("511234567890123"))

    def test13(self):
        """length 10"""
        self.assertFalse(credit_card_validator("34123456789012"))




if __name__ == '__main__':
    unittest.main()
