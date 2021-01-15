class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
       
        self._queue.append(item)
        
    def dequeue(self, number_to_delete):        
        """         
        Delete a item in the queue         
        """         
        self._queue.pop(int(number_to_delete)-1)

    def get_queue(self):
        return self._queue

    def size(self):
        pass