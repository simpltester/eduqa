import pytest
import requests

resources = {
    "posts" : 100,
    "comments" : 500,
    "albums" : 100,
    "photos" : 5000,
    "todos" : 200,
    "users" : 10
}

resource_for_user = {
    "posts" : 10,
    "todos" : 20,
    "albums" : 10
}

test_data = {
    "title" : "test_title",
    "body" : "test_body",
    "userId" : "1"
}

URL = "https://jsonplaceholder.typicode.com/"

def get_json(url, params=""):
    response = requests.get(url, params=params)
    return response.json()

def get_status_code(url):
    response = requests.get(url)
    return response.status_code

def test_connection():
    url = "https://jsonplaceholder.typicode.com/posts"
    status_code = get_status_code(url)
    assert status_code == 200

def test_answer_is_json():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert "application/json" in response.headers['Content-Type']

@pytest.mark.parametrize("test_data", [test_data])
def test_post_method(test_data):
    response = requests.post("https://jsonplaceholder.typicode.com/posts",
        data=test_data) 
    assert response.status_code == 201
    answer = response.json()
    answer.pop("id")
    assert answer == test_data 

@pytest.mark.parametrize("res, quant", list(resources.items()))
def test_common_resources(res, quant):
    answer = get_json(f"{URL}{res}")
    assert get_status_code(URL) == 200
    assert len(answer) == quant

@pytest.mark.parametrize("resource, counts", list(resource_for_user.items()))
def test_users_resources(resource, counts):
    answer = get_json(f"{URL}{resource}", params={"userId": "1"})
    assert get_status_code(URL) == 200
    assert len(answer) == counts
