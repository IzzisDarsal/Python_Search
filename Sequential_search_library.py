def is_similiar(title1, title2):
    title1 = title1.lower()
    title2 - title2.lower()

    if title1[0] == title2[0]:
        return True
    
    return False


def sequential_search(books, book_title):
    for book in books:
        if is_similiar(book['title'], book_title):
            return book['shelf']
        
    return "Buku titak ditemukan"

books = [
    {'title': 'Python Programming', 'shelf': 'A1'},
    {'title': 'Data Stuctures and Algorithms', 'shelf': 'B2'},
    {'title': 'Introduction to  Machine Learning', 'shelf': 'C3'},
    {'title': 'Database Management System', 'shelf': 'D4'},
]

book_title = input("Masukan judul buku yang ingin dicari: ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)