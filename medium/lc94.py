## Binary Tree inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Algorithm:
        1. initialize a stack, visited set.
        2. while len of stack > 0,
           for each node
            if node.left exit and was not explored, node = node.left
            elif node.right exit and was not explored, node = node.right
            else, break
        3. add the current node to stack
        """
        output = []
        if root:
            stack = [root]

            visited = set()
            node = root
            while stack:
                # print([i.val for i in stack])
                # print('output', output)
                # print('visited', [i.val for i in visited])
                node = stack[-1]

                while node:
                    # print(node.val)
                    # print([i.val for i in stack])
                    if node.left and node.left not in visited:
                        stack.append(node.left)
                        node = node.left
                    elif node.right and node.right not in visited:
                        x = stack.pop(-1)
                        output.append(x.val)
                        visited.add(x)
                        stack.append(node.right)
                        node = node.right
                    else:
                        visited.add(node)
                        break
                node = stack.pop(-1)
                output.append(node.val)

        return output
# faster, and no need visited 
        output = []
        stack = []
        node = root
        while stack or node:
            # go to the most left one
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]
            output.append(stack.pop().val)
            node = node.right
        return output
