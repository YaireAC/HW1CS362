import unittest
from credit_card_validator import credit_card_validator

class Testcredit_card_validator(unittest.TestCase):
    # Example
    # def test11(self):
    # """Verifies if Master Cards with valid lengths and invalid check bits returns False
    # Picked using Category Partition Testing"""
    # self.assertFalse(credit_card_validator("...."))
    
    def test1(self):
        self.assertTrue(credit_card_validator("4123456789012345"))


if __name__ == '__main__':
    unittest.main()
