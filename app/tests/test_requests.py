from app import app
import unittest

class TestHelloWorld(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_reponse_normal_get(self):
        response = self.app.get('/',)
        """ we are getting 200 """
        """ check response header """
        assertEqual(result.status_code, 200)
        """ check response content """
        assertEqual(
                    response.content, 
                    '<p>Morning, world</p>'
                    )
        """ check log file """
        pass

    def test_reponse_json_get(self):
        response = self.app.get('/',)
        """ we are getting 200 """
        assertEqual(result.status_code, 200)
        """ check json content """
        assertEqual(
                    response.content, 
                    '{"message": "Good morning"}'
                    )
        """ check log file """
        pass

    def test_reponse_error_get(self):
        response = self.app.get('/error',)
        """ we are getting 404 """
        assertEqual(result.status_code, 404)
        """ check log file """
        pass

 
 if __name == '__main__':
    unittest.main()
