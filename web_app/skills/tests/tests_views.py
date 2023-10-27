"""
Tests for skill app views.

Tests should be run from project root.

Examples:
    # For running a test use following command
    python web_app/manage.py test
"""
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from skills.views import index, detail
from skills.tests.fixtures import add_skill_object


class TestViews(TestCase):
    """
    Tests for all views in skills app.
    """

    NUMBER_OF_SKILL_OBJECTS = 2

    def test_index_view_with_no_skills(self):
        """
        Tests if a view returns a page if no skill objects are available.

        Requests a skill_list page without. Checks if response status is 200.
        Checks if skills/index.html template is used. Checks if the page has
        a proper content.
        """
        url: str = reverse("skills:skill_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills/index.html")
        self.assertContains(response, "No skills are available.")

    def test_index_view_with_skills(self):
        """
        Tests if a view returns a page if skills objects are available.

        Requests a skill_list page without. Checks if response status is 200.
        Checks if skills/index.html template is used. Checks if the page has
        a proper content.
        """
        add_skill_object()
        add_skill_object("ruby", "Ruby language")
        url: str = reverse("skills:skill_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills/index.html")
        self.assertEqual(len(response.context["skill_list"]),
                         self.NUMBER_OF_SKILL_OBJECTS)
