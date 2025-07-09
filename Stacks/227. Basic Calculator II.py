class Solution:
    def calculate(self, s: str) -> int:
        stack = []      # This stack will keep track of all numbers after resolving *, / immediately
        num = 0         # Temporary variable to build multi-digit numbers (e.g., 34, 102)
        op = '+'        # Stores the last seen operator; default to '+' for the first number
        s = s.replace(' ', '')  # Remove all spaces for cleaner parsing

        # Loop through each character with its index
        for i, ch in enumerate(s):
            if ch.isdigit():
                # If current character is a digit, build the full number
                num = num * 10 + int(ch)

            # If current character is an operator or it's the last character
            if not ch.isdigit() or i == len(s) - 1:
                # Based on the last operator (op), apply it to the current number
                if op == '+':
                    stack.append(num)  # Simply add the number to stack
                elif op == '-':
                    stack.append(-num)  # Push its negative for later summing
                elif op == '*':
                    prev = stack.pop()  # Pop the previous number to multiply with current num
                    stack.append(prev * num)
                elif op == '/':
                    prev = stack.pop()
                    # Perform integer division truncating toward zero
                    stack.append(int(prev / num))

                # Update the operator to the current one
                op = ch
                # Reset num for the next number
                num = 0

        # Sum all values in the stack for final result
        # At this point, all + and - were deferred to here
        return sum(stack)
