class Solution:
    """
    Generate all possible letter combinations that a phone number could represent.
    
    Classic phone keypad mapping:
    2 -> abc, 3 -> def, 4 -> ghi, 5 -> jkl, 6 -> mno,
    7 -> pqrs, 8 -> tuv, 9 -> wxyz
    """
    
    def __init__(self):
        # Mapping: index represents digit, value represents possible letters
        # Index 0 and 1 are empty (digits 0 and 1 don't have letters)
        self.digit_to_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    def letterCombinations(self, digits):
        """
        Main function to generate all letter combinations.
        
        Args:
            digits: String of digits (e.g., "23")
            
        Returns:
            List of all possible letter combinations
        """
        result = []
        
        # Edge case: empty input
        if not digits:
            return result
        
        self._generate_combinations(digits, result, 0, "")
        return result
    
    def _generate_combinations(self, digits, result, index, current_combination):
        """
        Backtracking helper to generate all letter combinations.
        
        Intuition:
        - We use backtracking/DFS to explore all possible paths
        - For each digit, we try all possible letters it can represent
        - We build the combination character by character
        - When we've processed all digits, we have a complete combination
        
        Example with "23":
        - First digit '2' -> try 'a', 'b', 'c'
        - For each, process second digit '3' -> try 'd', 'e', 'f'
        - Results: "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        
        Args:
            digits: Original input string of digits
            result: List to store all valid combinations
            index: Current position in the digits string
            current_combination: Current combination being built
        """
        # Base case: We've processed all digits
        # Add the complete combination to result
        if index == len(digits):
            result.append(current_combination)
            return
        
        # Get the current digit and its corresponding letters
        current_digit = int(digits[index])
        possible_letters = self.digit_to_letters[current_digit]
        
        # Try each possible letter for the current digit
        # This creates a branching tree where each branch represents a different letter choice
        for letter in possible_letters:
            # IMPORTANT: Why no explicit reset/backtrack needed?
hats            # Strings in Python are IMMUTABLE. When we do `current_combination + letter`,
            # we're creating a NEW string object, NOT modifying the existing one.
            # 
            # Example: If current_combination = "a" and letter = "d":
            #   - We pass "a" + "d" = "ad" to the recursive call
            #   - The original current_combination = "a" remains unchanged
            #   - When recursion returns, current_combination is still "a"
            #   - Next iteration: current_combination = "a" + "e" = "ae"
            #
            # This is different from using a mutable list (like in combination_sum_3.py),
            # where we'd need to do: list.append(), recurse, list.pop() to backtrack.
            #
            # Choose: Add current letter to combination (creates new string)
            # Explore: Recurse to process next digit
            self._generate_combinations(
                digits, 
                result, 
                index + 1,  # Move to next digit
                current_combination + letter  # Creates NEW string, doesn't modify original
            )
            # Unchoose: Not needed! The original current_combination is automatically preserved
            # because strings are immutable - each recursive call gets its own copy
