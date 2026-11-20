# Path Sum

**LeetCode:** [Path Sum](https://leetcode.com/problems/path-sum/)  
**Implementation:** recursive DFS in Python — [`solution.py`](./solution.py)

## 1. Problem

Determine whether a binary tree contains a **root-to-leaf** path whose node values add up to `targetSum`. The path must end at a leaf; reaching the target at an internal node is not enough.

## 2. Approach

The solution uses recursive DFS and carries the **remaining** sum down the current path. Instead of adding values along the path and comparing with `targetSum` at the end, each call subtracts the current node's value from `targetSum` and passes the remainder to its children.

1. If the node is `None`, this branch cannot contain a valid path, so return `False`.
2. Subtract `root.val` from `targetSum`.
3. If the node is a leaf, return whether the remainder is exactly `0`.
4. Otherwise, check the left subtree and the right subtree with the new remainder. One valid branch is enough, so the results are combined with `or`.

```python
def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
    if not root:
        return False

    targetSum -= root.val                      # remaining sum after this node

    if not root.left and not root.right:       # leaf: the path ends here
        return targetSum == 0

    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
```

Reassigning `targetSum` inside the function is safe: integers are immutable in Python, so each recursive call has its own local value, and the two child calls both receive the same remainder for this node.

### Trace example

Use `root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]` and `targetSum = 22`:

```text
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
```

DFS explores the left side first. The first leaf it reaches is `7`:

| Node | Remaining before | Remaining after | Leaf? | Result |
|---:|---:|---:|---|---|
| 5 | 22 | 17 | no | go left |
| 4 | 17 | 13 | no | go left (right child is `None`) |
| 11 | 13 | 2 | no | go left |
| 7 | 2 | −5 | yes | `False` → try the right child of `11` |
| 2 | 2 | 0 | yes | **`True`** |

The path `5 -> 4 -> 11 -> 2` gives `22`, so the function returns `True`. Because of short-circuit evaluation of `or`, the right subtree of the root (rooted at `8`) is never explored.

### Challenges and testing

The key condition is that the target must be reached **at a leaf**. A solution that returns `True` as soon as the remaining sum becomes `0` can wrongly accept a path that stops at an internal node. For example, in `root = [1, 2]` with `targetSum = 1`, the root alone gives `1`, but the root is not a leaf, so the correct answer is `False`.

Another subtle case is a node with only one child. The missing child returns `False`, which is correct: an empty branch is not a path to a leaf, so only the existing child can produce `True`.

Cases worth checking:

- empty tree with `targetSum = 0` → `False` (there is no root-to-leaf path at all);
- single node equal to the target, e.g. `[1]`, `1` → `True`;
- single node not equal to the target → `False`;
- `[1, 2]`, `targetSum = 1` → `False` (internal node matches, but it is not a leaf);
- negative values, e.g. `[-2, null, -3]`, `targetSum = -5` → `True`.

Negative values matter because a partial sum that has already "passed" the target can still come back to it, so it is not safe to stop exploring early.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

In the worst case (no valid path), the function is called once for every node and does constant work per call. If a valid path is found, `or` stops the search early, but the worst case is still linear.

**Auxiliary Space Complexity: `O(h)`**

The recursion follows one root-to-leaf path at a time, so the stack depth is at most the tree height `h`. That is `O(log n)` for a balanced tree and `O(n)` for a skewed tree.

## 4. Reflection / Improvement

An iterative DFS can store pairs `(node, remaining_sum)` on an explicit stack. It keeps `O(n)` time and avoids Python's recursion-depth limit, which could be reached by a skewed tree with the maximum of 5000 nodes. A BFS version with a queue of the same pairs also works and uses `O(w)` space, where `w` is the maximum width.

The recursive version is the clearest one because the code directly mirrors the definition: "a path exists from this node if it exists from one of its children with the reduced target". The early exit through `or` is already the main practical optimization; no algorithm can be asymptotically faster in general, because the valid path (or the proof that none exists) may require checking every node.
