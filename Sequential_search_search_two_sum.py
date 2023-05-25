def sequential_search_two_Sum(data, target):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i] + data[j] == target:
                return data[i], data[j]
        return None
    
my_list = [2, 7, 11, 15, 5, 9]
target_sum = 15
result = sequential_search_two_Sum(my_list, target_sum)
if result:
    print(f"Dua Elemen yang jumlahnyya sama dengan {target_sum} adalah {result[0]} dan {result[1]} ")
else:
    print("Tidak ada dua Elemen yang jumlahnya sama dengan Target")