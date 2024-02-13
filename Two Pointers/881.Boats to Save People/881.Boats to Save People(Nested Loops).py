def numRescueBoats(people,limit):
    """ The solution is of order of complexity O(n2) due to nested loop"""
    people.sort(reverse=True)
    count = people.count(limit)
    people = people[count:]
    indices = []
    for i in range(len(people)):
        j = i+1
        while j < len(people):
            if i not in indices and j not in indices:
                if people[i]+people[j] <= limit:
                    count += 1
                    indices += [i,j]
                    break
                else:
                    j+=1
            else:
                j += 1
    diff = len(people) - len(indices)
    if diff > 0:
        count += diff                     
    return count    
print(boats([1,2,3,4,5,6],6))    
