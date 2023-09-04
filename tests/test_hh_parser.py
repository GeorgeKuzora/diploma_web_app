import pytest
import web_scraping.scrapers.parsers.hh_parser as hhp


@pytest.fixture
def paginated_list_of_job_cards_html():
    with open("tests/mock_pages/hh_search_list_page.html", "r") as file:
        html = file.read()
    assert html is not None
    return html


@pytest.fixture
def job_page_html():
    with open("tests/mock_pages/hh_job_page.html", "r") as file:
        html = file.read()
    assert html is not None
    return html


@pytest.fixture
def empty_page_html():
    with open("tests/mock_pages/empty.html", "r") as file:
        html = file.read()
    assert html is not None
    return html


def test_get_number_of_job_list_pages(
    paginated_list_of_job_cards_html, empty_page_html
):
    parser = hhp.HHParser()
    pages_number = parser.get_number_of_job_list_pages(paginated_list_of_job_cards_html)
    assert pages_number == 28
    pages_number = parser.get_number_of_job_list_pages(empty_page_html)
    assert pages_number == 0


def test_get_hrefs_for_job_list_pages(
    paginated_list_of_job_cards_html, empty_page_html
):
    test_number_of_job_list_hrefs = 51
    parser = hhp.HHParser()
    job_card_hrefs = parser.get_href_of_job_cards(paginated_list_of_job_cards_html)
    assert len(job_card_hrefs) == test_number_of_job_list_hrefs
    for h in job_card_hrefs:
        assert isinstance(h, str)
    print(job_card_hrefs)
    job_card_hrefs = parser.get_href_of_job_cards(empty_page_html)
    assert job_card_hrefs == []


def test_get_job_card_data(job_page_html, empty_page_html):
    test_number_of_skills = 5
    parser = hhp.HHParser()
    skills = parser.get_job_card_data(job_page_html)
    assert len(skills["skills"]) == test_number_of_skills
    assert all(skills["skills"])
    skills = parser.get_job_card_data(empty_page_html)
    assert skills["skills"] == []
