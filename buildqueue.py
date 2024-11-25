class Queue:
  
    def __init__(self,size):
        self.size=size
        self.myqueue=[]
    def insert(self,newval):
        if len(self.myqueue)<self.size:
            self.myqueue.append(newval)
        else:
            print("myqueue is full")   
        
    def deqeue(self):
        if  len(self.myqueue)==0:
            print("myqueue is empty")
        else:
            self.myqueue.pop()
    def is_empty(self):
        if len(self.myqueue)==0:
            print("myqueue is empty")
    def __str__(self):
        return f"my queue : {self.myqueue}"
    

q1=Queue(5)   
q1.insert(4)
q1.insert(9)
q1.insert(10)
print(q1)
q1.deqeue()
print(q1)
