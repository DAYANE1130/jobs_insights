from src.counter import count_ocurrences

def test_counter():
    assert count_ocurrences('src/jobs.csv', 'Python')
    # print(count_ocurrences('src/jobs.csv', 'Python'))
    # return count_ocurrences('src/jobs.csv', 'Python')


