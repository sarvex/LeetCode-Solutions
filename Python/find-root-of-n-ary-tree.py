# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass


class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = 0
        for node in tree:
            root ^= id(node)
            for child in node.children:
                root ^= id(child)
        return next((node for node in tree if id(node) == root), None)


class Solution2(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = 0
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        return next((node for node in tree if node.val == root), None)


class Solution3(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = sum(node.val-sum(child.val for child in node.children) for node in tree)
        return next((node for node in tree if node.val == root), None)
