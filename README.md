# api-lab
ITCS386 API Testing Lab

## Part A1: Input Domain Model

API under test: POST /api/ratings

| Condition | Description | Input Blocks | Test Values |
|---|---|---|---|
| C1: Stars value | Number of stars | Below 1, 1–5 (Base), Above 5 | 0, 3, 6 |
| C2: Stars type | Data type | Integer (Base), Decimal, Text, Missing | 3, 3.5, "3", No field |
| C3: Pizza | Pizza existence | Exists (Base), Does not exist | New pizza, 999999999 |
| C4: Token | Authorization | Own token (Base), None, Wrong length | From auth, No header, Short token |