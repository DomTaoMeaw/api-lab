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
