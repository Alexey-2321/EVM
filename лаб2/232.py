class MyQueue(object):
    
    def __init__(self):
    
        self.input_stack = []   # для новых элементов
        self.output_stack = []  # для элементов в обратном порядке

    def push(self, x):
    
        self.input_stack.append(x)

    def pop(self):
    
        # Если выходной стек пуст, перекладываем элементы
        if not self.output_stack:
            self._transfer()
        # Берём элемент с вершины выходного стека
        return self.output_stack.pop()

    def peek(self):

        # Если выходной стек пуст, перекладываем элементы
        if not self.output_stack:
            self._transfer()
        # Смотрим на вершину выходного стека
        return self.output_stack[-1]

    def empty(self):
        
        return not self.input_stack and not self.output_stack
    
    def _transfer(self):
        
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())