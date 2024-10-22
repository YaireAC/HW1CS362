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

    def test14(self):
        """invalid"""
        self.assertFalse(credit_card_validator("111111111111111111111111111111"))

    def test134(self):
        """invalid"""
        self.assertFalse(credit_card_validator("123"))

    def test14(self):
        """invalid"""
        self.assertFalse(credit_card_validator("2720567890123454"))
        
    def test_valid_american_express(self):
        # Valid Amex: 15 digits, starts with 34
        self.assertTrue(credit_card_validator("341111111111111"))
        # Valid Amex: 15 digits, starts with 37
        self.assertTrue(credit_card_validator("371111111111111"))

    # Test for invalid American Express number (wrong length)
    def test_invalid_american_express_length(self):
        # Invalid Amex: 16 digits
        self.assertFalse(credit_card_validator("3411111111111111"))
    
    # Test for invalid American Express number (wrong prefix)
    def test_invalid_american_express_prefix(self):
        # Invalid Amex: 15 digits, wrong prefix
        self.assertFalse(credit_card_validator("321111111111111"))

    # Test for invalid card number (does not match any issuer)
    def test_invalid_card_unknown_issuer(self):
        # Invalid: unknown issuer
        self.assertFalse(credit_card_validator("6011111111111117"))

    # Test for invalid card number (invalid Luhn checksum)
    def test_invalid_luhn_checksum(self):
        # Invalid: Luhn checksum fails
        self.assertFalse(credit_card_validator("411111111111112"))
    def test_bug8_amex_invalid_checksum(self):
    # Invalid Amex: Luhn checksum fails, but length and prefix are valid
        self.assertFalse(credit_card_validator("341111111111118"))

    def test_bug8_mastercard_invalid_prefix(self):
    # Invalid MasterCard: 16 digits, prefix just outside valid range
        self.assertFalse(credit_card_validator("2721567890123456"))

    def test_bug8_visa_invalid_length(self):
    # Invalid Visa: 17 digits instead of 16
        self.assertFalse(credit_card_validator("41111111111111112"))

    def test_bug8_mastercard_upper_bound(self):
    # Valid MasterCard: 16 digits, highest valid prefix
        self.assertTrue(credit_card_validator("2720567890123456"))







    


if __name__ == '__main__':
    unittest.main()
