from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        file_jobs = csv.DictReader(file)
        list_jobs = list(file_jobs)
        return list_jobs

