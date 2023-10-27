"""
Test fixtures for skill app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .fixtures import <function_name>
"""
from skills.models import Skill

DEFAULT_SKILL_NAME: str = "python"
DEFAULT_SKILL_DESC: str = "Programming language Python"


def add_skill_object(skill_name: str = DEFAULT_SKILL_NAME,
                     skill_description: str = DEFAULT_SKILL_DESC):
    """
    Creates and saves skill object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        skill_name: Name of the skill.
            Default value 'python'
        skill_description: Description of the skill.
            Default value 'Programming language Python'

    Example:
        # Call this function like this
        add_skill_object('ruby', 'Ruby programming language')
    """
    skill: Skill = Skill(
        skill_name=skill_name, skill_description=skill_description
    )
    skill.save()
