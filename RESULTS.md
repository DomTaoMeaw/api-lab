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

### Step 0.11: Test a New User's Ratings

- Created a new user and logged in using the auth fixture.
- Sent GET /api/ratings with the user's authentication token.
- Expected Status Code: 200
- Expected Response: {"ratings": []}
- Result: PASSED
- Pytest: 5 passed in 6.24s

### Step 0.12, results of the three runs without a session (optional):
  - Run 1: FAILED (Login returned 401)
  - Run 2: PASSED (Login returned 200)
  - Run 3: FAILED (Login returned 401)
  - Summary: 2 failed and 1 passed.

### Step 0.13: Created a new rating successfully.
  - Test result: 6 passed in 6.42s.
  - Verified the rating ID, stars, and pizza ID.  

### Step 0.14: Tested reading, updating, and deleting ratings.
  - Test result: 9 passed in 15.04s.
  - Read rating: HTTP 200.
  - Update rating: HTTP 200.
  - Delete rating: HTTP 204.
  - Read deleted rating: HTTP 404.  

### Step 0.15: Tested refused requests.
  - Test result: 12 passed in 15.63s.
  - Duplicate username: HTTP 400.
  - Wrong password: HTTP 401.
  - Empty username: HTTP 400.
  - All error responses matched the expected messages.

### Step 0.16: Tested excluded tools.
  - Test result: 17 passed, 1 xfailed in 21.29s.
  - Excluding Knife: PASSED.
  - Excluding Scissors: PASSED.
  - Excluding Knife and Scissors: PASSED.
  - Excluding all three tools: XFAILED.

- Defect 1: The API returns HTTP 500 with an empty response body
  when all three tools are excluded.
  - Expected: HTTP 400 with a clear error message.
  - Actual: HTTP 500 with Content-Length: 0.
  - The test is marked as xfail because the API defect is known.  


## Part A2: Testing Different Input Blocks

### C1: Stars Range
- Stars = 0: HTTP 400 (Rejected)
- Stars = 6: HTTP 400 (Rejected)

### C2: Stars Type
- Decimal (3.5): HTTP 400 (Rejected)
- Text ("three"): HTTP 400 (Rejected)
- Missing stars: HTTP 400 (Rejected)

All tests passed successfully.

### C3: Pizza ID

- Existing pizza (Base): A valid pizza ID was used.
- Non-existing pizza ID (999999999):
  - HTTP Status Code: 400
  - Error: `pizza ID 999999999 not found`
- Result: PASSED

### C4: Authorization Token

- Missing token:
  - HTTP Status Code: 401
  - Error: `authentication failed`
- Invalid short token (`short`):
  - HTTP Status Code: 401
  - Error: `authentication failed`
- Result: PASSED

### Part A2: Overall Test Results

- Test File: `test_create_rating.py`
- Total test cases: 9
- C1: Stars value
- C2: Stars type
- C3: Pizza ID
- C4: Authorization token

Full test suite:
- Total tests collected: 27
- Passed: 26
- Xfailed: 1
- Failed: 0
- Execution Time: 32.36 seconds

Defect 1 remains marked as XFAILED because the API returns HTTP 500 instead of the expected HTTP 400 when all three tools are excluded.


## Part A3: Testing Rating Updates

### API Endpoint
`PUT /api/ratings/{id}`

### Test File
`test_update_rating.py`

### Test Function
`test_update_rating_stars`

### Test Cases

| Stars | Expected Status Code | Result |
|---|---|---|
| 0 | 400 | PASSED |
| 1 | 200 | PASSED |
| 5 | 200 | PASSED |
| 6 | 400 | PASSED |

### Assertions
- Stars values 1 and 5 were successfully updated.
- Stars values 0 and 6 were rejected.
- After a rejected update, the original rating remained unchanged.

### Test Results
- Part A3: 4 passed in 9.10s.
- Full test suite: 30 passed, 1 xfailed in 41.79s.
- Failed: 0

## Part A4: Testing Rating Ownership

### Test File
`test_rating_owner.py`

### Test Cases and Results

| Test Case | Result |
|---|---|
| Other user cannot read a rating | PASSED |
| Other user cannot update a rating | PASSED |
| Other user cannot delete a rating | PASSED |

### Full Test Suite Results
- Total tests: 34
- Passed: 33
- Xfailed: 1
- Failed: 0
- Execution time: 50.15 seconds

### Conclusion
The API prevents other users from reading, updating, or deleting a rating they do not own. The original rating remains unchanged after unauthorized update and delete attempts.


### Part B
### 1. API Tests vs. Unit Tests

API tests using a real server can detect problems that unit tests with stubs may miss, such as:
1. Integration issues between the API and the database.
2. Problems with HTTP responses, authentication, and communication between components.

Unit tests are still necessary because they are faster and help developers test individual functions separately. They also make it easier to identify and fix bugs.

### 2. Creating a Separate User for Each Test

Each test creates its own user to keep tests independent and avoid sharing data.

In a shop or hotel system, each customer should have their own account to protect personal information and prevent unauthorized access.

### 3. Using One Session

A session keeps cookies between requests, so the API can recognize the same client.

Without a session, cookies may be lost, causing authentication or request failures.

### 4. Excluded Tools Defect

The `test_exclude_all_tools` test reveals a defect. The API returns HTTP 500 with an empty response instead of HTTP 400 with a clear error message.

HTTP 500 makes the problem harder to understand and debug. It is marked as xfail because the API has a known issue and the test is expected to fail.

### 5. Base Choice Testing

Base choice coverage requires 9 test cases, while testing all possible combinations requires 72 test cases.

Base choice testing is more efficient because it tests each input condition without testing every possible combination.

### 6. Rating Ownership

The API returned HTTP 404 for reading and HTTP 400 for updating and deleting a rating owned by another user.

These results were expected because users should only access and manage their own ratings. The original rating remained unchanged.

### 7. Made-up Token

The API returned HTTP 200 and displayed the ratings even though the request used an invalid token.

This is a security defect because the API does not properly validate the token. Unauthorized users may access private data, which creates a data security risk.

### 8. API Testing vs. UI Testing

API tests are faster and more reliable because they test the backend directly without depending on the user interface. They also make it easier to test many inputs and error cases.