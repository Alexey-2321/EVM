class MyCircularQueue(object):
    
    def __init__(self, k):
        
        self.k = k                      # максимальный размер
        self.queue = [0] * k            # массив для хранения 
        self.front = -1                 # указатель на первый элемент (-1 = пусто)
        self.rear = -1                  # указатель на последний элемент (-1 = пусто)
    
    def enQueue(self, value):
    
        # Если очередь полная, нельзя добавить
        if self.isFull():
            return False
        
        # Если очередь пустая, устанавливаем front и rear на 0
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            # Иначе двигаем rear по кругу
            self.rear = (self.rear + 1) % self.k
        
        # Добавляем значение
        self.queue[self.rear] = value
        return True
    
    def deQueue(self):
        
        # Если очередь пустая, нельзя удалить
        if self.isEmpty():
            return False
        
        # Если удаляем последний элемент (очередь станет пустой)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Иначе двигаем front по кругу
            self.front = (self.front + 1) % self.k
        
        return True
    
    def Front(self):
        
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self):
        
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def isEmpty(self):
        
        return self.front == -1
    
    def isFull(self):
        
        # Очередь полна, если следующий за rear — это front
        return (self.rear + 1) % self.k == self.front