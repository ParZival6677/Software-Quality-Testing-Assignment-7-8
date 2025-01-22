Feature: Regression Testing
  Scenario: Create a new pet
    Given the API endpoint is "https://petstore.swagger.io/v2/pet"
    When I send a POST request with the following payload:
    """
    {
      "id": 111,
      "category": {"id": 111, "name": "string"},
      "name": "doggie",
      "photoUrls": ["string"],
      "tags": [{"id": 1112, "name": "string"}, {"id": 11123, "name": "happy"}],
      "status": "available"
    }
    """
    Then the response status code should be 200
    And the response should contain the pet ID

  Scenario: Get a pet by ID
    Given the API endpoint is "https://petstore.swagger.io/v2/pet/111"
    When I send a GET request
    Then the response status code should be 200
    And the response should contain the pet data

  Scenario: Get pet list
    Given the API endpoint is "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    When I send a GET request
    Then the response status code should be 200
    And the response should contain an array of pets

  Scenario: Get pet by tags
    Given the API endpoint is "https://petstore.swagger.io/v2/pet/findByTags?tags=string,happy"
    When I send a GET request
    Then the response status code should be 200
    And the response should show pets with these tags

  Scenario: Get pet by status
    Given the API endpoint is "https://petstore.swagger.io/v2/pet/findByStatus?status=available,sold"
    When I send a GET request
    Then the response status code should be 200
    And the response should show pets with these statuses

  Scenario: Update pet info
    Given the API endpoint is "https://petstore.swagger.io/v2/pet"
    When I send a PUT request with the updated pet data
    Then the response status code should be 200
    And the response should contain the updated pet information

  Scenario: Delete pet
    Given the API endpoint is "https://petstore.swagger.io/v2/pet/111"
    When I send a DELETE request
    Then the response status code should be 200
    And the response should confirm the pet is deleted