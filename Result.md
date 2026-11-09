### Step 0.1: Get Pizza Names

- API Endpoint: GET /api/names
- Number of pizza names returned: 18


### Step 0.2: Inspect HTTP Response

- HTTP Status Code: 200 (HTTP/2 200)
- Content-Type: application/json
- Content-Length: 243 bytes
- Set-Cookie Header: AWSALB, AWSALBCORS
- Vary Header: Origin


### Step 0.3: Authentication

- API Endpoint: GET /api/tools
- Without Token:
  - HTTP Status Code: 401
  - Response: {"error":"authentication failed"}
- With Token:
  - HTTP Status Code: 200
  - Tools returned:
    - Knife
    - Pizza cutter
    - Scissors


### Step 0.4: Create a Vegetarian Pizza

- API Endpoint: POST /api/pizza
- Request Body:
  {"mustBeVegetarian": true}
- Pizza ID: 53700
- Pizza returned: The Dark Frutti di Mare
- Calories: 425
- Vegetarian: true
- Number of ingredients: 6

### Step 0.5: Using Python Requests

- GET /api/names
  - Status Code: 200
  - Content-Type: application/json
  - Content-Length: 243
  - Number of pizza names: 18

- GET /api/tools (with authentication)
  - Status Code: 200
  - Tools returned: Knife, Pizza cutter, Scissors

- POST /api/pizza (with authentication)
  - Request Body: `{"mustBeVegetarian": true}`
  - Status Code: 200
  - Pizza ID: 110831
  - Pizza Name: The Young Fungi e Olive
  - Dough: Thick
  - Calories: 425
  - Vegetarian: true
  - Number of ingredients: 6

### Step 0.6: First API Test with pytest

- Test File: test_names.py
- Test Function: test_get_pizza_names
- API Endpoint: GET /api/names
- Assertions:
  - HTTP Status Code is 200
  - Margherita exists in the pizza names
- Test Result: PASSED
- Total Tests: 1 passed
- Execution Time: 1.01 seconds  

### Step 0.7: Testing the Tools Endpoint

- Test File: test_tools.py
- Test Function: test_get_tools
- API Endpoint: GET /api/tools
- Authentication: Authorization Token
- Assertions:
  - HTTP Status Code is 200
  - Tools match ["Knife", "Pizza cutter", "Scissors"]
- Test Result: PASSED
- Total Tests: 2 passed
- Execution Time: 2.02 seconds

### Step 0.8: Testing Pizza Creation

- Test File: test_pizza.py

- Test 1: test_create_vegetarian_pizza
  - API Endpoint: POST /api/pizza
  - Authentication: Valid Token
  - Expected Status Code: 200
  - Verified that the pizza name is not empty.
  - Verified that the pizza is vegetarian.
  - Verified that all ingredients are vegetarian.
  - Result: PASSED

- Test 2: test_create_pizza_without_token
  - API Endpoint: POST /api/pizza
  - Authentication: No Token
  - Expected Status Code: 401
  - Expected Error: authentication failed
  - Result: PASSED

- Total Tests: 4 passed
- Execution Time: 3.82 seconds

### Step 0.9: Create a New User and Login

- Created a new user using POST /api/users.
  - Status Code: 201
  - User ID: 1137
  - Username: lab-dc6aa2b7e107

- Logged in using POST /api/users/token/login.
  - Status Code: 200
  - Authentication Token: Received successfully

- Retrieved ratings using GET /api/ratings.
  - Status Code: 200
  - Response: {"ratings": []}

- Result: Successfully created a new user, logged in, and confirmed that the user has no ratings.

### Step 0.10: Create a Reusable API Client

- Created conftest.py.
- Created QuickPizza class inheriting from requests.Session.
- Configured the base URL: https://quickpizza.grafana.com
- Overrode the request() method to automatically add the base URL.
- Created an api fixture with session scope.
- Ran pytest -v to check existing tests.
- Test Result: 4 passed
- Execution Time: 3.69 seconds