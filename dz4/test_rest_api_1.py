import pytest
import requests

def get_json(url):
    response = requests.get(url)
    return response.json()

def get_status_code(url):
    response = requests.get(url)
    return response.status_code

def is_jpg(jpg_url):
    jpg = jpg_url.split("/")[-1]
    if ".jpg" in jpg  or ".jpeg" in jpg:
        return True

def get_all_breeds():
    # по хорошему тут должен быть список пород в list, но так проще)
    url = "https://dog.ceo/api/breeds/list/all"
    answer = get_json(url)
    return answer["message"].keys()

def get_sub_breed(breed):
    url = f"https://dog.ceo/api/breed/{breed}/list"
    answer = get_json(url)
    print(answer["message"])
    return answer["message"]

    
def test_connection():
    url = "https://dog.ceo/api/breeds/image/random"
    status_code = get_status_code(url)
    assert status_code == 200

def test_answer_is_json():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.headers['Content-Type'] == "application/json"

def test_status_in_json():
    url = "https://dog.ceo/api/breeds/image/random"
    answer = get_json(url)
    assert answer["status"] == "success"

@pytest.mark.parametrize("count", range(10))
def test_message_in_json(count):
    url = "https://dog.ceo/api/breeds/image/random"
    answer = get_json(url)
    assert is_jpg(answer["message"])

def test_error_request_connection():
    url = "https://dog.ceo/api/breed/test/images/random"
    status_code = get_status_code(url)
    assert status_code == 404

def test_error_answer_by_json():
    url = "https://dog.ceo/api/breed/test/images/random"
    answer = get_json(url)
    assert answer["status"] == "error"

def test_get_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    answer = get_json(url)
    breeds = get_all_breeds()
    assert answer["status"] == "success"
    assert len(answer["message"]) == len(breeds)

@pytest.mark.parametrize("breed", get_all_breeds())
def test_breeds_answer(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    answer = get_json(url)
    assert answer["status"] == "success"
    assert is_jpg(answer["message"])


@pytest.mark.parametrize("sub_breed", get_sub_breed("terrier"))
def test_get_sub_breed_terrier(sub_breed):
    url = f"https://dog.ceo/api/breed/terrier/{sub_breed}/images/random"
    answer = get_json(url)
    assert answer["status"] == "success"
    assert is_jpg(answer["message"])
