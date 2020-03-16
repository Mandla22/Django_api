from rest_framework.test import APITestCase


class Test(APITestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000"
        self.post_data = {
            "date": "2021-03-11T09:25:03Z",
            "amount": 20,
            "type": "water"
        }

    def test_get(self):
        response = self.client.get(self.base_url+"/api/")
        self.assertEqual(200, response.status_code)

    def test_post(self):
        response = self.client.post(self.base_url+"/api/", self.post_data)
        self.assertEqual(200, response.status_code)