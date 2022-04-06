import unittest
from app import app

class BasicTests(unittest.TestCase):
    def test_main_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_page2(self):
        tester = app.test_client(self)
        response = tester.get('/health')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
