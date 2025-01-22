import requests
from behave import given, when, then
import json

@given('the API endpoint is "{endpoint}"')
def step_given_api_endpoint(context, endpoint):
    context.endpoint = endpoint

@when('I send a POST request with the following payload:')
def step_when_post_request(context):
    payload = json.loads(context.text)
    headers = {"Content-Type": "application/json"}
    context.response = requests.post(context.endpoint, json=payload, headers=headers)

@when('I send a GET request')
def step_when_get_request(context):
    context.response = requests.get(context.endpoint)

@when('I send a PUT request with the updated pet data')
def step_when_put_request(context):
    payload = {
        "id": 111,
        "category": {"id": 111, "name": "updated"},
        "name": "updated_doggie",
        "photoUrls": ["updated_string"],
        "tags": [{"id": 1112, "name": "updated_tag"}],
        "status": "sold"
    }
    headers = {"Content-Type": "application/json"}
    context.response = requests.put(context.endpoint, json=payload, headers=headers)

@when('I send a DELETE request')
def step_when_delete_request(context):
    context.response = requests.delete(context.endpoint)

@then('the response status code should be {status_code:d}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain the pet ID')
def step_then_contains_pet_id(context):
    json_response = context.response.json()
    assert 'id' in json_response, "Response does not contain 'id'"

@then('the response should contain the pet data')
def step_then_contains_pet_data(context):
    json_response = context.response.json()
    assert 'id' in json_response, "Response does not contain 'id'"
    assert 'name' in json_response, "Response does not contain 'name'"

@then('the response should contain an array of pets')
def step_then_contains_array_of_pets(context):
    json_response = context.response.json()
    assert isinstance(json_response, list), "Response is not an array"
    assert len(json_response) > 0, "Response array is empty"

@then('the response should show pets with these tags')
def step_then_contains_pets_with_tags(context):
    json_response = context.response.json()
    assert isinstance(json_response, list), "Response is not an array"
    for pet in json_response:
        assert 'tags' in pet, "Pet does not contain 'tags'"
        tags = [tag['name'] for tag in pet['tags']]
        assert any(tag in ["string", "happy"] for tag in tags), \
            "Pet tags do not match the expected tags"

@then('the response should show pets with these statuses')
def step_then_contains_pets_with_statuses(context):
    json_response = context.response.json()
    assert isinstance(json_response, list), "Response is not an array"
    for pet in json_response:
        assert 'status' in pet, "Pet does not contain 'status'"
        assert pet['status'] in ["available", "sold"], \
            f"Pet status '{pet['status']}' is not expected"

@then('the response should confirm the pet is deleted')
def step_then_confirm_pet_deleted(context):
    json_response = context.response.json()
    assert 'message' in json_response, "Response does not contain 'message'"
    assert json_response['message'] == "111", "Pet ID not confirmed as deleted"

@then('the response should indicate the pet is not found')
def step_then_pet_not_found(context):
    json_response = context.response.json()
    assert 'message' in json_response, "Response does not contain 'message'"
    assert json_response['message'] == "Pet not found", \
        "Response message does not indicate pet is not found"
