#Wubi Halefom
#03/6/23

from llist import *
from gencyclic import *


def getNext(Node):
    return Node.next

def llprint(lst, num):
    count = 0
    currentNode = lst.head
    for i in range(num):
        print(currentNode.val, end=' ')
        currentNode = currentNode.next
        

def find_cycle(lst):
 
    tortoise = getNext(lst.head)
    hare = getNext(getNext(lst.head))
    while tortoise != hare:
        tortoise = getNext(tortoise)
        hare = getNext(getNext(hare))
  
    mu = 0
    tortoise = lst.head
    while tortoise != hare:
        tortoise = getNext(tortoise)
        hare = getNext(hare)   
        mu += 1
 
    lam = 1
    hare = getNext(tortoise)
    while tortoise != hare:
        hare = getNext(hare)
        lam += 1
 
    return lam, mu


if __name__ == "__main__":
    tup = find_cycle(lst)
    print(f"The cycle starts at: {tup[0]}")
    print(f"The cycle's length is: {tup[1]}")

#The cycle starts at 17 and its length  is 47060
