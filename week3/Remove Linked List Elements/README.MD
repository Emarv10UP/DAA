### 1. Problem

Remove all nodes from a singly linked list that contain a specific target value (`val`).

### 2. Approach

* **How it works:** We use a "dummy" node (`a`) placed right before the head. This handles edge cases where the head itself needs to be removed. A pointer (`b`) traverses the list; if the next node has the target value, we skip it by changing pointer links (`b.next = b.next.next`). Otherwise, we move forward normally (`b = b.next`).
* **Tracing Example (`1 -> 2 -> 6 -> 3`, target `6`):**
* Dummy node `a` points to `1`. `b` starts at `a`.
* `b` checks `1` and `2` (no match, moves forward).
* `b` sees the next node is `6` (matches!). It bypasses `6` by linking directly to `3`.
* Returns `a.next` (the cleaned list `1 -> 2 -> 3`).


* **Challenges:** Without a dummy node, removing the head node requires tedious edge-case handling. Using a dummy node treats the head like any other node, keeping the code clean and bug-free.

### 3. Time & Space Complexity

* **Time Complexity:** O(n) — We traverse the linked list of length $n$ at most once.
* **Space Complexity:** O(1) — Only a couple of pointer variables are used, requiring no extra memory.

### 4. Reflection / Improvement

* **More efficient approach?** The current solution is already optimal.
* **What could be changed?** It achieves the best possible **O(n)** time and **O(1)** space complexity, so no changes are needed for optimization.
