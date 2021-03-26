# Write a recursive function to count the number of nodes in a Tree. (first do your self then see code)

def count_nodes(self):
	count = 1
	left_count = 0
	right_count = 0
	if self.left:
		left_count = self.left.count_nodes()
		
	if self.right:
		right_count = self.right.count_nodes()
	
	return count + left_count + right_count
	
	
 Q # 2:	
'''The height of a tree is the maximum number of levels in the tree. So, a tree with just one node has a height of 1. If the root has children which are leaves, the height of the tree is 2.
The height of a TreeNode can be computed recursively using a simple algorithm: The height Of a TreeNode With no children is 1. If it has children the height is: max of height of its two sub-trees  + 1.
Write a clean, recursive function for the TreeNode class that calculates the height based on the above statement(first do your self then see code) ''' 


def get_height(self):
	height = 1
	left_height = 0
	right_height = 0
	if self.left:
		left_height = self.left.get_height()
		
	if self.right:
		right_height = self.right.get_height()
	
	return count + max(left_height, right_height)
	
	
print(self.val)
if self.left.val > self.val or self.right.val < self.val
	return False
