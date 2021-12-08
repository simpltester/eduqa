import pytest
import requests

def get_json(url, params=""):
    response = requests.get(url, params=params)
    return response.json()

def get_status_code(url):
    response = requests.get(url)
    return response.status_code
  
def test_connection():
    url = "https://api.openbrewerydb.org/breweries"
    status_code = get_status_code(url)
    assert status_code == 200

def test_answer_is_json():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    assert "application/json" in response.headers['Content-Type']

@pytest.mark.parametrize("find", ("dog", "west", "east", "coast", "beach"))
def test_search(find):
    url = "https://api.openbrewerydb.org/breweries/search"
    params = {"query" : find}
    answer = get_json(url, params)
    assert get_status_code(url) == 200
    assert len(answer) > 1

@pytest.mark.parametrize("text", ("dog", "west", "east", "coast", "beach"))
def test_autocomplete(text):
    url = "https://api.openbrewerydb.org/breweries/autocomplete"
    params = {"query" : text}
    answer = get_json(url, params)
    assert len(answer) >= 1

filters = {
    "by_city" : "Alma",
    "by_dist" : "-117.113975,32.9167796",
    "by_name" : "west",
    "by_state" : "Hawaii",
    "by_postal" : "94002",
    "by_type" : "micro",
}

@pytest.mark.parametrize("find, data", list(filters.items()))
def test_find_by(find, data):
    url = "https://api.openbrewerydb.org/breweries"
    params = {find : data}
    answer = get_json(url, params)
    assert get_status_code(url) == 200
    assert len(answer) > 1
