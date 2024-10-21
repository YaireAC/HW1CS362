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
        self.assertTrue(credit_card_validator(""))

    def test2(self):
        #length 14
        self.assertTrue(credit_card_validator("34345678901234"))

    def test3(self):
        self.assertTrue(credit_card_validator("423456789012345"))
   


if __name__ == '__main__':
    unittest.main()
