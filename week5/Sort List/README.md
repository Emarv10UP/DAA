# Problem 2: Sort List

## 1. Problem
Given the `head` of a singly-linked list, sort its nodes in ascending order in $O(N \log N)$ time complexity.

## 2. Approach
Since we can't easily jump to random indices in a linked list, I adapted **Merge Sort** using the **Fast & Slow Pointer** trick to find the middle node.

1. **Base Case:** If the list is empty or has only one node, it is already sorted.
2. **Find Middle & Split:** Use a `slow` pointer (moves 1 step) and a `fast` pointer (moves 2 steps). When `fast` reaches the end, `slow` is at the middle. Cut the list into two halves by setting `slow.next = None`.
3. **Recursion:** Recursively sort both sublists.
4. **Merge:** Merge the two sorted linked lists back together using a dummy head node and re-linking pointer references.

### Tracing Example (`head = [4, 2, 1, 3]`)
* **Split:** `slow` stops at node `2`. Cut the link $\rightarrow$ Left half: `4 -> 2`, Right half: `1 -> 3`.
* **Recursion:** 
  * `4 -> 2` breaks into `4` and `2`, then merges into `2 -> 4`.
  * `1 -> 3` breaks into `1` and `3`, then merges into `1 -> 3`.
* **Merge (`2 -> 4` and `1 -> 3`):**
  * Compare $2$ vs $1$ $\rightarrow$ attach $1$
  * Compare $2$ vs $3$ $\rightarrow$ attach $2$
  * Compare $4$ vs $3$ $\rightarrow$ attach $3$
  * Attach remaining node $4$ $\rightarrow$ Final List: `1 -> 2 -> 3 -> 4`

### Challenges I Ran Into
I initially started `fast = head` when finding the midpoint. On even-length lists, this caused `slow` to stop one node too far, causing an infinite recursion loop and a **Time Limit Exceeded / Stack Overflow**. Setting `fast = head.next` fixed it so `slow` stops right at the end of the first half.

## 3. Complexity Analysis
* **Time Complexity:** $O(N \log N)$ — Finding the middle and merging nodes takes $O(N)$ operations per level across $\log N$ recursion levels.
* **Space Complexity:** $O(\log N)$ — Pointers are rearranged in-place without creating new nodes ($O(1)$ memory), but the recursive call stack takes $O(\log N)$ space.

## 4. Reflection / Improvement
* **Can it be improved?** Yes. We can optimize the space complexity to a strict $O(1)$ by writing an **Iterative (Bottom-Up) Merge Sort**. Instead of recursion, we would merge sublists in loops of increasing sizes ($1, 2, 4, 8, \dots$).
