from typing import Optional
from bs4 import BeautifulSoup as bs


class HHParser:
    DEFAULT_PAGE_NUMBER = 0

    def __init__(self) -> None:
        pass

    def get_number_of_job_list_pages(self, html: str) -> int:
        soup: bs = bs(html, "html.parser")
        pager_tag = soup.find("div", attrs={"class": "pager"})
        if pager_tag:
            page_count = (
                int(
                    pager_tag.find_all("span", recursive=False)[-1]
                    .find("a", attrs={"class": "bloko-button"})
                    .span.text
                )
                - 1
            )
            return int(page_count)
        return self.DEFAULT_PAGE_NUMBER

    def get_href_of_job_cards(self, html: str) -> list[Optional[str]]:
        soup: bs = bs(html, "html.parser")
        stripped_hrefs = []
        href_for_job_cards = []
        main_content = soup.find(
            "div",
            attrs={
                "data-qa": "vacancy-serp__results",
                "id": "a11y-main-content",
            },
        )
        if main_content:
            for a in main_content.find_all(
                "a",
                attrs={
                    "class": "serp-item__title",
                    "data-qa": "serp-item__title",
                },
            ):
                if a:
                    stripped_hrefs.append(str(a.get("href").split("?")[0]))
        return stripped_hrefs

    def get_job_card_data(self, html: str) -> dict:
        skills = []
        soup: bs = bs(html, "html.parser")
        skills_div = soup.find("div", attrs={"class": "bloko-tag-list"})
        if skills_div:
            for skill in skills_div.children:
                skills.append(str(skill.find("span").text))
        return {"skills": skills}


# Back-end developer (Django, Python)
#
# от 120 000 до 120 000 ₽ на руки
#
# Требуемый опыт работы: 3–6 лет
#
# Полная занятость, полный день
#
# Описание
#
# Ключевые навыки <- 1
#
# ООО Автоматизация ПРО
#
# Санкт-Петербург, Петроградская
