async def test_ping(oh_client):
    """
    Given
    -   Valid url to test ping
    When
    -   Sending get for ping
    Then
    -   Should return {"ping": "pong"}
    :param oh_client: aiohttp test client
    """
    url: str = "oh/v1/"
    resp = await oh_client.get(url)
    assert resp.status == 200
    assert await resp.json() == {'ping': 'pong'}
