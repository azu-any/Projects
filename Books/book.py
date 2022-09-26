def main():
    books = [] 
    with open("Desktop/books.txt", "r") as file:
        for line in file:
            books.append(line.rstrip())
    
    while True:
        try:
            print("What would you like to do?")
            print("0: Exit")
            print("1: See the whole list of books")
            print("2: Add a book")
            dec = int(input("Option: "))
            if dec == 1:
                bprint(books)
                continue
            elif dec == 2:
                add(books)
                continue
            elif dec == 0:
                print("Goodbye")
                break
            else:
                print("Choose 1 or 2")
                continue
        except ValueError:
            print("Value not accepted")
            continue


def bprint(books):
    for item in sorted(books):
        book, author = item.split("/")
        print(f"{book} by {author}")

def add(books):
    with open("Desktop/books.txt", "a") as file:
        book = input("What's the name? ").strip()
        author = input("Who's the author? ").strip()
        file.write(f"{book}/{author}\n")
        print("Item added")

main()