from collections import deque

def timeRequiredToBuy(tickets, k): 
    queue = deque();
    
    for i in range(len(tickets)):
        queue.append(i)
    
    time = 0;
    
    while queue:
        time += 1
        front = queue.popleft()
        tickets[front] -= 1
        if k == front and tickets[front] == 0:
            return time;
        if tickets[front] != 0:
            queue.append(front);
   
    return time;


# print(timeRequiredToBuy([2, 3, 2], 2))

# print(timeRequiredToBuy([5, 1, 1, 1], 0))



def timeRequiredToBuyNoQueue(tickets, k):
    time = 0;
    
    for i in range(len(tickets)):
        if i >= k:
            time += min(tickets[k], tickets[i])
        else:
            time += min(tickets[k] - 1, tickets[i])
    
    return time;

