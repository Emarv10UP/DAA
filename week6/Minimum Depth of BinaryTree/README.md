# Minimum Depth of Binary Tree

**LeetCode:** [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)  
**Implementation:** iterative BFS with early exit in Python — [`solution.py`](./solution.py)

## 1. Problem

Find the minimum depth of a binary tree: the number of nodes along the shortest path from the root down to the nearest **leaf**. A leaf is a node that has no left child and no right child. An empty tree has depth `0`.

## 2. Approach

The solution uses breadth-first search (BFS). BFS visits nodes in order of their distance from the root: first the root, then all nodes at depth `2`, then all nodes at depth `3`, and so on. Therefore, the **first leaf removed from the queue is a closest leaf**, and its depth is the answer. The algorithm can stop immediately at that point.

Each queue entry is a pair `(node, depth)`, so the depth of a node is always known when it is removed:

1. If the tree is empty, return `0`.
2. Put `(root, 1)` into a `deque`.
3. Repeatedly remove the front pair `(node, depth)`:
   - if `node` is a leaf, return `depth`;
   - otherwise, add each existing child with depth `depth + 1`.

```python
def minDepth(self, root: TreeNode | None) -> int:
    if not root:
        return 0

    queue = deque([(root, 1)])          # (node, depth of that node)

    while queue:
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth                # first leaf found by BFS = closest leaf

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0
```

Only existing children are added to the queue, so a missing child is never mistaken for a leaf. The final `return 0` is never reached for a non-empty tree, because every finite non-empty tree has at least one leaf; it only keeps the function's return type consistent.

### Trace example

Consider `root = [1, 2, 3, null, null, null, 4]`:

```text
       1
      / \
     2   3
          \
           4
```

| Step | Removed | Leaf? | Queue after the step |
|---:|---|---|---|
| 1 | `(1, 1)` | no | `[(2, 2), (3, 2)]` |
| 2 | `(2, 2)` | **yes** | — return `2` |

The answer is `2`, through the path `1 -> 2`. Nodes `3` and `4` are never removed from the queue, which shows the benefit of the early exit.

### Challenges and testing

The most important edge case is a node with **exactly one child**. A tempting recursive formula `1 + min(minDepth(left), minDepth(right))` is wrong there: the missing child returns `0`, even though it is not a path to a leaf. For the chain `[2, null, 3, null, 4, null, 5, null, 6]` that formula returns `1`, but the correct answer is `5`. The BFS solution avoids this problem by design, because it only enqueues real children and only stops at a real leaf.

Cases worth checking:

- empty tree `[]` → `0`;
- single node `[1]` → `1` (the root itself is a leaf);
- the example above → `2`;
- right-only chain `[2, null, 3, null, 4, null, 5, null, 6]` → `5`;
- a tree where the nearest leaf is on the "smaller-looking" side.

## 3. Time and Space Complexity

**Time Complexity: `O(n)`**

Each node is added to and removed from the queue at most once, with constant work per node. In the worst case (for example, a chain, or a complete tree where all leaves are on the last level) the algorithm processes every node before it finds a leaf. When a shallow leaf exists, BFS stops early and examines only the nodes up to that level.

**Auxiliary Space Complexity: `O(w)`**, where `w` is the maximum width of the tree.

The queue holds at most about one level of nodes at a time. This is `O(1)` for a chain and up to `O(n)` for a wide, complete tree. Each entry stores a node and an integer, which is still constant space per entry.

## 4. Reflection / Improvement

A correct recursive DFS solution handles the one-child case explicitly:

```python
def minDepth(self, root):
    if not root:
        return 0
    if not root.left:
        return 1 + self.minDepth(root.right)
    if not root.right:
        return 1 + self.minDepth(root.left)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

It uses `O(h)` stack space, but it always explores the **whole** tree, even if a leaf exists right next to the root. BFS is the better fit here because the question asks for the *nearest* leaf, and BFS reaches nearer nodes first. BFS also avoids Python's recursion-depth limit, which matters because this problem allows up to `10^5` nodes. The trade-off is memory on very wide trees, where the queue can grow to `O(n)`.
