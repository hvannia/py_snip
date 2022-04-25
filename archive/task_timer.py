#from dataclasses import dataclass 
import time

from datetime import datetime, timedelta


class Task(object):
    _registry = []
    
    #current_task:int = 0
    #task_count:int = 0
 
    def __init__(self,task_name:str) -> None:
        self.task_name: str = task_name
        self.active:bool = False
        #self.start_time:datetime.datetime = None
        self.zero_duration :datetime.datetime =  datetime.now() 
        self.duration : datetime.timedelta =self.zero_duration-self.zero_duration
        self._registry.append(self)

    def __str__(self):
        return f'Task {self.task_name}, active: {self.active}'


class TaskTimerManager():


    def stop_task(self, t:Task)->None:
        if t.active:
            print(f'stopping {t.task_name}')
            t.duration = t.duration + (datetime.now() - t.start_time) 
            t.active = False 
            print(f'stopped {t.task_name} has run {t.duration}')

    def start_task(self,t:Task)->None:
        #print(f' stopping any active tasks... ')
        for rtask in Task._registry:
            if rtask != t and rtask.active:
                self.stop_task(rtask)
        # start this task
        if t.active:
            print(f'{t.name} already started, run time {t.duration}')
        else:
            t.active=True
            t.start_time = datetime.now()
            #t.duration = t.duration + t.start_time
            print(f'started {t.task_name} :: start time:{t.start_time} ')

    def stop_all(self)->None:
        for rtask in Task._registry:
            #if rtask.start_time !=None:
            self.stop_task(rtask)
                #print(rtask.start_time)

    def print_all(self)->None:
        for rtask in Task._registry:
            print(f'{rtask.task_name} active?: {rtask.active}')
            if hasattr(rtask, 'duration'): print(f'duration:{rtask.duration}')


'''t1= Task('t1')
t2= Task('t2')
t3= Task('t3')
tm = TaskTimerManager()
tm.start_task(t1)
time.sleep( 3 )
tm.start_task(t2)
time.sleep( 3 )
tm.start_task(t1)
time.sleep( 3 )
tm.stop_all()
tm.print_all()
'''