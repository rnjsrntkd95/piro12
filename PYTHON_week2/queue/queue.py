# 큐 클래스 구현
class queue:
    def __init__(self):
        self.queue_li = []
        self.rear = 0
        self.front = 0

    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False

    def push(self, data):
        self.queue_li.append(data)
        self.rear += 1

    def pop(self):
        if self.isEmpty():
            return None
        data = self.queue_li[self.front]
        self.front += 1
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue_li[self.front]