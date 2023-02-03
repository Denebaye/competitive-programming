class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        column_dict = defaultdict(list)
        min_col = max_col = 0

        def traverse(node):
            nonlocal min_col, max_col
            queue = deque([(node, 0, 0)])

            while queue:
                current_node, row, col = queue.popleft()

                if current_node is not None:
                    column_dict[col].append((row, current_node.val))
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)

                    queue.append((current_node.left, row + 1, col - 1))
                    queue.append((current_node.right, row + 1, col + 1))

        traverse(root)

        result = []
        for c in range(min_col, max_col + 1):
            result.append([val for row, val in sorted(column_dict[c])])

        return result
