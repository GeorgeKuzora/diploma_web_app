import aiohttp
from fake_useragent import UserAgent
import pytest
import web_scraping.scrapers.request_handlers.http_request_handler as hrh


@pytest.mark.asyncio
async def test_send_get_request():
    session = aiohttp.ClientSession()
    handler = hrh.HttpRequestHandler()
    ua = UserAgent()
    response = await handler.send_get_request(
        url="http://httpbin.org/get", session=session, params=ua.random
    )
    assert 200 == response[0]


@pytest.mark.asyncio
async def test_raise_for_status_exeption():
    session = aiohttp.ClientSession()
    handler = hrh.HttpRequestHandler()
    with pytest.raises(Exception):
        response = await handler.send_get_request(
            url="http://234adsf.org/get", session=session
        )
