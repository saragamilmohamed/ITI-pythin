
import json
class Queue:
    
    names_queues={}

    queues_file = "queues.json"
    
    def __init__(self,size,name):
        self.size=size
        self.name=name
        self.myqueue=[]
        Queue.names_queues[self.name] = self.myqueue 
        self.save()

    def insert(self,newval):

        if len(self.myqueue)<self.size:
            self.myqueue.append(newval)
        elif len(self.myqueue)>self.size:
            raise ValueError ("OutOfRangeException")


    @classmethod
    def load(cls):
        try:
            fileobject = open(cls.queues_file)
            queues = json.load(fileobject)
            fileobject.close()
        except FileNotFoundError:
            queues = []

        return queues


    def save(self):
        queues = self.__class__.load()
        queues.append(self.__dict__)
        try:
            with open(self.queues_file, mode='w') as queues_file:
                queues_file.write(json.dumps(queues, indent=4))

            return True
        except Exception as e:
            print(e)
            return False
        


        
    def deqeue(self):
        if  len(self.myqueue)==0:
            print("myqueue is empty")
        else:
            self.myqueue.pop()
    def is_empty(self):
        if len(self.myqueue)==0:
            print("myqueue is empty")
    def __str__(self):
        return f"my queue {self.name}: {self.myqueue}"
    

q1=Queue(5,"abc")   
q1.insert(1)
q1.insert(2)
q1.insert(3)
q1.insert(4)
q1.insert(5)

#print(q1)
q1.deqeue()
#print(q1)
q2=Queue(3,"cde")
q1.insert(1)
q1.insert(2)
q1.insert(3)

#print(Queue.names_queues['abc'])

