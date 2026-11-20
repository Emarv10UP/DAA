# Sum of Left Leaves

**LeetCode:** [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)  
**Implementation:** recursive DFS (the parent checks its left child) in Python — [`solution.py`](./solution.py)

## 1. Problem

Return the sum of all **left leaves** in a binary tree. A left leaf is a node that is the **left child** of its parent **and** has no children of its own. A left child that has children is not counted, and a leaf that is a right child is not counted either.

## 2. Approach

A node cannot tell by itself whether it is a left child — only its parent knows that. Therefore, in this solution each node looks **one level down** at its own left child:

1. If the node is `None`, return `0`.
2. Look at the left child:
   - if it exists **and** is a leaf, add its value to `total`;
   - otherwise, recursively compute the sum of left leaves inside the left subtree (if the left child is `None`, this call simply returns `0`).
3. Recursively add the sum of left leaves inside the right subtree. The right child itself is never added directly, but its subtree can contain left leaves.
4. Return `total`.

```python
def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
    if not root:
        return 0

    total = 0

    if root.left and not root.left.left and not root.left.right:
        total += root.left.val                     # left child is a leaf: count it
    else:
        total += self.sumOfLeftLeaves(root.left)   # search inside the left subtree

    total += self.sumOfLeftLeaves(root.right)      # left leaves can be on the right side too

    return total
```

When the left child is a leaf, there is no recursive call into it: a leaf has no children, so its subtree cannot contain any other left leaves.

### Trace example

For `root = [3, 9, 20, null, null, 15, 7]`:

```text
       3
      / \
     9   20
        /  \
       15   7
```

- At node `3`: its left child `9` is a leaf, so add `9`. Then recurse into the right child `20`.
- At node `20`: its left child `15` is a leaf, so add `15`. Then recurse into the right child `7`.
- At node `7`: it has no children. Its left child is `None` (the recursive call returns `0`), and its right child is `None` (also `0`), so it returns `0`.

Node `7` is a leaf, but it is a **right** child, so it is never added; node `20` is a left-side ancestor of `15`, but it is a right child with children, so it is not added either.

The total is `9 + 15 = 24`.

### Challenges and testing

The main distinction is between a **left child** and a **left leaf**. Counting every left child would be wrong as soon as a left child has its own children. Here, the leaf check `not root.left.left and not root.left.right` happens before anything is added.

A second subtle case is the root. The root is nobody's left child, so even when the whole tree is a single node, the answer is `0`. In this solution this happens naturally: the root's value is never added directly — only values of left children are.

Cases worth checking:

- single node `[1]` → `0` (the root is not a left leaf);
- the example above → `24`;
- a left child that is not a leaf: `[1, 2, null, 3]` → `3` (node `2` is skipped, node `3` is counted);
- only a right leaf: `[1, null, 2]` → `0`;
- negative values, e.g. `[1, -4, 2]` → `-4`.

Negative values confirm that the algorithm adds the actual node values and does not assume that every contribution is positive.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Each node is reached by at most one recursive call, and each call does constant work: a few comparisons and additions. When the left child is a leaf, the algorithm reads it directly instead of calling the function on it, which only saves work. Therefore, the total time is linear in `n`.

**Auxiliary Space Complexity: `O(h)`**

The recursion stack contains at most `h + 1` calls, where `h` is the height of the tree. That is `O(log n)` for a balanced tree and `O(n)` for a skewed tree. No additional collection proportional to the number of nodes is used.

## 4. Reflection / Improvement

Another common approach is to pass a Boolean flag `is_left` into a helper function: a node then adds its own value if it is a leaf and `is_left` is `True`. Both approaches have the same complexity. The parent-check version used here needs no helper and no extra parameter, but it accesses grandchildren (`root.left.left`), which makes the condition a little longer.

An iterative DFS or BFS can apply the same parent-side check for each node taken from a stack or queue. It keeps `O(n)` time and avoids Python's recursion-depth limit, using `O(h)` (stack) or `O(w)` (queue) extra space. No asymptotically faster general solution exists, because every node may need to be checked.
