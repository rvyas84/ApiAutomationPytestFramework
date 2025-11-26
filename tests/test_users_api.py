import json
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

#Get Request
def test_get_users(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("GET JSON Response Body: ", json_str)
    assert len(json_data) > 1

#POST Request
def test_create_users(api_client, load_test_data):

    # Create User
    payload = generate_test_user_payload(load_test_data, api_client)

    response = api_client.post(payload, "users")
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("POST JSON Response Body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == payload["name"]

    # Validate newly created user
    get_response = api_client.get(f"users/{user_id}")
    assert get_response.status_code == 200

#PUT Request
def test_update_users(api_client, load_test_data):
    
    # Create User
    payload = generate_test_user_payload(load_test_data, api_client)

    response = api_client.post(payload, "users")
    assert response.status_code == 201

    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("POST JSON Response Body: ", json_str)
    user_id = json_data["id"]

    # Update User
    payload = update_user(payload, api_client)

    response = api_client.put(payload, f"users/{user_id}")
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("PUT JSON Response Body: ", json_str)
    assert "name" in json_data

    # Validate updated user
    get_response = api_client.get(f"users/{user_id}")
    assert get_response.status_code == 200

# #DELET Request
def test_delete_users(api_client, load_test_data):
    
    # Create User
    payload = generate_test_user_payload(load_test_data, api_client)

    response = api_client.post(payload, "users")
    assert response.status_code == 201

    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print("POST JSON Response Body: ", json_str)
    user_id = json_data["id"]

    # Delete User
    response = api_client.delete(f"users/{user_id}")
    assert response.status_code == 204

    # Validate newly created user deleted
    get_response = api_client.get(f"users/{user_id}")
    assert get_response.status_code == 404


# Generate Test User Data
def generate_test_user_payload(load_test_data, api_client):
    payload = load_test_data["new_user"]

    first_name = api_client.generate_random_string()
    last_name = api_client.generate_random_string()
    
    full_name = f"{first_name} {last_name}"
    unique_email = f"{first_name}.{last_name}@example.com"

    payload["name"] = full_name
    payload["email"] = unique_email

    return payload

def update_user(test_data, api_client):
    payload = test_data

    first_name = api_client.generate_random_string()
    last_name = api_client.generate_random_string()

    full_name = f"{first_name} {last_name}"
    
    payload["name"] = full_name

    return test_data
    