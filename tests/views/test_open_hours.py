async def test_get_open_hours(oh_client):

    pass


async def test_post_open_hours(oh_client):
    post_data = {
        "friday": [
            {
                "type": "open",
                "value": 64800
            }
        ],
        "saturday": [
            {
                "type": "close",
                "value": 3600,
            },
            {
                "type": "open",
                "value": 32400,
            },
            {
                "type": "close",
                "value": 39600
            },
            {
                "type": "open",
                "value": 57600
            },
            {
                "type": "close",
                "value": 82800
            }
        ]
    }
    url: str = "oh/v1/opening_hours"

    response = await oh_client.post(path=url, json=post_data)
    k = await response.json()
    kk = k
