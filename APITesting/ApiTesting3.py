import requests


def test_get_all_products():
   response = requests.get("https://fakestoreapi.com/products")
   assert response.status_code == 200
   assert response.elapsed.total_seconds() < 2


   data = response.json()
   assert type(data) == list
   assert len(data) > 0

   assert isinstance(data, list)

   product = data[0]
   assert "id" in product
   assert "title" in product
   assert "price" in product
   print(response.json())


def test_post_new_product():
   payload = {
      "title": "keyboard",
      "price": 100,
      "description": "good",
      "category": "optical",
      "image": "http://example.com"
   }
   response = requests.post("https://fakestoreapi.com/products", json=payload)

   assert response.status_code == 201
   assert response.elapsed.total_seconds() < 10

   data = response.json()
   assert isinstance(data, dict)

   assert "id" in data
   assert data["title"] == payload["title"]
   assert data["price"] == payload["price"]
   assert data["description"] == payload["description"]
   assert data["category"] == payload["category"]
   assert data["image"] == payload["image"]

   print(response.json())



def test_update_product():
   payload = {
      "title": "mousepad",
      "price": 50,
      "description": "good",
      "category": "glass",
      "image": "http://example.com"
   }
   BASE_URL = "https://fakestoreapi.com/products"
   response = requests.put(f"{BASE_URL}/21", json=payload)

   assert response.status_code == 200
   assert response.elapsed.total_seconds() < 2

   data = response.json()
   assert isinstance(data, dict)

   assert data["title"] == payload["title"]
   assert data["price"] == payload["price"]
   assert data["description"] == payload["description"]
   assert data["category"] == payload["category"]
   assert data["image"] == payload["image"]


def test_delete_product():
   response = requests.delete("https://fakestoreapi.com/products/21")

   assert response.status_code == 200

   if response.text:
      data = response.json()
      assert data["id"] == 21










