from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        file_jobs = csv.DictReader(file)
        return list(file_jobs)

