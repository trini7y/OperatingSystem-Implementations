import threading
import time
import random


quantumTime = 3
arrivalTime = 0
# delayTime = 0
readyState = []
getDelay = []
DoneProcess = []
threadLock = threading.Lock()

def randMem(start, stop, steps):
       memReq = []
       for memories in range(5):
           randJb = random.randrange(start, stop, steps)
           memReq.append( randJb )
       return memReq

burstTime = randMem(1, 6, 1)

print("Burst Time:", burstTime )

#This line loads the process
def loadProcess( process = randMem(1, 10, 3)):
    processes = []
    for i in range( len(process) ):
        processes.append( process[i] )
    return processes

print("Processes in the HOLD state", loadProcess())
#The returns each burst time
def getBurstTime(burstTime):
    for burst in burstTime:
        threadLock.acquire()
        return burst
        
        # if ()
def updateReadyQueue( readyState ):
    for i in range(len(loadProcess())):
        readyState.append(loadProcess()[i])
        threadLock.acquire()
        if (len(readyState) == 0):
            print("Ready queue has been popped ")
            threadLock.release()

#This allocates CPU for processing
def cpuScheduler(readyQueue, burstTime, quantumTime):
    number = 1
    undoneProcess = 0
    delay = 0
    timeStamp = []
    process = {}
    while True:
        for key, value in enumerate( readyQueue ):
            print( "P{0} is running".format(key) )
            print("P{0} = {1}".format(key, readyQueue[key]))
            delay += 1
            process[value] = readyQueue[key]
            number += 1
            print("Bursttime: ", burstTime)
            print( delay)
            threadLock.acquire()
            remainingTime = burstTime - delay
            readyQueue.pop(key)
            print(readyQueue)
            timeStamp.append(remainingTime)
            if (delay == quantumTime):
                print("alert lock exeeded quantum time")
                undoneProcess = readyQueue[key]
                threadLock.release()
                readyQueue.append(undoneProcess)
            else:
                DoneProcess.append(readyQueue[key])
            if (number == key):
                key = 1
                number = 0
        

        
# print("Ready Queue:", updateReadyQueue() )
if __name__ == "__main__":

        x = threading.Thread(target=cpuScheduler, args=( readyState, getBurstTime( burstTime ), quantumTime) )
        readyqueue = threading.Thread(target=updateReadyQueue, args=(readyState, ))
        x.start()
        readyqueue.start()