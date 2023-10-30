"""
Test fixtures for jobs app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .jobs_fixtures import <function_name>
"""
from typing import Any
from datetime import date
from companies.models import Address, Company
from companies.tests.address_fixtures import add_address_object
from companies.tests.company_fixtures import add_company_object
# from skills.tests.fixtures import add_skill_object
from skills.models import Skill
from jobs.models import Job


DEFAULT_ADDRESS: Address = add_address_object()
DEFAULT_COMPANY: Company = add_company_object()
DEFAULT_SKILL: Skill = Skill.objects.create(skill_name="python",
                                            skill_description="python")
DEFAULT_TEST_JOB: dict[str, Any] = {
    "id": 1,
    "job_name": "Python developer",
    "job_desc": "Developing in python",
    "skills": [
        DEFAULT_SKILL,
    ],
    "min_salary": 50000,
    "max_salary": 100000,
    "company": DEFAULT_COMPANY,
    "pub_date": date.fromisoformat("2023-10-30"),
    "address": DEFAULT_ADDRESS,
    "is_archived": False,
    "required_exp": "",
}


def add_job_object(
    id: int = DEFAULT_TEST_JOB["id"],
    job_name: str = DEFAULT_TEST_JOB["job_name"],
    job_desc: str = DEFAULT_TEST_JOB["job_desc"],
    skills: list[Skill] = DEFAULT_TEST_JOB["skills"],
    min_salary: int = DEFAULT_TEST_JOB["min_salary"],
    max_salary: int = DEFAULT_TEST_JOB["max_salary"],
    company: Company = DEFAULT_TEST_JOB["company"],
    pub_date: date = DEFAULT_TEST_JOB["pub_date"],
    address: str = DEFAULT_TEST_JOB["address"],
    is_archived: bool = DEFAULT_TEST_JOB["is_archived"],
    required_exp: str = DEFAULT_TEST_JOB["required_exp"],
) -> Job:
    """
    Creates and saves job object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        id: Job id.
            Default value: 1
        job_name: Job title.
            Default value: 'Python developer'
        job_desc: Job description.
            Default value: 'Developing in python.'
        skills: Job skills.
            Default value: Default skills
        min_salary: Job minimum salary.
            Default value: 50000
        max_salary: Job maximum salary.
            Default value: 100000
        company: Job company.
            Default value: Default company
        pub_date: Job publication date.
            Default value: 100000
        address: Job address.
            Default value: Default address
        is_archived: Job archived flag.
            Default value: False
        required_exp: Experience required for a job.
            Default value: ""

    Example:
        # Call this function like this
        add_job_object(<args>)
    """
    job: Job = Job(
        id=id,
        job_name=job_name,
        job_description=job_desc,
        min_salary=min_salary,
        max_salary=max_salary,
        pub_date=pub_date,
        is_archived=is_archived,
        required_experience=required_exp
    )
    job.save()
    job.company = company
    job.address = address
    job.skills.add(*skills)
    return Job.objects.get(id=id)
