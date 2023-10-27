"""
Test module for skills app models.

Tests should be run from project root.

Examples:
    # For running a test use following command
    python web_app/manage.py test
"""
from django.db.models import QuerySet
from django.test import TestCase
from django.db.utils import IntegrityError

from skills.models import Skill
from skills.tests.fixtures import (add_skill_object,
                                   DEFAULT_SKILL_NAME,
                                   DEFAULT_SKILL_DESC)


class SkillModelTests(TestCase):
    """
    Tests for Skill model
    """
    def test_create_skill_with_all_fields(self):
        """
        Tests if skill is created using Skill model.

        Creates a new skill object, fetches all objects from database.
        Checks if number of objects is exactly 1, checks if object's fields
        have proper values.
        """
        add_skill_object()
        queried_skills: QuerySet[Skill] = Skill.objects.all()
        self.assertEqual(len(queried_skills), 1)
        self.assertEqual(queried_skills[0].skill_name, DEFAULT_SKILL_NAME)
        self.assertEqual(
            queried_skills[0].skill_description, DEFAULT_SKILL_DESC
        )

    def test_not_unique_skill_raises_exeption(self):
        """
        Tests if adding a not unique skill raises a IntegrityError.

        Creates a new skill object. Checks if creation of an object with
        the same values raises an IntegrityError.
        """
        add_skill_object()
        skill = Skill(
            skill_name=DEFAULT_SKILL_NAME, skill_description=DEFAULT_SKILL_DESC
        )
        self.assertRaises(IntegrityError, skill.save)
