import json, csv

def get_users(json_file):
    clear_users = []
    with open(json_file, "r") as users_file:
        users = json.load(users_file)
    for user in users:
        clear_users.append(
            {
                "name" : user.get("name"),
                "gender" : user.get("gender"),
                "address" : user.get("address"),
                "age" : user.get("age")
            }
        )
    return clear_users

def get_books(csv_file):
    clear_books = []
    with open(csv_file, "r") as books_file:
        books = csv.DictReader(books_file, delimiter=",")
        for book in books:
            clear_books.append(
                {
                    "title" : dict(book).get("Title"),
                    "author" : dict(book).get("Author"),
                    "pages" : int(dict(book).get("Pages")),
                    "genre" : dict(book).get("Genre")
                }
            )
    return clear_books

def make_reference(users, books):
    count_users = len(users)
    count_books = len(books)
    min_count_books = count_books // count_users

    def first_books_gen(books_list, num_bks):
        for i in range(0, len(books_list), num_bks):
            yield books_list[i:i+num_bks]
    
    sorted_books = list(first_books_gen(books, min_count_books))

    for i, user in enumerate(users):
        user.update({"books" : sorted_books[i]})

    last_books = []
    for book in sorted_books[count_users:]:
        last_books.extend(book)
    
    for user in users[:len(last_books)]:
        user["books"].append(last_books.pop())
    
    return users

def create_result(reference):
    with open("result.json", "w") as result_file:
        json.dump(reference, result_file, indent=4)

    

users = get_users("users.json")
books = get_books("books.csv")
result = make_reference(users, books)
create_result(result)
