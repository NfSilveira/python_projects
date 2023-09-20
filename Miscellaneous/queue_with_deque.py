from typing import Any, Deque
from collections import deque

queue: Deque[Any] = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print('Removido', queue.popleft())
print('Removido', queue.popleft())
print('Removido', queue.popleft())

print('For Inútil')
for item in queue:
    print(item)