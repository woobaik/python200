class Solution:
    def maxDepth(self, s: str) -> int:

        max_nested = 0
        current_nested_level = 0

        for i in s:
            if i == '(':
                current_nested_level += 1

            elif i == ')':
                current_nested_level -= 1

            if current_nested_level > max_nested:
                max_nested = current_nested_level

        return max_nested
