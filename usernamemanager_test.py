import unittest

def test_check_password(self):
        valid_password = "valid_password123"
        invalid_password = "short"

        self.assertTrue(self.manager.check_password(valid_password))
        self.assertFalse(self.manager.check_password(invalid_password))
        
if __name__ == '__main__':
    unittest.main()
