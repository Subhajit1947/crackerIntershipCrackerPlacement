#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        cz,co,ct=0,0,0
        temp=head
        while temp:
            if temp.data==0:
                cz+=1
            if temp.data==1:
                co+=1
            if temp.data==2:
                ct+=1
            temp=temp.next
        temp=head
        while temp:
            if cz!=0:
                temp.data=0
                cz-=1
            elif cz==0 and co!=0:
                temp.data=1
                co-=1
            elif cz==0 and co==0 and ct!=0:
                temp.data=2
                ct-=1
            temp=temp.next
        
        return head
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))

# } Driver Code Ends