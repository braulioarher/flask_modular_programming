from .api import app
import requests

class Test_API:
    client = app.test_client()

    def test_hello_from_app(self):
        url = "/Hello"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == b'Welcome to your flask application'
            
    def test_hello_from_app_on_port(self):
        url = "http://localhost:8081/Hello"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.text == 'Welcome to your flask application'

    def test_hello_from_nginx_server(self):
        url = "http://localhost:8000/Hello"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.text == 'Welcome to your flask application'    


    def test_conf_file_contents(self):
        with open('deploy.conf', 'r') as f:
            content = f.read()
            assert "location /Hello" in content
            assert "server localhost:8081" in content
            assert "listen 8000" in content