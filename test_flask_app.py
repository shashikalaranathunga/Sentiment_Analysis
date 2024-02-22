import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_index_get(self):
        response = self.client.get('/?q=test')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        response = self.client.post('/', data={'q': 'This is a positive sentence.'})
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('sentiment', data)
        self.assertEqual(data['sentiment'], 'Positive')

    def test_missing_parameter(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 400)  # Corrected status code expectation
        data = response.json
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'No text provided.')  # Optionally check the error message

if __name__ == '__main__':
    unittest.main()
