import random

freeMem = []
busyMem = []
identity = []
frag = []
busyJob = []
waitJob = []
memLoc = []

# Creates random memomory size and locations
def randMem(start, stop, steps):
       memReq = []
       for memories in range(20):
           randJb = random.randrange(start, stop, steps)
           memReq.append(randJb)
                #print("J{0} | {1}K".format(jobNumbers, memReq))
       return memReq
#This gets the status 
def status(stat):
    if stat == True:
        return "Busy"
    else: return "Free"

#To check the firstfit and allocates memory dynamically
def firstFit(memJobs, freeMem, memBlockSize):
     for i,  in range(len(memJobs)):
      for j in range(len(memJobs)):
        if(memJobs[i] <= freeMem[j]):
            busyMem.append(memBlockSize[j]);
            busyJob.append(memJobs[i])
            identity.append(i)
            memLoc.append(j)
            frag.append(freeMem[j] - memJobs[i])
            waitJob.append(memJobs[i])
            print( i, memJobs[i], freeMem[j])
            freeMem[j] = -1
            print( i, memJobs[i], freeMem[j])
            break
 
if __name__ == "__main__":
  
      #Assign random memory size and locations 
      memJobs = randMem(10, 200, 3)
      memLocation = randMem(1000, 5000, 4)
      memBlockSize = randMem(10, 200, 10)

      #store all values in 
      for i in range(len(memBlockSize)):
            freeMem.append(memBlockSize[i])

      print("Mem:" , freeMem)
      print("Jobs:" , memJobs)

      firstFit(memJobs, freeMem, memBlockSize)

      print("Busy:" , busyMem)
      print("freeMem:" , freeMem)
      print("id:" , identity )

      #delete -1 on the list
      for i in range(0, freeMem.count(-1)):
            freeMem.remove(-1)

      print("NEw freeMem", freeMem)
      print("Memory location \t|", "memory BlockSize \t|", "Job Number\t|", "Job Size\t|", "Status\t|")
      for mem in enumerate(memBlockSize):
          if( busyMem[mem] in memBlockSize):
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t | {4} \t\t\t\t".format(memLoc[mem], busyMem[mem], identity[mem], memJobs[mem], status(True)))
          else: 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t| {4}".format(memLoc[mem], busyMem[mem] , identity[mem], memJobs[mem], status(False) ))