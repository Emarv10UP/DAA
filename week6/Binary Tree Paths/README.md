# Binary Tree Paths

**LeetCode:** [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)  
**Implementation:** recursive DFS with backtracking in Python — [`solution.py`](./solution.py)

## 1. Problem

Return all paths from the root of a binary tree to its leaves, in any order. Each path is a string of node values separated by `->`, for example `"1->2->5"`.

## 2. Approach

The solution uses recursive DFS and one shared mutable list `path` that always holds the values on the way from the root to the current node.

1. If the node is `None`, return.
2. Append the node's value (as a string) to `path`.
3. If the node is a leaf, join `path` with `"->"` and add the string to `paths`.
4. Otherwise, explore the left and right children with the same `path` list.
5. Before returning, remove the current value with `path.pop()`, so that the list again describes the path to the parent.

Adding a value when entering a node and removing it when leaving is called **backtracking**.

```python
def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
    paths = []

    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:      # leaf: one complete path
            paths.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()                                # backtrack

    dfs(root, [])
    return paths
```

Values are converted to strings when they are appended, so `"->".join(path)` works directly and negative values such as `-3` are handled correctly.

### Trace example

Consider `root = [1, 2, 3, null, 5]`:

```text
      1
     / \
    2   3
     \
      5
```

| Action | `path` | `paths` |
|---|---|---|
| Enter `1` | `["1"]` | `[]` |
| Enter `2` | `["1", "2"]` | `[]` |
| Left child of `2` is `None` — return | `["1", "2"]` | `[]` |
| Enter `5` — leaf, save path | `["1", "2", "5"]` | `["1->2->5"]` |
| Leave `5` (`pop`) | `["1", "2"]` | `["1->2->5"]` |
| Leave `2` (`pop`) | `["1"]` | `["1->2->5"]` |
| Enter `3` — leaf, save path | `["1", "3"]` | `["1->2->5", "1->3"]` |
| Leave `3`, leave `1` | `[]` | `["1->2->5", "1->3"]` |

The result is `["1->2->5", "1->3"]`, and `path` is empty again at the end, which confirms that every append was matched by a pop.

### Challenges and testing

The most important detail is the `path.pop()` at the end of `dfs`. It runs for **every** non-empty node, both for leaves and for internal nodes. Without it, values from the left branch stay in the list, and the example above would produce `"1->2->5->3"` instead of `"1->3"`.

The leaf check is also important. A leaf is a node with **both** children missing. A node with only one child (like node `2` above) is not a leaf, so no path is saved there; the call on its missing child simply returns.

During the work on this solution, the submitted code initially contained a duplicated copy of the `dfs` function and the `return` statement after the first `return paths`. That copy was unreachable, so it did not change the output, but it was removed from `solution.py` to keep the code clean.

Cases worth checking:

- single node `[1]` → `["1"]` (LeetCode guarantees at least one node; an empty tree would return `[]`);
- the example above → `["1->2->5", "1->3"]`;
- left-only chain `[1, 2, null, 3]` → `["1->2->3"]`;
- a tree with negative values, e.g. `[-1, -2]` → `["-1->-2"]`;
- a full tree `[1, 2, 3, 4, 5, 6, 7]` → four paths.

## 3. Time and Space Complexity

**Time Complexity: `O(n · h)` in general, `O(n^2)` in the worst case.**

The DFS itself visits every node once and does `O(1)` work per node (append, pop, leaf check), which is `O(n)`. In addition, for every leaf the algorithm builds a string with `"->".join(path)`, which takes time proportional to the path length, at most `O(h)`. With `L` leaves this costs `O(L · h)`. Since `L ≤ n`, the total is `O(n · h)`:

- for a balanced tree, `h = O(log n)`, so the time is `O(n log n)`;
- the worst case is a tree with a long "spine" and many leaves hanging from its lower part, where both `L` and `h` are proportional to `n`, giving `O(n^2)`.

This cost is unavoidable, because it equals the size of the output that must be produced.

**Auxiliary Space Complexity: `O(h)`**, excluding the returned list.

The recursion stack and the `path` list each grow to at most `h` elements. The returned list of strings is the output and can take `O(n · h)` characters in total.

## 4. Reflection / Improvement

An alternative is to pass a **new string** to each recursive call, for example `dfs(node.left, path + "->" + str(node.left.val))`. This removes the need for `pop`, because each call has its own copy, but it copies the whole prefix at every node instead of only at leaves. The shared-list approach used here copies data only when a full path is actually saved.

An iterative DFS with a stack of `(node, path_string)` pairs can replace recursion and avoid recursion-depth limits. No approach can beat the size of the output, because every character of every path has to be written.
