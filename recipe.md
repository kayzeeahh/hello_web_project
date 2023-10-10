{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# Sortnames route
POST HTTP://localhost:5001/sort-names?names=Joe,Alice,Zoe,Julia,Kieran


2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

# GET /sort-names
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide some names
"""

3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
POST /sort-names
  Expected response (200 OK):
  "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_sort_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

