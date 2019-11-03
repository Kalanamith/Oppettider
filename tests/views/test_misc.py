import pytest


@pytest.mark.parametrize(
    "url, expected",
    [
        ("oh/v2/", "Not Found"),
        ("oh/v1", "Not Found"),
        ("oh", "Not Found"),
        ("oh", "Not Found")
    ]
)
async def test_invalid_url(oh_client, url, expected):
    """
    Given
    -   Invalid url
    When
    -   Sending get for an invalid url
    Then
    -   Should return {"ping": "pong"}
    :param oh_client: aiohttp test client
    """
    resp = await oh_client.get(url)
    assert resp.status == 404
    assert resp.reason == expected