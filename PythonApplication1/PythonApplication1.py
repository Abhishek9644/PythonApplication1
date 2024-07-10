import requests
 
frontend_url = "https://127.0.0.1"
def test_front();
response = response.get(f"{frontend_url}/message")   
assert response.status_code ==200
assert"hello" in response.text

if _name_ == "_main_":
    test_front()
    print("passed the integration")

