# api-lab
ITCS386 API Testing Lab

## Part A1: Input Domain Model

API under test: `POST /api/ratings`

| Condition | Description | Input Blocks | Test Values | Test Function |
|---|---|---|---|---|
| C1: Stars value | Number of stars | Below 1 | 0 | `test_stars_out_of_range[0]` |
| C1: Stars value | Number of stars | 1–5 (Base) | 3 | `test_base_choice_is_saved` |
| C1: Stars value | Number of stars | Above 5 | 6 | `test_stars_out_of_range[6]` |
| C2: Stars type | Data type | Integer (Base) | 3 | `test_base_choice_is_saved` |
| C2: Stars type | Data type | Decimal | 3.5 | `test_decimal_stars` |
| C2: Stars type | Data type | Text | "three" | `test_text_stars` |
| C2: Stars type | Data type | Missing | No field | `test_missing_stars` |
| C3: Pizza | Pizza existence | Exists (Base) | New pizza | `test_base_choice_is_saved` |
| C3: Pizza | Pizza existence | Does not exist | 999999999 | `test_pizza_id_does_not_exist` |
| C4: Token | Authorization | Own token (Base) | From auth | `test_base_choice_is_saved` |
| C4: Token | Authorization | None | No header | `test_missing_token` |
| C4: Token | Authorization | Wrong length | Short token | `test_short_token` |
