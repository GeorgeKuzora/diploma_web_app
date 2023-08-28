import aiohttp
from fake_useragent import UserAgent
import pytest
import web_scraping.scrapers.request_handlers.http_request_handler as hrh


DEFAULT_REQUEST_VALUES = {"text": "python", "area": 2, "page": 0}


@pytest.mark.asyncio
async def test_send_get_request_without_user_agent():
    session = aiohttp.ClientSession()
    handler = hrh.HttpRequestHandler()
    response = await handler.send_get_request(
        url="https://hh.ru/search/vacancy",
        session=session,
        params=DEFAULT_REQUEST_VALUES,
    )
    assert response
    assert "python" in response


@pytest.mark.asyncio
async def test_send_get_request_with_user_agent():
    session = aiohttp.ClientSession()
    ua = UserAgent()
    handler = hrh.HttpRequestHandler()
    response = await handler.send_get_request(
        url="https://hh.ru/search/vacancy",
        session=session,
        params=DEFAULT_REQUEST_VALUES,
        headers={"User-Agent": ua.random},
    )
    assert response
    assert "python" in response


@pytest.mark.asyncio
async def test_raise_for_status_exeption():
    session = aiohttp.ClientSession()
    handler = hrh.HttpRequestHandler()
    with pytest.raises(Exception):
        response = await handler.send_get_request(
            url="http://234adsf.org/get", session=session
        )
