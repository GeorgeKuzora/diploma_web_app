from typing import Protocol

from web_scraping.scrapers.interfaces.parser import Parser
from web_scraping.scrapers.interfaces.request_handler import RequestHandler


class Scraper(Protocol):
    def __init__(self, request_handler: RequestHandler, parser: Parser) -> None:
        ...

    def run(self, *args, **kwargs) -> list:
        ...
