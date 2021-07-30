import json
from pprint import pprint
import hashlib


class Countries:

    def __init__(self, countries):
        self.countries = countries
        self.url = 'https://en.wikipedia.org/wiki/'

    def get_country(self, index):
        return self.countries[index]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.countries):
            raise StopIteration
        country = self.get_country(self.index)["name"]["common"]
        return {country: self.url + country}


with open("countries.json", "r") as read_file:
    data = json.load(read_file)
    # countries = [country for country in Countries(data)]


def generator(file):
    with open(file, "r") as f:
        for line in f:
            hash_str = hashlib.md5(f.readline().strip().encode())
            yield hash_str.hexdigest()


for hash_string in generator("countries.json"):
    pprint(hash_string)
