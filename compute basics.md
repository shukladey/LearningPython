## Time Complexity
Time complexity describes how the runtime of your code grows as input size grows.


👉 It’s not about how fast your laptop is

👉 It’s about how the algorithm scales

We use Big-O notation (O(…)) to describe this growth.

Think of it like this

If input size = n:
- n = 10 → small data
- n = 1,000,000 → big data


Side Tip:
- Good code grows slowly
- Bad code grows very fast


| Big-O      | Meaning           | Example             | Comment             | Sample Code             |
| ---------- | ----------------- | ------------------- | ------------------- | ------------------- |
| O(1)       | Constant time     | Accessing list item | Runtime does not change with input size | `return arr[0]` # Even if arr has 10 or 1 million elements → same time |
| O(n)       | Linear time       | Single loop         | Runtime grows linearly with input size | `for item in arr: print(item)` If n = 10 → 10 operations; If n = 1000 → 1000 operations |
| O(n²)      | Quadratic time    | Nested loops        | Nested loops = danger sign | `for i in arr: for j in arr: print(i, j)` # print pairs |
| O(log n)   | Logarithmic       | Binary search       | Each step cuts the problem in half | `left, right = 0, len(arr) - 1 while left <= right: mid = (left + right) // 2 if arr[mid] == target: return True elif arr[mid] < target: left = mid + 1 else: right = mid - 1 return False` # If n = 1,000,000 → ~20 steps |
| O(n log n) | Efficient sorting | `sorted()`          | Used by Python’s built-in sorting (Timsort) | `sorted_list = sorted(arr)` # Much faster than naive sorting for large inputs |
