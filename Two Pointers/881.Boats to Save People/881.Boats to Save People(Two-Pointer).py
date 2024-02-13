def numRescueBoats(people, limit):
    people.sort()
    #using two-pointer approach
    start, end = 0, len(people) - 1
    count = 0
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        count += 1
    return count
print(boats([3,3,3],3)) 
