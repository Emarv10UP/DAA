# Binary Tree Preorder Traversal

**LeetCode:** [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)  
**Implementation:** iterative DFS with an explicit stack in Python — [`solution.py`](./solution.py)

## 1. Problem

Return the values of all nodes of a binary tree in **preorder** order: the current node first, then its left subtree, and then its right subtree.

## 2. Approach

Instead of recursion, the solution uses an explicit stack (a Python list) that plays the role of the call stack.

1. If the tree is empty, return `[]`.
2. Push the root onto the stack.
3. While the stack is not empty:
   - pop the top node and append its value to `result` (the node is processed **before** its children — this is what makes it preorder);
   - push the **right** child first, then the **left** child.

A stack is LIFO (last in, first out). Because the left child is pushed last, it is popped next, so the whole left subtree is processed before the right child is popped. This produces exactly the order node → left → right.

```python
def preorderTraversal(self, root: TreeNode | None) -> list[int]:
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Right is pushed first, so left is popped (and processed) first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### Trace example

For `root = [1, null, 2, 3]`:

```text
      1
       \
        2
       /
      3
```

| Step | Popped | `result` | Pushed | Stack after the step |
|---:|---|---|---|---|
| 0 | — | `[]` | `1` | `[1]` |
| 1 | `1` | `[1]` | right `2` (no left child) | `[2]` |
| 2 | `2` | `[1, 2]` | left `3` (no right child) | `[3]` |
| 3 | `3` | `[1, 2, 3]` | nothing | `[]` |

The stack is empty, so the result is `[1, 2, 3]`.

A tree with both children shows why the push order matters. For `[1, 2, 3]`, after popping `1` the stack becomes `[3, 2]`, so `2` (the left child) is popped before `3`, giving `[1, 2, 3]`. If the children were pushed in the order left, right, the answer would be `[1, 3, 2]`, which is wrong.

### Challenges and testing

The main challenge is the **push order**. It is the opposite of the visiting order, because the stack reverses it. Pushing left before right is a common mistake that silently produces node → right → left.

Another detail is checking children before pushing them. Only existing children are pushed, so `stack.pop()` never returns `None` and `node.val` is always safe.

Cases worth checking:

- empty tree `[]` → `[]` (handled by the early return);
- single node `[1]` → `[1]`;
- left-only chain `[1, 2, null, 3]` → `[1, 2, 3]`;
- right-only chain `[1, null, 2, null, 3]` → `[1, 2, 3]`;
- a full tree such as `[1, 2, 3, 4, 5]` → `[1, 2, 4, 5, 3]`.

The full tree is the most useful test, because it is the only one of these where the push order of two siblings actually matters.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Every node is pushed once and popped once, and each pop does constant work (one `append` to the result and up to two pushes). The total time is therefore linear in the number of nodes.

**Auxiliary Space Complexity: `O(h)`**, where `h` is the tree height.

When a node is popped, its children replace it on the stack, and at most one pending right child is left behind on each level of the current path. Therefore, the stack never holds more than about `h + 1` nodes. This is `O(log n)` for a balanced tree and `O(n)` for a skewed tree. The output list `result` takes another `O(n)` space, which is required by the problem.

## 4. Reflection / Improvement

The recursive version is shorter and follows the definition directly:

```python
def preorderTraversal(self, root):
    if not root:
        return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

However, this one-line form creates new lists at every call and can take `O(n^2)` time on a skewed tree; a recursive helper that appends to one shared list avoids that. The iterative version chosen here keeps `O(n)` time, does not depend on Python's recursion-depth limit, and makes the role of the stack explicit. Morris traversal could reduce the auxiliary space to `O(1)`, at the cost of temporarily modifying the tree.
