# DAA
# Week 6 - Binary Tree Problems

This folder contains solutions and reports for the ten assigned LeetCode problems on binary trees. Each problem has its own directory with the submitted code (`solution.py`) and a report (`README.md`) describing the problem, the approach, a trace example, edge cases, time and space complexity, and possible improvements.

All solutions are written in Python 3.

## Problem reports

| # | Problem | Approach | Time | Extra space |
|---:|---|---|---|---|
| 01 | [Binary Tree Inorder Traversal](./01-binary-tree-inorder-traversal/README.md) | Recursive DFS | `O(n)` | `O(h)` |
| 02 | [Maximum Depth of Binary Tree](./02-maximum-depth-of-binary-tree/README.md) | Iterative BFS, level by level | `O(n)` | `O(w)` |
| 03 | [Minimum Depth of Binary Tree](./03-minimum-depth-of-binary-tree/README.md) | Iterative BFS, stop at first leaf | `O(n)` | `O(w)` |
| 04 | [Path Sum](./04-path-sum/README.md) | Recursive DFS with remaining sum | `O(n)` | `O(h)` |
| 05 | [Binary Tree Preorder Traversal](./05-binary-tree-preorder-traversal/README.md) | Iterative DFS with a stack | `O(n)` | `O(h)` |
| 06 | [Binary Tree Postorder Traversal](./06-binary-tree-postorder-traversal/README.md) | Stack (root → right → left) + reverse | `O(n)` | `O(h)` |
| 07 | [Invert Binary Tree](./07-invert-binary-tree/README.md) | Recursive DFS, swap in place | `O(n)` | `O(h)` |
| 08 | [Binary Tree Paths](./08-binary-tree-paths/README.md) | Recursive DFS with backtracking | `O(n · h)` | `O(h)` |
| 09 | [Sum of Left Leaves](./09-sum-of-left-leaves/README.md) | Recursive DFS, parent checks left child | `O(n)` | `O(h)` |
| 10 | [Merge Two Binary Trees](./10-merge-two-binary-trees/README.md) | Recursive DFS on both trees | `O(min(n, m))` | `O(k + h)` |

Notation: `n` — number of nodes, `h` — height of the tree (`O(log n)` if balanced, `O(n)` if skewed), `w` — maximum width of a level, `k` — number of positions present in both trees (task 10). "Extra space" does not include the returned output list.

## Common ideas

- **DFS vs. BFS.** Recursive or stack-based DFS uses memory proportional to the height `h`; queue-based BFS uses memory proportional to the width `w`. BFS is natural for "level" questions (tasks 02 and 03), and it lets task 03 stop at the first leaf it finds.
- **Recursion vs. explicit stack.** Tasks 05 and 06 replace recursion with an explicit stack, which avoids Python's recursion-depth limit on very deep trees.
- **Leaf checks.** Tasks 03, 04, 08 and 09 depend on the exact definition of a leaf: a node with **no** left child **and** no right child.
