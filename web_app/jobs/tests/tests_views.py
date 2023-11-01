"""
Tests for jobs app views.

Tests should be run from project root.

Examples:
    # For running a test use following command
    python web_app/manage.py test
"""
from typing import Any, Callable
from django.test import TestCase
from django.urls import reverse
from jobs.views import index


class TestJobViews(TestCase):
    """
    Tests for views in skills app.
    """
    DETAILS_PAGE_JOB_ID: int = 1
    add_job_function: Callable

    @classmethod
    def setUpTestData(cls) -> None:
        """
        Sets up tests data.

        Fixture import because skill object should be created during test
        and not during initial imports.
        """
        from jobs.tests.jobs_fixtures import add_job_object
        cls.add_job_function = add_job_object

    def setUp(self) -> None:
        """
        Sets up test data before every test.

        Added job object in test database.
        """
        self.add_job_function(id=self.DETAILS_PAGE_JOB_ID)

    def test_index_view_user_not_logged_in(self):
        """
        Tests if a view returns a page for a not logged user.
        """
        url: str = reverse("jobs:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/index.html")

    def test_search_view_user_not_logged_in(self):
        """
        Tests if a view returns a page for a not logged user.
        """
        url: str = reverse("jobs:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/search.html")

    def test_details_view_user_not_logged_in(self):
        """
        Tests if a view returns a page for a not logged user.
        """
        url: str = reverse("jobs:job_detail", args=[self.DETAILS_PAGE_JOB_ID])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/details.html")
