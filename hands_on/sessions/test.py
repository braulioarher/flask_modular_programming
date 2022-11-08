import os
import pytest
import requests
from app import app
from bs4 import BeautifulSoup


class Test_API:
    client = app.test_client()

    def test_login(self):
        url = 'http://localhost:5000/login'
        payload = "{'username': 'admin', 'password': 'test'}"
        headers = {'Content-Type': 'text/html'}
        response = self.client.post(url, data=payload, headers=headers)
        assert response.status_code == 308

    def test_user(self):
        url = 'http://localhost:5000/user/'
        headers = {'Content-Type': 'text/html'}
        response = self.client.get(url, headers=headers)
        assert response.status_code == 200

    def test_logout(self):
        url = 'http://localhost:5000/logout/'
        headers = {'Content-Type': 'text/html'}
        response = self.client.get(url, headers=headers)
        assert response.status_code == 200


class Test_Webpage:
    def get_soup1(self):
        post_params = {'username': 'admin', 'password': 'test'}
        source = requests.post("http://localhost:5000/login/", data=post_params)
        soup1 = BeautifulSoup(source.content, 'html.parser')
        return soup1

    def get_soup2(self):
        source = requests.get("http://localhost:5000/user/")
        soup2 = BeautifulSoup(source.content, 'html.parser')
        return soup2

    def get_soup3(self):
        source = requests.get("http://localhost:5000/logout/")
        soup3 = BeautifulSoup(source.content, 'html.parser')
        return soup3

    def get_soup4(self):
        post_params = {'username': 'user', 'password': 'demo'}
        source = requests.post("http://localhost:5000/login/", data=post_params)
        soup4 = BeautifulSoup(source.content, 'html.parser')
        return soup4

    def test_login_and_user_page(self):
        soup1 = self.get_soup1()
        msg = soup1.find('p', {'id': 'a'})
        link = soup1.find('a')
        assert msg.text == 'Logged in as admin'
        assert link['href'] == '/logout'

        soup3 = self.get_soup3()
        assert soup3.text == "You've been logged out successfully!"

        soup4 = self.get_soup4()
        msg = soup4.find('p', {'id': 'a'})
        assert msg.text == 'Logged in as user'

    def test_user_page(self):
        soup2 = self.get_soup2()
        msg = soup2.find('p', {'id': 'b'})
        link = soup2.find('a')
        assert msg.text == 'You are not logged in'
        assert link['href'] == '/login'

