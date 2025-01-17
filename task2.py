def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
            
        # Якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # Якщо x менше за значення посередині списку, ігноруємо праву половину та оновлюємо верхню межу
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # Інакше x присутній на позиції і сам же являється верхньою межею
        else:
            return (iterations, arr[mid])  

    # Якщо елемент не знайдено, повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)


sorted_array = [1.1, 2.3, 3.5, 4.7, 5.9, 6.0, 7.2]
target_value = 4.0

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")