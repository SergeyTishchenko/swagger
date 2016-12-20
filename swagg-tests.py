import requests
import json
import pytest


@pytest.fixture
def test_data():
    baseUrl = 'http://petstore.swagger.io/v2'
    header = {'Content-type': 'application/json'}
    data = dict(id=99, username="swagg", firstName="test001", lastName="test001", email="123l@gmail.com",
                password="q1w2e3r4&77", phone="123456789", userStatus=5)
    return [baseUrl, header, data]


class swagg_api_test(object):

    def user_create(self, test_data):
        method = '/user'
        response = requests.post(test_data[0] + method, headers=test_data[1], data=json.dumps(test_data[2]))
        assert response.status_code == 200, "Unexpected response code!"

    def user_login(self, test_data):
        method = '/user/login?username={0}&password={1}'.format(test_data[2]['username'], test_data[2]['password'])
        response = requests.get(test_data[0] + method)
        assert response.status_code == 200, "Unexpected response code!"

    def user_logout(self, test_data):
        method = '/user/logout'
        response = requests.get(test_data[0] + method)
        assert response.status_code == 200, 'Unexpected response code!'
        assert not response.content, 'Response body is not empty!'

    def user_delete(self, test_data):
        method = '/user/{0}'.format(test_data[2]['username'])
        response = requests.delete(test_data[0] + method)
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, 'Unexpected response code!'

    def user_get(self, test_data):
        method = '/user/{0}'.format(test_data[2]['username'])
        response = requests.get(test_data[0] + method)
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, 'Unexpected response code!'

    def user_update(self, test_data):
        test_data[2]['firstName'] = 'Changed'
        method = '/user/{0}'.format(test_data[2]['username'])
        response = requests.put(test_data[0] + method, headers=test_data[1], data=json.dumps(test_data[2]))
        assert response.status_code != 400, 'Invalid username supplied'
        assert response.status_code != 404, 'User not found'
        assert response.status_code == 200, 'Unexpected response code!'