import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    """
    Return true if valid otherwise false
    Visa:
        Prefix(es): 4
        Length: 16
    MasterCard:
        Prefix(es): 51 through 55 and 2221 through 2720 
        Length: 16
    American Express:
        Prefix(es): 34 and 37
        Length: 15
    """


    def test1(self):
        # Empty
        self.assertFalse(credit_card_validator(""))

    
    def test2(self):
        # Length 14
        self.assertFalse(credit_card_validator("34345678901234"))

    
    def test3(self):
        # Doesn't pass algorithm
        self.assertFalse(credit_card_validator("5234567890123456"))

    
    def test4(self):
        # Start with 3 instead of 4
        self.assertFalse(credit_card_validator("3123457890123456"))

    
    def test5(self):
        # 2721 not 2720
        self.assertFalse(credit_card_validator("2721567890123456"))

    
    def test6(self):
        # Length 15
        self.assertFalse(credit_card_validator("222140534324887"))

    
    def test820(self):
        # Just the prefix
        self.assertFalse(credit_card_validator("34"))

    
    def test899(self):
        # Just the prefix
        self.assertFalse(credit_card_validator("37"))

    
    def test111(self):
        # Doesn't pass Luhn algorithm
        self.assertFalse(credit_card_validator("341111111111111"))

    
    def test121(self):
        # Length 20
        self.assertFalse(credit_card_validator("34345678901234567890"))

    
    def test1121(self):
        # Length 10
        self.assertFalse(credit_card_validator("3434567890"))

    
    def test1321(self):
        # Invalid credit card number
        self.assertFalse(credit_card_validator("12345678901234"))

    
if __name__ == '__main__':
    unittest.main()
