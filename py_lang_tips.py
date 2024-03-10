[::-1] # reverse a

# remove item by index in list
lst.pop(i) or del lst[i]


# python stack (LIFO)
stack = []
stack.append(x)
stack.pop()


# python queue (FIFO)
from collections import deque
q = deque()
q.append('a')
q.popleft()


# python heap/pq
I and II has the same time complexity, but II is sychronized and supports concurrent processes, and use class interface.
I.
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
customers.put((3, "Charles"))
while customers:
     print(heapq.heappop(q))

II.
from queue import PriorityQueue
customers = PriorityQueue()
customers.put((2, "Harry"))
customers.put((3, "Charles"))
while customers:
     print(customers.get())



# declare 2 d array
dp = [[False for _ in range(sz)] for _ in range(sz)]


# iterate 2d array (first outer then inner)
pos = [1 for row in dp for itm in row if itm]
sum(pos)


["foo", "bar", "baz"].index("bar") # 1


for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)




filtered_chars = filter(lambda ch: ch.isalnum(), s)
lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

filtered_chars_list = list(lowercase_filtered_chars)
reversed_chars_list = filtered_chars_list[::-1]


# "detach" is the same as "with torch.no_grad():

str(datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f'))

# download file from web and save
from urllib.request import urlretrieve
urlretrieve(url, filename) # this will download "url" and save in "filename"