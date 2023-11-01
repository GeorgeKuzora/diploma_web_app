"""
Test module for jobs app models.

Tests should be run from project root.

Examples:
    # For running a test use following command
    python web_app/manage.py test
"""
from django.db.models import QuerySet
from django.test import TestCase
from skills.models import Skill
from companies.models import Company, Address
from jobs.models import Job


class JobTests(TestCase):
    """
    Tests for Job model.
    """
    def test_create_job_with_all_fields(self) -> None:
        """
        Test if job object is created using Job model

        Creates a new job object, fetches all objects from database.
        Checks if number of objects is exactly 1.
        """
        from jobs.tests.jobs_fixtures import add_job_object
        add_job_object()
        queried_job: QuerySet[Job] = Job.objects.all()
        self.assertEqual(len(queried_job), 1)
