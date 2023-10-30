"""
Test fixtures for skill app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .fixtures import <function_name>
"""
from skills.models import Skill

DEFAULT_SKILL_ID: int = 1
DEFAULT_SKILL_NAME: str = "python"
DEFAULT_SKILL_DESC: str = "Programming language Python"


def add_skill_object(id: int = DEFAULT_SKILL_ID,
                     skill_name: str = DEFAULT_SKILL_NAME,
                     skill_description: str = DEFAULT_SKILL_DESC) -> Skill:
    """
    Creates and saves skill object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        id: Id of the skill.
            Default value 1
        skill_name: Name of the skill.
            Default value 'python'
        skill_description: Description of the skill.
            Default value 'Programming language Python'

    Example:
        # Call this function like this
        add_skill_object('ruby', 'Ruby programming language')
    """
    skill: Skill = Skill(id=id,
                         skill_name=skill_name,
                         skill_description=skill_description)
    skill.save()
    return Skill.objects.get(skill_name=skill_name)
