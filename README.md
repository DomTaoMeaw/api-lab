# api-lab
ITCS386 API Testing Lab

## Part A1: Input Domain Model

API under test: POST /api/ratings

| Condition | Description | Input Blocks |
|---|---|---|
| C1: Stars range | Number of stars | Below 1, 1–5, Above 5 |
| C2: Stars type | Data type of stars | Integer, Decimal, Text, Missing |
| C3: Pizza ID | Whether the pizza exists | Existing pizza, Non-existing pizza |
| C4: Authorization | Validity of authorization token | Own valid token, No token, Invalid token |