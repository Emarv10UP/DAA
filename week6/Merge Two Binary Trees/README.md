# Merge Two Binary Trees

**LeetCode:** [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)  
**Implementation:** recursive DFS that creates new nodes for overlapping positions, in Python — [`solution.py`](./solution.py)

## 1. Problem

Given the roots of two binary trees, merge them into one tree. If both trees have a node at the same position, the merged node's value is the sum of the two values. If only one tree has a node at that position, that node (with its whole subtree) is used in the merged tree.

## 2. Approach

The solution walks both trees **at the same time** with recursion, always looking at two nodes in the same position:

1. If `root1` is missing, return `root2` (which may also be `None`).
2. If `root2` is missing, return `root1`.
3. If both nodes exist, create a **new** node `merged` with value `root1.val + root2.val`.
4. Recursively merge the two left children and attach the result as `merged.left`.
5. Recursively merge the two right children and attach the result as `merged.right`.
6. Return `merged`.

```python
def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    if not root1:
        return root2
    if not root2:
        return root1

    merged = TreeNode(root1.val + root2.val)
    merged.left = self.mergeTrees(root1.left, root2.left)
    merged.right = self.mergeTrees(root1.right, root2.right)

    return merged
```

When one of the nodes is missing, the other subtree is returned **as it is**. There is nothing to add in that part of the tree, so the algorithm does not walk into it and does not copy it.

### Trace example

First tree `root1 = [1, 3, 2, 5]`:

```text
      1
     / \
    3   2
   /
  5
```

Second tree `root2 = [2, 1, 3, null, 4, null, 7]`:

```text
      2
     / \
    1   3
     \   \
      4   7
```

| Position | `root1` value | `root2` value | What happens |
|---|---:|---:|---|
| Root | 1 | 2 | new node `3` |
| Left child of root | 3 | 1 | new node `4` |
| Right child of root | 2 | 3 | new node `5` |
| Left-left | 5 | missing | node `5` from `root1` is reused |
| Left-right | missing | 4 | node `4` from `root2` is reused |
| Right-left | missing | missing | `None` |
| Right-right | missing | 7 | node `7` from `root2` is reused |

The merged tree is `[3, 4, 5, 5, 4, null, 7]`:

```text
       3
      / \
     4   5
    / \   \
   5   4   7
```

### Challenges and testing

The key cases are the ones where one of the two nodes is missing. Returning `None` there would throw away a subtree that must be kept. Returning the existing node keeps it, and the case "both are missing" is also covered, because `return root2` then returns `None`.

Another important detail is **which nodes are new**. Nodes in overlapping positions are newly created, so the values in `root1` and `root2` are not changed — for the example above, `root1` is still `[1, 3, 2, 5]` after the call. However, the non-overlapping subtrees are **shared** with the input trees: the merged tree points to the same node objects as `root1` or `root2` in those parts. If one of the input trees were modified later, the merged tree could change too. If complete independence were required, those subtrees would have to be deep-copied.

Cases worth checking:

- two empty trees `[]`, `[]` → `[]`;
- one empty tree: `[]`, `[1]` → `[1]` (the existing tree is returned);
- two single nodes `[1]`, `[2]` → `[3]`;
- the example above → `[3, 4, 5, 5, 4, null, 7]`;
- trees whose missing branches are at different depths, to check that whole subtrees are kept.

## 3. Time and Space Complexity

Let `n` and `m` be the numbers of nodes in the two trees, and let `k` be the number of positions where **both** trees have a node.

**Time Complexity: `O(k)`, which is at most `O(min(n, m))`.**

A new node is created and two recursive calls are made only at overlapping positions. Each call where one node is missing returns immediately in `O(1)`, and there are at most `2k + 1` such calls. Non-overlapping subtrees are not traversed. Since `k` cannot be larger than the size of the smaller tree, the time is `O(min(n, m))`.

**Space Complexity: `O(k)` for the new nodes, plus `O(h)` for the recursion stack.**

The function allocates `k` new `TreeNode` objects, one for each overlapping position; these become part of the returned tree. The recursion stack only goes as deep as the overlapping part of the two trees, so its depth is at most the height of the smaller tree: `O(log min(n, m))` for balanced trees and `O(min(n, m))` in the worst (skewed) case.

## 4. Reflection / Improvement

A common alternative is to merge **in place** into `root1`: instead of creating `merged`, do `root1.val += root2.val`, attach the merged children to `root1`, and return `root1`. This avoids allocating `k` new nodes, so the extra memory is only the `O(h)` stack, but it destroys the original values of `root1`. The version used here is a reasonable middle ground: it does not change either input tree, and it still avoids copying the parts of the trees that do not overlap.

An iterative version can process pairs of nodes with a stack or queue and avoid Python's recursion-depth limit. It keeps `O(k)` time. No approach can be asymptotically faster in general, because every overlapping position needs its own addition.
