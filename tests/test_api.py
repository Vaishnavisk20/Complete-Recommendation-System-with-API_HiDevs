import requests

BASE_URL = "https://zany-space-system-69r5wv79ww5qc55p5-8000.app.github.dev"

def test_health():
    res = requests.get(f"{BASE_URL}/health")
    assert res.status_code == 200

def test_recommend():
    headers = {"x-api-key": "12345"}
    res = requests.get(f"{BASE_URL}/recommend/1", headers=headers)
    assert res.status_code == 200