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


def test_get_number_of_job_list_pages(paginated_list_of_job_cards_html):
    parser = hhp.hh_parser()
    pages_number = parser.get_number_of_job_list_pages(paginated_list_of_job_cards_html)
    assert pages_number == 28


def test_get_hrefs_for_job_list_pages(paginated_list_of_job_cards_html):
    test_number_of_job_list_hrefs = 51
    parser = hhp.hh_parser()
    job_card_hrefs = parser.get_href_of_job_cards(paginated_list_of_job_cards_html)
    assert len(job_card_hrefs) == test_number_of_job_list_hrefs


def test_get_job_card_data(job_page_html):
    test_number_of_skills = 5
    parser = hhp.hh_parser()
    skills = parser.get_job_card_data(job_page_html)
    assert len(skills["skills"]) == test_number_of_skills
    assert all(skills["skills"])

