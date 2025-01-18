from search_algorhitms import kmp_search, boyer_moore_search, rabin_karp_search
from helpers import download_text, measure_time

url1 = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
url2 = "https://drive.google.com/uc?id=18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"

text1 = download_text(url1)
text2 = download_text(url2)

existing_substring = "структури даних"
non_existing_substring = "xnotfoundsubstringx" 

# Функція для заміру часу виконання операцій пошуку
def benchmark_searching_algorithms():
    algorithms = {
        "Кнут-Морріс-Пратт": kmp_search,
        "Боєр-Мур": boyer_moore_search,
        "Рабін-Карп": rabin_karp_search,
    }

    for text_num, text in enumerate([text1, text2], start=1):
        print(f"\nТекст {text_num}:")
        print("-" * 50)
        print("{:<20} {:<15} {:<15}".format("Алгоритм", "Існуючий", "Неіснуючий"))
        print("-" * 50)

        for name, algorithm in algorithms.items():
            time_existing = measure_time(algorithm, text, existing_substring)
            time_non_existing = measure_time(algorithm, text, non_existing_substring)

            print("{:<20} {:<15.6f} {:<15.6f}".format(name, time_existing, time_non_existing))

        print("-" * 50)


benchmark_searching_algorithms()