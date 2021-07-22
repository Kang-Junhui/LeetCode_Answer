# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        Q = collections.deque([root])
        res = ['#']
        
        while Q:
            node = Q.popleft()
            if node:
                Q.append(node.left)
                Q.append(node.right)
                
                res.append(str(node.val))
            else:
                res.append('#')
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        Q = collections.deque([root])
        cnt = 2
        
        while Q:
            node = Q.popleft()
            
            if nodes[cnt] != '#':
                node.left = TreeNode(int(nodes[cnt]))
                Q.append(node.left)
            cnt += 1
            
            if nodes[cnt] != '#':
                node.right = TreeNode(int(nodes[cnt]))
                Q.append(node.right)
            cnt += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
