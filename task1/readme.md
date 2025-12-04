# Sorting Algorithm Comparison

We compared three sorting algorithms: Insertion Sort, Merge Sort, and Python's built-in Timsort.

## Test Results
- Small arrays (n=100): all algorithms fast, Insertion Sort acceptable.
- Medium arrays (n=1000): Insertion Sort slows down significantly, Merge Sort and Timsort fast.
- Large arrays (n=10000): Insertion Sort very slow, Merge Sort slower than Timsort, Timsort fastest.

## Conclusions
- Insertion Sort has O(n²) complexity, inefficient for large arrays.
- Merge Sort has O(n log n) complexity, stable and predictable.
- Timsort combines Insertion Sort and Merge Sort: handles small runs efficiently and large arrays with merge, making it the most practical choice.
- Python's built-in sorting functions should be preferred in real-world projects due to their speed and reliability.
