# Binary Tree Inorder Traversal

**LeetCode:** [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)  

## 1. Problem

Given the root of a binary tree, return the values of its nodes in **inorder** order. Inorder means that the left subtree is processed first, then the current node, and finally the right subtree.

## 2. Approach

The solution uses recursive depth-first search (DFS). A nested helper function `traverse(node)` writes values into a shared list `result`:

1. If the node is `None`, it stops that branch.
2. It recursively processes the left child.
3. It appends the current node's value to `result`.
4. It recursively processes the right child.

The order of these operations is essential. Appending the value before visiting the left child would produce preorder traversal, and appending it after both calls would produce postorder traversal.

```python
def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)       # 1. left subtree
        result.append(node.val)   # 2. current node
        traverse(node.right)      # 3. right subtree

    traverse(root)
    return result
```

Because `result` is defined in the outer function, the helper can append to it directly without passing the list as an argument or returning partial lists.

### Trace example

Consider this tree (`root = [1, null, 2, 3]`):

```text
      1
       \
        2
       /
      3
```

| Step | Action | `result` |
|---:|---|---|
| 1 | Start at node `1`; go to its left child (`None`) and return | `[]` |
| 2 | Append node `1` | `[1]` |
| 3 | Go to the right child, node `2`; first go to its left child, node `3` | `[1]` |
| 4 | Node `3` has no left child; append `3`; it has no right child | `[1, 3]` |
| 5 | Return to node `2` and append it; its right child is `None` | `[1, 3, 2]` |

The final answer is `[1, 3, 2]`.

### Challenges and testing

The main point to get right is **when** the current node is added. All three depth-first traversals visit the same nodes; they differ only in where the `append` is placed relative to the two recursive calls. The example above is a good check: an implementation that adds `1` and then `2` before `3` would be doing preorder, not inorder.

Cases worth checking:

- empty tree `[]` → `[]`;
- single node `[1]` → `[1]`;
- left-skewed chain, e.g. `[3, 2, null, 1]` → `[1, 2, 3]`;
- right-skewed chain, e.g. `[1, null, 2, null, 3]` → `[1, 2, 3]`.

Skewed trees are useful because they create the deepest possible recursion for a given number of nodes.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Every node is visited exactly once. At each visit, the algorithm does a constant amount of work besides the recursive calls: one comparison with `None` and one `append`. Calls on `None` children are also constant-time, and there are `n + 1` of them. Therefore, the total work grows linearly with the number of nodes `n`.

**Auxiliary Space Complexity: `O(h)`**

The recursion stack holds at most `h + 1` active calls, where `h` is the height of the tree. This is `O(log n)` for a balanced tree and `O(n)` for a completely skewed tree. The returned list `result` uses `O(n)` space, but that is output space rather than auxiliary working space.

## 4. Reflection / Improvement

An iterative inorder traversal can replace the call stack with an explicit stack: keep going left and pushing nodes, then pop a node, record it, and move to its right child. It still takes `O(n)` time and `O(h)` auxiliary space, but it avoids Python's recursion-depth limit (about 1000 by default) on very deep trees. On LeetCode the tree has at most 100 nodes, so the recursive version is safe and easier to read.

Morris traversal can reduce auxiliary space to `O(1)` by temporarily rewiring `right` pointers, but it is harder to implement correctly and modifies the tree during the traversal. No approach can be asymptotically faster than `O(n)`, because every node must appear in the output.
