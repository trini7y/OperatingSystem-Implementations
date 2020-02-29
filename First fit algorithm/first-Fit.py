import random

freeMem = []
busyMem = []
identity = []
busyJob = []
frag = []
flag = []
allocated = []
memLoc = []

# Creates random memomory size and locations
def randMem(start, stop, steps):
       memReq = []
       for memories in range(20):
           randJb = random.randrange(start, stop, steps)
           memReq.append(randJb)
       return memReq
#This gets the status 
def status(stat):
    if stat == True:
        return "Busy"
    else: return "Free"

#To check the firstfit and allocates memory dynamically
def firstFit(memJobs, freeMem, memBlockSize):
     for i in range(len(memJobs)):
      for j in range(len(memJobs)):
        if(flag[j] == 0 and (memJobs[i] <= memBlockSize[j]) ):
          flag[j] = -1
          allocated[j] = 0
          busyMem.append(memBlockSize[j]);
          frag.append(memBlockSize[j] - memJobs[i])
          freeMem[j ] = -1
          identity.append(j)
          break

if __name__ == "__main__":
  
      #Assign random memory size and locations 
      memJobs = randMem(10, 200, 3)
      memLocation = randMem(1000, 5000, 4)
      memBlockSize = randMem(10, 200, 10)

      #store all values in 
      for i in range(len(memBlockSize)):
            freeMem.append(memBlockSize[i])
            flag.append(0)
            allocated.append(-1)

      # for i in range(0, ):
      #       freeMem.remove(0)

      print("Mem:" , freeMem)
      print("Jobs:" , memJobs)


      firstFit(memJobs, freeMem, memBlockSize)

      print("Busy:" , busyMem)
      print("freeMem:" , freeMem)
      print("id:" , identity )
      print("Flag:" , flag)
      print("allocated:" , allocated )

     
      
      print("busyJob:", busyJob)
      print("busyJob:", busyJob) 
    
      print("Memory location \t|", "memory BlockSize \t|", "Job Number\t|", "Job Size\t|", "Status\t|")
      for mem in range(len( memBlockSize)):
          if( flag[mem] == -1): 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t | {4} \t\t\t\t".format(identity[mem], memBlockSize[identity[mem]], mem+1, memJobs[mem], status(True)))
          else: 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t| {4}".format(identity[mem], memBlockSize[mem], mem+1, memJobs[mem], status(False) ))