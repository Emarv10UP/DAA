# Invert Binary Tree

**LeetCode:** [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)  

## 1. Problem

Given the root of a binary tree, invert it — swap the left and right child of **every** node — and return the root. The values stay the same; only the structure is mirrored.

## 2. Approach

The solution uses recursive DFS and changes the tree **in place**:

1. If the current node is `None`, return `None`.
2. Swap the current node's children with tuple assignment: `root.left, root.right = root.right, root.left`.
3. Recursively invert the (new) left subtree and the (new) right subtree.
4. Return the current node.

```python
def invertTree(self, root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    root.left, root.right = root.right, root.left   # swap children

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
```

The swap is done in a single tuple assignment. Python evaluates the right side `(root.right, root.left)` completely before assigning, so no temporary variable is needed and neither child reference is lost.

The swap is performed **before** the recursive calls (a preorder-style traversal). The order of the two recursive calls does not matter: after the swap they still cover both original subtrees, and each subtree is inverted exactly once. The return values of the recursive calls are not used, because each call modifies its subtree in place and the child pointers of `root` already point to the correct nodes.

### Trace example

Starting tree `root = [4, 2, 7, 1, 3, 6, 9]`:

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

- At node `4`: swap its children, so `7` is now on the left and `2` on the right.
- Recurse into node `7` (now the left child): swap `6` and `9`, so its left child is `9` and its right child is `6`. Nodes `9` and `6` are leaves; swapping their `None` children changes nothing.
- Recurse into node `2` (now the right child): swap `1` and `3`, so its left child is `3` and its right child is `1`.

The result is `[4, 7, 2, 9, 6, 3, 1]`:

```text
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### Challenges and testing

A dangerous implementation assigns the children one at a time, for example:

```python
root.left = self.invertTree(root.right)
root.right = self.invertTree(root.left)   # root.left has already been overwritten!
```

After the first line the original left subtree is lost, and the second line inverts the right subtree a second time. Swapping both references in one tuple assignment, as in this solution, avoids this bug.

Another point is that **every level** must be mirrored, not only the root's children. Checking only the first level of the output is not enough to confirm correctness.

Cases worth checking:

- empty tree `[]` → `[]`;
- single node `[1]` → `[1]`;
- one child, e.g. `[2, 1]` → `[2, null, 1]` (a left child becomes a right child);
- the three-level example above → `[4, 7, 2, 9, 6, 3, 1]`.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Every node is visited once, and each visit performs one constant-time swap. Calls on `None` children are also constant-time. The total running time is linear in the number of nodes.

**Auxiliary Space Complexity: `O(h)`**

The recursion stack reaches a maximum depth equal to the tree height `h`: `O(log n)` for a balanced tree and `O(n)` for a skewed tree. The tree is modified in place, so no new nodes are created.

## 4. Reflection / Improvement

The same swaps can be done iteratively with a queue (BFS) or a stack (DFS): pop a node, swap its children, and push the non-empty children. The time stays `O(n)`; a BFS queue uses `O(w)` space, where `w` is the maximum width. The iterative version is useful for very deep trees where Python's recursion limit could be a problem, but it is not asymptotically faster.

Because the solution modifies the input tree, the original structure is not preserved. If the original tree had to be kept, the function would need to build a new mirrored tree, which would take `O(n)` extra memory.
