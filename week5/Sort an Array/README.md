# Problem 1: Sort an Array

## 1. Problem
Given an array of integers `nums`, we need to sort it in ascending order in $O(N \log N)$ time without relying on built-in sorting functions.

## 2. Approach
I went with **Merge Sort** because it guarantees $O(N \log N)$ time even in the worst case. To keep memory usage under control, I created a single temporary array `temp` at the start instead of creating new arrays on every recursive call.

1. **Divide:** Find the middle index `mid = (left + right) // 2`.
2. **Conquer:** Recursively split and sort the left half `[left...mid]` and right half `[mid+1...right]`.
3. **Merge:** Compare elements from both halves, place them in order inside `temp`, and copy the sorted values back into `nums`. *(Added a small check: if `nums[mid] <= nums[mid+1]`, the halves are already in order, so we can skip the merge step altogether).*

### Tracing Example (`nums = [5, 2, 3, 1]`)
* **Splitting:** `[5, 2, 3, 1]` gets divided into `[5, 2]` and `[3, 1]`, then down to single elements `[5]`, `[2]`, `[3]`, `[1]`.
* **Merging halves:** 
  * Merge `[5]` & `[2]` $\rightarrow$ `[2, 5]`
  * Merge `[3]` & `[1]` $\rightarrow$ `[1, 3]`
* **Final Merge (`[2, 5]` + `[1, 3]`):**
  * Compare $2$ and $1$ $\rightarrow$ pick $1$
  * Compare $2$ and $3$ $\rightarrow$ pick $2$
  * Compare $5$ and $3$ $\rightarrow$ pick $3$
  * Take remaining $5$ $\rightarrow$ Result: `[1, 2, 3, 5]`

### Challenges I Ran Into
My first attempt used Python list slicing (like `nums[:mid]`), which ended up allocating new sublists everywhere. This blew up the memory usage and hit a **Memory Limit Exceeded** on LeetCode. I fixed this by passing boundary indices (`left`, `right`) and reusing a single pre-allocated `temp` list.

## 3. Complexity Analysis
* **Time Complexity:** $O(N \log N)$ — The array is split in half $\log N$ times, and merging elements across each level takes $O(N)$ linear time.
* **Space Complexity:** $O(N)$ — Requires $O(N)$ memory for the shared `temp` buffer plus $O(\log N)$ space on the call stack for recursion.

## 4. Reflection / Improvement
* **Can it be improved?** Yes. We could use **Heap Sort** to get $O(1)$ auxiliary space while keeping $O(N \log N)$ time. An iterative (bottom-up) merge sort would also eliminate the recursion stack overhead.
