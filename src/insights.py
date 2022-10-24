from curses.ascii import isdigit
from src.jobs import read


def get_unique_job_types(path):
    list_job = read(path)
    jobs_types = set()
    for job_type in list_job:
        jobs_types.add(job_type["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    list_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_job.append(job)
    return list_job


def get_unique_industries(path):
    list_job = read(path)
    list_industry = set()
    for industry in list_job:
        if industry["industry"] != "":
            list_industry.add(industry["industry"])
    return list_industry


def filter_by_industry(jobs, industry):
    list_job = []
    for job in jobs:
        if job["industry"] == industry:
            list_job.append(job)
    return list_job


def get_max_salary(path):
    list_job = read(path)
    better_salary = set()
    for salary in list_job:
        if salary["max_salary"] != "" and salary["max_salary"].isdigit():
            better_salary.add(int(salary["max_salary"]))
    return max(better_salary)


def get_min_salary(path):
    list_job = read(path)
    bad_salary = set()
    for salary in list_job:
        if salary["min_salary"] != "" and salary["min_salary"].isdigit():
            bad_salary.add(int(salary["min_salary"]))
    return min(bad_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job.get("min_salary")) is not int
        or type(job.get("max_salary")) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
