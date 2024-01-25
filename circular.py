"""
CircularQueue: A dictionary using a circular buffer. It removes the oldest element when the buffer lenght exceed the maximum size.
"""

from collections import OrderedDict

class CircularQueue(OrderedDict):
    """
    Initialize maxlen
    """
    def __init__(self, maxlen):
        self.maxlen = maxlen
        super().__init__()

    """
    enqueue: add the pair (key, value) item or remove last inserted item if the buffer is full
    """
    def enqueue(self, key, value):
        # Remove last item if buffer is full
        if len(self) >= self.maxlen:
            super().popitem(last=True)        
        OrderedDict.__setitem__(self, key, value)

def test_circular_queue(max_size):

    if not max_size > 0:
        print("Circular buffer size must be greater than 0!")
        return
    
    # Initialize a CircularDict with a maximum length of max_size
    cqueue = CircularQueue(maxlen=max_size)
    # Add items
    for i in range(1, max_size + 1):
        cqueue.enqueue( 'key' + str(i) , 'value' + str(i))

    print(f'Circular queue with {max_size} items:')
    print(cqueue)

    # Add more items, only last item will be inserted
    for i in range(max_size + 1, max_size + 3):
        cqueue.enqueue( 'key' + str(i) , 'value' + str(i))

    print(f'After adding element(s) beyond maxlen: {cqueue}')
    print(f'{cqueue}')

