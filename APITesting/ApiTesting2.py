import requests
BASE_URL = "https://api.restful-api.dev/objects"

def test_get_all_objects():
    response = requests.get("https://api.restful-api.dev/objects")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for item in data:
        assert "id" in item
        assert "name" in item
        assert "data" in item



def test_get_one_object():
    response = requests.get("https://api.restful-api.dev/objects/1")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "name" in data
    assert "data" in data

def test_post_new_object():
    payload = {
        "name": "QA test object",
        "data": {
            "color": "black",
            "price": 1000
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    assert response.status_code == 200 or response.status_code == 201

    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert data['name'] == payload['name']

    print(response.json())



def test_update_object():
    # 1. создаём объект
    create_payload = {
        "name": "QA object",
        "data": {
            "color": "black",
            "price": 1000
        }
    }

    create_response = requests.post(BASE_URL, json=create_payload)
    obj_id = create_response.json()["id"]

    # 2. обновляем объект
    update_payload = {
        "name": "UPDATED QA object",
        "data": {
            "color": "red",
            "price": 2000
        }
    }

    response = requests.put(f"{BASE_URL}/{obj_id}", json=update_payload)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == obj_id
    assert data["name"] == update_payload["name"]
    assert data["data"]["color"] == "red"
    assert data["data"]["price"] == 2000




def test_delete_object():

    # 1. CREATE OBJECT
    create_payload = {"name": "QA object"}

    create_response = requests.post(
        "https://api.restful-api.dev/objects",
        json=create_payload
    )

    obj_id = create_response.json()["id"]

    # 2. DELETE OBJECT
    delete_response = requests.delete(
        f"https://api.restful-api.dev/objects/{obj_id}"
    )

    assert delete_response.status_code in (200, 204)

    # 3. VERIFY DELETE
    get_response = requests.get(
        f"https://api.restful-api.dev/objects/{obj_id}"
    )

    assert get_response.status_code == 404













