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
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
