# Binary Tree Postorder Traversal

**LeetCode:** [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)  
**Implementation:** iterative DFS with one stack and a final reversal in Python — [`solution.py`](./solution.py)

## 1. Problem

Return the values of all nodes of a binary tree in **postorder** order: the left subtree first, then the right subtree, and the current node last.

## 2. Approach

A direct iterative postorder traversal is tricky, because a node may only be recorded after **both** of its subtrees are finished. This solution avoids that difficulty with a simple observation:

- postorder is **left → right → root**;
- reversed, this is **root → right → left**;
- root → right → left is just a preorder traversal with the two children swapped, which is easy to do with a stack.

So the algorithm builds the order root → right → left and reverses it at the end:

1. If the tree is empty, return `[]`.
2. Push the root onto the stack.
3. While the stack is not empty:
   - pop a node and append its value to `result`;
   - push the **left** child first, then the **right** child, so that the right child is popped first.
4. Return `result[::-1]`.

```python
def postorderTraversal(self, root: TreeNode | None) -> list[int]:
    if not root:
        return []

    stack = [root]
    result = []

    # Build root -> right -> left
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:            # pushed first, popped later
            stack.append(node.left)
        if node.right:           # pushed last, popped first
            stack.append(node.right)

    # Reverse to get left -> right -> root
    return result[::-1]
```

Compared with the preorder solution in task 05, the only difference inside the loop is the push order of the children; the reversal at the end turns the result into postorder.

### Trace example

For `root = [1, null, 2, 3]`:

```text
      1
       \
        2
       /
      3
```

| Step | Popped | `result` (root → right → left) | Pushed | Stack after the step |
|---:|---|---|---|---|
| 0 | — | `[]` | `1` | `[1]` |
| 1 | `1` | `[1]` | right `2` | `[2]` |
| 2 | `2` | `[1, 2]` | left `3` | `[3]` |
| 3 | `3` | `[1, 2, 3]` | nothing | `[]` |

Reversing `[1, 2, 3]` gives the final answer `[3, 2, 1]`. The root `1` correctly appears last.

For a full tree `[1, 2, 3, 4, 5]`:

```text
        1
       / \
      2   3
     / \
    4   5
```

the loop produces `[1, 3, 2, 5, 4]` (root → right → left), and the reversal gives `[4, 5, 2, 3, 1]`, which is the correct postorder.

### Challenges and testing

The main thing to get right is that **both** steps must be changed compared with preorder: the push order (left first, then right) and the final reversal. Doing only one of them gives a wrong order. For example, reversing a normal preorder `[1, 2, 4, 5, 3]` gives `[3, 5, 4, 2, 1]`, which is not postorder.

It is also important to notice that the values are **not** produced in postorder during the loop. If someone needed to process nodes in postorder one at a time (for example, to free child nodes before their parent), this trick would not work, because the correct order only exists after the reversal.

Cases worth checking:

- empty tree `[]` → `[]`;
- single node `[1]` → `[1]`;
- left-only chain `[1, 2, null, 3]` → `[3, 2, 1]`;
- right-only chain `[1, null, 2, null, 3]` → `[3, 2, 1]`;
- full tree `[1, 2, 3, 4, 5]` → `[4, 5, 2, 3, 1]`.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Every node is pushed and popped exactly once with constant work per node. The reversal `result[::-1]` takes another `O(n)`. In total, `O(n) + O(n) = O(n)`.

**Auxiliary Space Complexity: `O(h)` for the stack**, plus `O(n)` for the result.

As in the preorder traversal, the stack holds the current path plus at most one pending sibling per level, so its size is `O(h)`: `O(log n)` for a balanced tree and `O(n)` for a skewed tree. The list `result` is the output and takes `O(n)`. Note that `result[::-1]` creates a **new** reversed list, so for a short time two lists of size `n` exist; this is still `O(n)`. Using `result.reverse()` and returning `result` would reverse the list in place and avoid the extra copy.

## 4. Reflection / Improvement

The recursive solution matches the definition directly (left call, right call, then `append`) and uses `O(h)` stack space. The iterative "reversed preorder" approach used here avoids recursion-depth limits and is much simpler than a true one-stack postorder traversal.

A true iterative postorder traversal (with one stack and a pointer to the previously visited node, or with a "visited" flag for each node) produces values in the correct order immediately and does not need the reversal. It has the same `O(n)` time and `O(h)` stack space, but its control flow is noticeably more complex. For this problem, where only the final list is needed, the reversal trick is the clearer choice.
