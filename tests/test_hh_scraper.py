import asyncio
import pytest
from web_scraping.scrapers.scrapers.hh_scraper import HHScraper
from web_scraping.scrapers.parsers.hh_parser import HHParser
from web_scraping.scrapers.request_handlers.http_request_handler import (
    HttpRequestHandler,
)


@pytest.mark.scraper
@pytest.mark.asyncio
async def test_hh_scraper():
    parser = HHParser()
    request_handler = HttpRequestHandler()
    scraper = HHScraper(request_handler, parser)
    resp = await scraper.fetch_data("python", "санкт-петербург")
    assert resp


@pytest.mark.scraper
@pytest.mark.asyncio
async def test_get_job_list_pages_quantity():
    parser = HHParser()
    request_handler = HttpRequestHandler()
    scraper = HHScraper(request_handler, parser)
    resp = await scraper.get_job_list_pages_quantity("python", "москва")
    assert resp
    assert type(resp) is int
    assert resp > 0


# @pytest.mark.scraper
# @pytest.mark.asyncio
# async def test_get_job_list_pages_quantity():
