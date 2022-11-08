import os
import pytest
from app import app


class Test_API:
    client = app.test_client()

    def test_set_cookie(self):
        response = self.client.get('/setcookie/')
        assert response.status_code == 200
        assert b'cookie was successfully set' in response.data

    def test_get_cookie(self):
        response = self.client.get('/getcookie/')
        assert response.status_code == 200
        assert b'you visited this site 1 times' in response.data

        response = self.client.get('/getcookie/')
        assert response.status_code == 200
        assert b'you visited this site 2 times' in response.data

        response = self.client.get('/getcookie/')
        assert response.status_code == 200
        assert b'you visited this site 3 times' in response.data

        # test set cookie and get cookie
        response = self.client.get('/setcookie/')
        assert response.status_code == 200

        response = self.client.get('/getcookie/')
        assert response.status_code == 200
        assert b'you visited this site 1 times' in response.data

