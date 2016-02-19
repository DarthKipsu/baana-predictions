import data.data_fetcher as fetch

def write_to_file(path, value):
    with open(path, 'a') as f:
        f.write("%s \n" % value)

write_to_file('data/clean/actual', fetch.cyclist_count())

