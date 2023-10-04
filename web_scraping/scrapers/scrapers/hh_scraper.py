import time
import aiohttp
from collections import Counter
from fake_useragent import UserAgent
from ..request_handlers.http_request_handler import HttpRequestHandler
from ..parsers.hh_parser import HHParser


class HHScraper:
    BASE_URL = "https://hh.ru/search/vacancy"
    FIRST_PAGE = 0

    AREA = {
        "россия": 113,
        "москва": 1,
        "санкт-петербург": 2,
        "владивосток": 22,
        "волгоград": 24,
        "воронеж": 26,
        "екатеринбург": 3,
        "казань": 88,
        "калуга": 43,
        "краснодар": 53,
        "красноярск": 54,
        "нижний новгород": 66,
        "новосибирск": 4,
        "ростов-на-дону": 76,
        "самара": 78,
        "саратов": 79,
        "сочи": 237,
        "уфа": 99,
        "ярославль": 112,
        "севастополь": 130,
        "симферополь": 131,
    }

    DEFAULT_REQUEST_VALUES = {"text": None, "area": AREA["россия"], "page": FIRST_PAGE}

    def __init__(self, request_handler: HttpRequestHandler, parser: HHParser) -> None:
        self.request_handler = request_handler
        self.parser = parser

    async def fetch_data(self, text: str, area: str):
        number_of_pages = await self.get_job_list_pages_quantity(text, area)
        job_pages_urls = await self.get_job_cards_urls(text, area, number_of_pages)
        total_skills = await self.get_data_from_job_pages(job_pages_urls)
        skills_counter = Counter(total_skills)
        with open("skills.txt", "a", encoding="utf-8") as file:
            for skill in skills_counter.most_common(30):
                file.write(f"{str(skill)}\n")
        return True

    async def get_job_list_pages_quantity(self, text, area):
        user_agent = UserAgent()
        session = aiohttp.ClientSession()
        first_page_values = await self.build_request_values(text, area)
        headers = {"User-Agent": str(user_agent.random)}
        first_html_page = await self.request_handler.send_get_request(
            url=self.BASE_URL,
            session=session,
            params=first_page_values,
            headers=headers,
        )
        print("Got pages quantity")
        await session.close()
        return self.parser.get_number_of_job_list_pages(first_html_page)

    async def get_job_cards_urls(self, text, area, number_of_pages):
        user_agent = UserAgent()
        session = aiohttp.ClientSession()
        job_pages_urls = []
        for page in range(number_of_pages):
            page_values = await self.build_request_values(text, area, page)
            headers = {"User-Agent": user_agent.random}
            html_page = await self.request_handler.send_get_request(
                url=self.BASE_URL, session=session, params=page_values, headers=headers
            )
            job_pages_urls.extend(self.parser.get_href_of_job_cards(html_page))
        print("Got job cards urls")
        await session.close()
        return job_pages_urls

    async def get_data_from_job_pages(self, urls):
        session = aiohttp.ClientSession()
        user_agent = UserAgent()
        total_skills = []
        for i, url in enumerate(urls, start=1):
            if i % 99 == 0:
                session = aiohttp.ClientSession()
            headers = {"User-Agent": user_agent.random}
            job_html = await self.request_handler.send_get_request(
                url=url, session=session, headers=headers
            )
            skills = self.parser.get_job_card_data(job_html)["skills"]
            total_skills.extend(skills)
            print(skills)
            time.sleep(0.5)
        await session.close()
        return total_skills

    async def build_request_values(
        self,
        text: str = "",
        area: str = "",
        page: int = 0,
    ) -> dict:
        request_values: dict = self.DEFAULT_REQUEST_VALUES
        if text:
            request_values["text"] = text
        if area:
            request_values["area"] = area
        if page:
            request_values["page"] = page
        return request_values
