def sequential_search(phone_book, name):
    for i in range(len(phone_book)):
        if phone_book[i]['name'] == name:
            return phone_book[i]['phone_number'] 
    return None  

phone_book = [
    {'name': 'John Doe', 'phone_number': '081234567890'},
    {'name': 'Jane Smith', 'phone_number': '089876543210'},
    {'name': 'Michael Johnson', 'phone_number': '087811223344'},
    {'name': 'Emily Davis', 'phone_number': '082122232425'}
]

target_name = 'Jane Smith'

result = sequential_search(phone_book, target_name)

if result is not None:
    print("Nomor telepon", target_name, "adalah", result)
else:
    print("Nama", target_name, "tidak ditemukan dalam buku telepon.")
