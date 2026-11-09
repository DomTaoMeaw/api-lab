# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: HTTP 401.
- Step 0.4, the name of your pizza: The Dark Frutti di Mare.
- Step 0.12, results of the three runs without a session (optional): 2 failed and 1 passed.
- Step 0.16, blocks of "how many of the three tools are excluded": 1 tool, 2 tools, and all 3 tools.

## Defect report

- Title: API fails when all three tools are excluded.
- Request: Create a pizza with all three tools excluded.
- Expected result: HTTP 400 with a clear error message.
- Actual result: HTTP 500 with an empty response body.
- Severity: Medium.

## Part A

- Step A4, status codes when the other user reads, changes and deletes:
  - Read: HTTP 404
  - Update: HTTP 400
  - Delete: HTTP 400

## Part B

1. API tests can detect integration problems and HTTP or authentication issues. Unit tests are still needed because they are faster and test individual functions.

2. Each test creates its own user to keep tests independent. In a shop or hotel, separate accounts help protect customer information.

3. A session keeps cookies between requests so the API can recognize the same client. Without it, authentication may fail.

4. The `test_exclude_all_tools` test reveals a defect. HTTP 500 with an empty response makes the problem difficult to understand. It is marked as xfail because the API has a known issue.

5. Base choice coverage requires 9 test cases, while testing all combinations requires 72 test cases. Base choice testing is more efficient.

6. The API returned HTTP 404 for reading and HTTP 400 for updating and deleting another user's rating. These results were expected because users should only manage their own ratings.

7. The API returned HTTP 200 and displayed ratings even with an invalid token. This is a security defect because unauthorized users may access private data.

8. API tests are faster and more reliable because they test the backend directly without depending on the user interface.