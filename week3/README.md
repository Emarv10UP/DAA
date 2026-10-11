1. Problem
Determine if a singly linked list reads the same forwards and backwards.

2. Approach
How it works: Traverse the linked list using a pointer, extract each node's value, and store them in a Python list. Then, check if the list equals its own reverse (b == b[::-1]).

Tracing Example (1 -> 2 -> 2 -> 1):

Collect values into b = [1, 2, 2, 1].

Compare b with its reverse [1, 2, 2, 1] -> Match (True).

Challenges: Reversing the linked list in-place destroys the original structure, and recursion can be messy. Storing values in an array is simpler and cleaner, avoiding pointer manipulation bugs.

3. Time & Space Complexity
Time Complexity: O(n) — We traverse the list once and compare the array in linear time.

Space Complexity: O(n) — Extra memory is used to store node values in the list.

4. Reflection / Improvement
More efficient approach? Yes, we can achieve O(1) space complexity.

What to change? Use fast and slow pointers to find the middle, reverse the second half of the list in-place, and compare it with the first half.
