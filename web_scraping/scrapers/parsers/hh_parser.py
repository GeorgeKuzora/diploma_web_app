from bs4 import BeautifulSoup as bs


class hh_parser:
    def __init__(self) -> None:
        pass

    def get_number_of_job_list_pages(self, html: str) -> int:
        soup: bs = bs(html, "html.parser")
        page_count = (
            int(
                soup.find("div", attrs={"class": "pager"})
                .find_all("span", recursive=False)[-1]
                .find("a", attrs={"class": "bloko-button"})
                .find("span")
                .text
            )
            - 1
        )
        return page_count

    def get_href_of_job_cards(self, html: str) -> list[str]:
        soup: bs = bs(html, "html.parser")
        return list(
            map(
                lambda a: a.attrs["href"].split("?")[0],
                soup.find(
                    "div",
                    attrs={
                        "data-qa": "vacancy-serp__results",
                        "id": "a11y-main-content",
                    },
                ).find_all(
                    "a",
                    attrs={"class": "serp-item__title", "data-qa": "serp-item__title"},
                ),
            )
        )
