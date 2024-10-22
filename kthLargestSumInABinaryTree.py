# Brief

# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.

#Solution
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        if not root:
            return -1

        # Simulate a queue for BFS
        queue = [root]  # Initialize the queue with the root node
        level_sums = []  # Store the sum of each level

        while queue:
            level_sum = 0
            next_level = []  # List to hold the next level of nodes

            # Process all nodes at the current level
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)  # Add left child to next level
                if node.right:
                    next_level.append(node.right)  # Add right child to next level

            # Append the sum of the current level to level_sums
            level_sums.append(level_sum)

            # Move to the next level
            queue = next_level

        # Sort level sums in descending order
        level_sums.sort(reverse=True)

        # Return the kth largest sum if there are at least k levels
        if k <= len(level_sums):
            return level_sums[k - 1]
        else:
            return -1
