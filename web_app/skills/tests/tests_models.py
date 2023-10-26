from django.test import TestCase
from django.db.utils import IntegrityError

from skills.models import Skill


class SkillModelTests(TestCase):

    def test_create_skill_with_all_fields(self):
        skill_name = "python"
        skill_description = "Programming language Python"
        skill = Skill(
            skill_name=skill_name, skill_description=skill_description
        )
        skill.save()
        queried_skills = Skill.objects.all()
        self.assertEqual(len(queried_skills), 1)
        self.assertEqual(queried_skills[0].skill_name, skill_name)
        self.assertEqual(
            queried_skills[0].skill_description, skill_description
        )

    def test_not_unique_skill_raises_exeption(self):
        skill_name = "python"
        skill_description = "Programming language Python"
        skill = Skill(
            skill_name=skill_name, skill_description=skill_description
        )
        skill.save()
        skill = Skill(
            skill_name=skill_name, skill_description=skill_description
        )
        self.assertRaises(IntegrityError, skill.save)
