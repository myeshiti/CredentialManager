import unittest
from usernamemanager import UserCredentialsManager, CredentialsChecker, CredentialsGenerator

class TestUserCredentialsManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserCredentialsManager()
        self.generator = CredentialsGenerator()
        self.checker = CredentialsChecker()

    def test_save_credentials(self):
        result = self.manager.save_credentials("TestUser1", "Password123!")
        self.assertEqual(result["ID"], 1)
        self.assertEqual(result["Username"], "TestUser1")
        self.assertEqual(result["Password"], "Password123!")

    def test_check_password_valid(self):
        self.assertTrue(self.manager.check_password("LongEnough1!"))

    def test_check_password_invalid(self):
        self.assertFalse(self.manager.check_password("short"))

    def test_generate_password_length(self):
        password = self.manager.generate_password()
        self.assertEqual(len(password), 12)

    def test_generate_username_types(self):
        for t in ["short", "medium", "long"]:
            username = self.generator.generate_username(t)
            self.assertIsInstance(username, str)
            self.assertTrue(8 <= len(username) <= 20)

    def test_check_credentials_valid(self):
        username = "JohnDoe1!"
        password = "ValidPass123"
        valid, errors = self.checker.check_credentials(username, password, "John")
        self.assertTrue(valid)
        self.assertEqual(len(errors), 0)

    def test_check_credentials_invalid(self):
        username = "bad"
        password = "short"
        valid, errors = self.checker.check_credentials(username, password, "Missing")
        self.assertFalse(valid)
        self.assertGreater(len(errors), 0)

if __name__ == '__main__':
    unittest.main()
