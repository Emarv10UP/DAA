### 1. Problem

Remove all duplicate elements from a sorted singly linked list so that each unique element appears only once.

### 2. Approach

* **How it works:** Since the linked list is already sorted, all duplicate values will appear consecutively. We use a pointer (`a`) to traverse the list, comparing the current node's value (`a.val`) with the next node's value (`a.next.val`). If they are equal, we skip the duplicate by bypassing it (`a.next = a.next.next`). If they are different, we simply move to the next node (`a = a.next`).
* **Tracing Example (`1 -> 1 -> 2`):**
* `a` starts at the first `1`. It sees the next node is also `1` (duplicate!). It updates pointer to skip it: `1 -> 2`.
* `a` moves forward to `2`. The next node is `None`, so the loop ends.
* Returns `head` (`1 -> 2`).


* **Challenges:** Initially, I considered using a hash set to track seen elements. However, since the list is sorted, a hash set would waste **O(n)** space. Leveraging the sorted order allows us to compare adjacent elements directly in-place without extra memory.

### 3. Time & Space Complexity

* **Time Complexity:** O(n) — We traverse each node of the linked list of length $n$ exactly once.
* **Space Complexity:** O(1) — We modify the list in-place using only a single pointer variable, requiring no extra memory.

### 4. Reflection / Improvement

* **More efficient approach?** The current solution is already optimal for a sorted list.
* **What could be changed?** It achieves the best possible **O(n)** time and **O(1)** space complexity, so no further optimization is needed.
