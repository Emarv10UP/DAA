# Maximum Depth of Binary Tree

**LeetCode:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)  
**Implementation:** iterative BFS (level-order traversal) in Python — [`solution.py`](./solution.py)

## 1. Problem

Given the root of a binary tree, return its maximum depth: the number of nodes on the longest path from the root down to the farthest leaf. An empty tree has depth `0`.

## 2. Approach

The solution uses breadth-first search (BFS) and processes the tree **level by level**. The maximum depth is simply the number of levels in the tree.

1. If the tree is empty, return `0`.
2. Put the root into a queue (`collections.deque`) and set `depth = 0`.
3. While the queue is not empty:
   - remember how many nodes are in the queue right now — this is exactly the number of nodes on the current level;
   - remove that many nodes from the front of the queue and add their existing children to the back;
   - after the whole level has been processed, increase `depth` by one.
4. When the queue becomes empty, every level has been counted, so return `depth`.

```python
def maxDepth(self, root: TreeNode | None) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        for _ in range(len(queue)):      # process exactly one level
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1

    return depth
```

The key detail is `range(len(queue))`. The length is evaluated **once**, before the inner loop starts, so children that are appended during the loop belong to the next level and are not processed in the current iteration.

### Trace example

For the tree `root = [3, 9, 20, null, null, 15, 7]`:

```text
       3
      / \
     9   20
        /  \
       15   7
```

| Level | Queue before the level | Nodes processed | Queue after the level | `depth` |
|---:|---|---|---|---:|
| 1 | `[3]` | `3` | `[9, 20]` | 1 |
| 2 | `[9, 20]` | `9`, `20` | `[15, 7]` | 2 |
| 3 | `[15, 7]` | `15`, `7` | `[]` | 3 |

The queue is empty, so the answer is `3`.

### Challenges and testing

The main challenge in a level-order solution is keeping levels separate. If `depth` were increased for every popped node instead of once per level, the function would return the number of nodes rather than the number of levels. Fixing the level size with `len(queue)` before the inner loop solves this.

A second common mistake is mixing up **nodes** and **edges**. This problem counts nodes, so a single-node tree has depth `1`, not `0`; this is why `depth` is increased after the root's level is processed.

Cases worth checking:

- empty tree `[]` → `0` (handled by the early return);
- single node `[1]` → `1`;
- the balanced example above → `3`;
- a chain such as `[1, null, 2]` → `2`.

The chain confirms that the algorithm counts every level even when each level has only one node.

`deque` is used instead of a list because `deque.popleft()` is `O(1)`, while `list.pop(0)` is `O(n)`. On LeetCode `deque` is already imported; in a standalone file it needs `from collections import deque`.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Every node is added to the queue once and removed once. Each removal does a constant amount of work: checking two children and possibly appending them. Therefore, the total time is proportional to the number of nodes `n`.

**Auxiliary Space Complexity: `O(w)`**, where `w` is the maximum width of the tree (the largest number of nodes on one level).

At any moment, the queue contains at most one full level plus some children of that level, which is bounded by `O(w)`. For a skewed tree (a chain) `w = 1`, so the queue uses `O(1)` space. For a complete binary tree the last level contains about `n / 2` nodes, so the worst case is `O(n)`. The function returns a single integer, so there is no output list.

## 4. Reflection / Improvement

A recursive DFS solution is shorter:

```python
def maxDepth(self, root):
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

It also runs in `O(n)` time, but its recursion stack uses `O(h)` space, where `h` is the height. The two approaches are good in opposite cases: DFS uses little memory on wide, balanced trees, while BFS uses little memory on deep, narrow trees. BFS has the practical advantage that it does not depend on Python's recursion-depth limit, which matters for this problem because the tree can contain up to `10^4` nodes and a skewed tree of that size would exceed the default limit. Neither approach can beat `O(n)` time, because the deepest leaf can be anywhere and every node may need to be inspected.
