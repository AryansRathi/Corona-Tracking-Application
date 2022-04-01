from turtle import clear
from app import app
import unittest
import os
import sys
import string
import random
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# import tempfile


class FlaskTestCase(unittest.TestCase):
    # Please note that this test cases depend on your computer as well as well. For example if I already have
    # a instructor named admin in my database that might not be true for you so KEEP THIS IN MIND.

    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'index', response.data)

    # # The login is successful for an agent

    def test_admin_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/agent_log', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'agent_log', response.data)

    # # # # The login is not successful for incorrect credentials
    def test_hospital_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/hospital_log', data=dict(username="wrong1", password="wrong"), follow_redirects=True)
        self.assertIn(b'hospital_log', response.data)

    # # # # The login is successful for a hospital
    def test_hospital_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/hospital_log', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'hospital_log', response.data)

    def test_admin(self):
        tester = app.test_client(self)
        response = tester.get('/agent_log', content_type="html/text")
        self.assertIn(b'agent_log', response.data)

    def test_hospital(self):
        tester = app.test_client(self)
        response = tester.get('/hospital_page', content_type="html/text")
        self.assertIn(b'hospital_page', response.data)

    def test_visitor_reg(self):
        tester = app.test_client(self)
        response = tester.get('/visitor_registration',
                              content_type="html/text")
        self.assertIn(b'visitor_registration', response.data)

    def test_place_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/place_log', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'place_log', response.data)

    def test_visitor_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/visitor_log', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'visitor_log', response.data)

    def test_scan_qr(self):
        tester = app.test_client(self)
        response = tester.get('/scan_qr', content_type="html/text")
        self.assertIn(b'scan_qr', response.data)

    def test_qr(self):
        tester = app.test_client(self)
        response = tester.get('/qr', content_type="html/text")
        self.assertIn(b'qr', response.data)


if __name__ == '__main__':
    unittest.main()
