import csv
from csv import DictReader
import json
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from files import RESULT_FILE_PATH


def get_users_amount():
    with open(JSON_FILE_PATH, "r") as file:
        users = json.load(file)
        return len(users)


def get_books_amount():
    with open(CSV_FILE_PATH, "r") as file:
        books_data = csv.reader(file)
        amount_books = -1
        for i in books_data:
            amount_books += 1
        return amount_books


def get_book_title(row):
    if row["Title"] != "":
        return row["Title"]
    else:
        return None


def get_book_author(row):
    if row["Author"] != "":
        return row["Author"]
    else:
        return None


def get_book_pages(row):
    if row["Pages"] != "":
        return int(row["Pages"])
    else:
        return None


def get_book_genre(row):
    if row["Genre"] != "":
        return row["Genre"]
    else:
        return None


def get_user_books_by_index(index):
    books = []
    for i in range(index, get_books_amount() + 1, get_users_amount()):
        with open(CSV_FILE_PATH, "r") as file:
            csv_reader = DictReader(file)
            count_row = 0
            for row in csv_reader:
                if count_row == i:
                    books.append({"Title": get_book_title(row), "Author": get_book_author(row),
                                  "Pages": get_book_pages(row), "Genre": get_book_genre(row)})
                    break
                else:
                    count_row += 1
    return books


for_dump = []
with open(JSON_FILE_PATH, "r") as file:
    users = json.load(file)
    for index in range(get_users_amount()):
        one_user_dict = {'name': users[index]["name"], 'gender': users[index]["gender"],
                         'address': users[index]["address"], 'age': users[index]["age"],
                         'books': get_user_books_by_index(index)}

        for_dump.append(one_user_dict)

with open(RESULT_FILE_PATH, 'w') as f:
    json.dump(for_dump, f, indent=4)
