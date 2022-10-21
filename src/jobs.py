from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open("src/jobs.csv", 'r') as file:
        file_jobs = csv.DictReader(file)
    return [file_jobs]