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

    # Index page test

    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'index', response.data)

    # The login is successful for an agent

    def test_admin_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_agent', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'login_agent', response.data)

    #  The login is not successful for incorrect credentials
    def test_hospital_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_hospital', data=dict(username="wrong1", password="wrong"), follow_redirects=True)
        self.assertIn(b'login_hospital', response.data)

    #  The login is successful for a hospital
    def test_hospital_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_hospital', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'login_hospital', response.data)

    def test_admin(self):
        tester = app.test_client(self)
        response = tester.get('/login_agent', content_type="html/text")
        self.assertIn(b'login_agent', response.data)

    def test_hospital(self):
        tester = app.test_client(self)
        response = tester.get('/in_hospital', content_type="html/text")
        self.assertIn(b'in_hospital', response.data)

    def test_visitor_reg(self):
        tester = app.test_client(self)
        response = tester.get('/register_visitor',
                              content_type="html/text")
        self.assertIn(b'register_visitor', response.data)

    def test_place_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_place', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'login_place', response.data)

    def test_visitor_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_visitor', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'login_visitor', response.data)

    def test_scan_qr(self):
        tester = app.test_client(self)
        response = tester.get('/scan', content_type="html/text")
        self.assertIn(b'in_visitor', response.data)

    def test_qr(self):
        tester = app.test_client(self)
        response = tester.get('/qrcode', content_type="html/text")
        self.assertIn(b'in_place', response.data)

    def test_check_in(self):
        tester = app.test_client(self)
        response = tester.get('/check_in', content_type="html/text")
        self.assertIn(b'checkin', response.data)

    def test_visitor(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_visitor', data=dict(username="jac", password="jac"), follow_redirects=True)
        self.assertIn(b'login_visitor', response.data)

    def test_visitor_worng(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_visitor', data=dict(username="jacsd", password="jacsdf"), follow_redirects=True)
        self.assertIn(b'login_visitor', response.data)


if __name__ == '__main__':
    unittest.main()
