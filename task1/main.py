import random
import timeit
from algorythms import merge_sort, insertion_sort, timsort

def main():
    # --- test data generation ---
    sizes = [100, 1000, 10000]  
    test_arrays = {n: [random.randint(0, 10000) for _ in range(n)] for n in sizes}

    results = {}
    
    for n, arr in test_arrays.items():
        arr_merge = arr.copy()
        arr_insertion = arr.copy()
        arr_timsort = arr.copy()

        # Merge sort
        t_merge = timeit.timeit(lambda: merge_sort(arr_merge), number=1)
        
        # Insertion sort
        t_insertion = timeit.timeit(lambda: insertion_sort(arr_insertion), number=1)
        
        # Timsort
        t_timsort = timeit.timeit(lambda: timsort(arr_timsort), number=1)

        results[n] = {
            "merge_sort": t_merge,
            "insertion_sort": t_insertion,
            "timsort": t_timsort
        }

    # --- print results ---
    for size, timing in results.items():
        print(f"\nArray size: {size}")
        for algo, t in timing.items():
            print(f"{algo}: {t:.6f} sec")

if __name__ == "__main__":
    main()
