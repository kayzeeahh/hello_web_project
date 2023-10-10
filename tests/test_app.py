# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"
    
    
"""
When I make a GET request to /
I should get a 200 response
"""
def test_get_wave_(web_client):
    response = web_client.get('/wave?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'I am waving at Dana'
    

    """
    When I make a POST request 
    """
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: Hello'
    

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee', 'num': '3'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in eee'


"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia', 'num': '5'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in eunoia'


"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial', 'num': '4'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in mercurial'
    
    
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names':'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'
    
    
def test_get_names(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo' 
    
# === End Example Code ===
