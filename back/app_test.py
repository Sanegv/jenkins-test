import unittest
from unittest.mock import patch, MagicMock
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode('utf-8'), 'API is running!')

    @patch('app.get_db_connection')
    def test_get_data(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [(1, 'salut')]

        response = self.client.get('/data')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [[1, 'salut']])

        mock_cursor.execute.assert_called_with('SELECT * FROM items')

    def test_echo(self):
        response = self.client.get('/echo?=salut+le+monde')
        self.assertEqual(response.data.decode('utf-8'), 'salut le monde')

if __name__ == '__main__':
    unittest.main()
