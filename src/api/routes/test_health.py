import json
import unittest
from utils.factory import create_app
from utils.config import DevelopmentConfig

class BaseTestCase(unittest.TestCase):
    """A base test case"""
    def setUp(self):
        app = create_app(DevelopmentConfig)
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        print "teardown complete"

class TestHealthEndpoint(BaseTestCase):
    """Test Health Endpoint"""
    def setUp(self):
        super(TestHealthEndpoint, self).setUp()

    def test_returns_status_ok(self):
        """Should return status OK and HTTP 200 when hitting health endpoint"""
        response = self.app.get('/health')
        r = json.dumps(response.data)

        self.assertEqual(200, response.status_code)
        self.assertTrue('"status":"OK"', r)