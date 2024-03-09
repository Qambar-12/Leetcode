def getIntersectionNode(headA, headB):
    a,b = 0,0
    currA,currB = headA,headB
    while currA or currB:
        if currA:
            a += 1
            currA = currA.next
        if currB:
            b += 1
            currB = currB.next
    diff = abs(a-b)
    if a > b:
        for node in range(diff):
            headA = headA.next
    elif b > a:
        for node in range(diff):
            headB = headB.next
    else:
        pass
    nodeA,nodeB = headA , headB   
    if nodeA == nodeB:
        return nodeA
    else:
        while nodeA:
            if nodeA.next == nodeB.next:
                return nodeA.next
            nodeA = nodeA.next
            nodeB = nodeB.next    
        return None                       
