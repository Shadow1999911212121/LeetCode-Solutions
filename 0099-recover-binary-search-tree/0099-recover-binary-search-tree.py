class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # If current node breaks the sorted order
            if self.prev and self.prev.val > node.val:
                # First violation: prev is the culprit
                if not self.first:
                    self.first = self.prev
                # Second violation: current is the culprit
                self.second = node
                
            self.prev = node
            inorder(node.right)
            
        inorder(root)
        
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val
