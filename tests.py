import unittest
from credit_card_validator import credit_card_validator

class Testcredit_card_validator(unittest.TestCase):

#Return true if valid otherwise false
#       Visa
# Prefix(es): 4
# Length: 16
#       MasterCard
# Prefix(es): 51 through 55 and 2221 through 2720 
# Length: 16
#       American Express
# Prefix(es): 34 and 37
# Length: 15


    # Example
    # def test11(self):
    # """Verifies if Master Cards with valid lengths and invalid check bits returns False
    # Picked using Category Partition Testing"""
    # self.assertFalse(credit_card_validator("...."))
    
    def test1(self):
        #Empty
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        #length 14
        self.assertFalse(credit_card_validator("34345678901234"))

    def test3(self):
        #wrong prefix, 52 instead of 51
        self.assertFalse(credit_card_validator("5234567890123456"))

    def test4(self):
        #start with 3 instead of 4
        self.assertFalse(credit_card_validator("3123457890123456"))

    def test5(self):
        #2721 not 2720
        self.assertFalse(credit_card_validator("2721567890123456"))

    def test6(self):
        #
        self.assertFalse(credit_card_validator("5555555555555555"))
   


if __name__ == '__main__':
    unittest.main()
