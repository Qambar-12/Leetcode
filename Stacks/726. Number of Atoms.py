class Solution:
    def countOfAtoms(self, formula: str) -> str:
        #stack of hashmaps 
        #An element can have Upper and Lower case ch both
        #The count of an element may be more than just a single digit

        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            #for each opening parantheses we need to have a separate hashmap count
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                curr_map = stack.pop()
                count = ""
                while i+1 < len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i += 1
                count = 1 if not count else int(count)    
                prev_map = stack[-1]
                for element in curr_map:
                    prev_map[element] += (curr_map[element]*count)
            #upper case character
            else:
                element = formula[i]
                #checking for lower case character
                while i+1 < len(formula) and formula[i+1].islower():
                    element += formula[i+1]
                    i += 1
                #checking for the number of atoms that is not necassarily single digit
                count = ""    
                while i+1 < len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i += 1
                count = 1 if not count else int(count)    
                #add the element and its count to the hashmap
                curr_map = stack[-1]
                curr_map[element] += count
            i += 1     

        final_map = stack[-1]
        res = ""
        for element in sorted(final_map.keys()):
            count = "" if final_map[element] == 1 else str(final_map[element])
            res += (element + count)
        return res    
