import JMT
import MMT
import random

 

def randMem(start, stop, steps):
       memReq = []
       for memories in range(10):
           randJb = random.randrange(start, stop, steps)
           memReq.append(randJb)
       return memReq



if __name__ == "__main__":

    jobs = randMem(10, 200, 3)
    memory = random.randrange(5, 20, 5)
    for identity in range(10):
        jobTable = JMT.JobTable(identity, jobs[identity])
        memoryTable = MMT.mainMemory(identity, memory )
        print( memoryTable.getAddress())
    
    
    