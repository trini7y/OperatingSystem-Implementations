import random

freeMem = []
busyMem = []
identity = []
busyJob = []
frag = []
Allocated = []
nonAllocated = []
freeLocId = []

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
  # Using linear search this line checks if the memory size is greater than or equals to the mem job size
     for i in range(len(memJobs)):
      for j in range(len(memJobs)):
        if(Allocated[j] == 0 and (memBlockSize[j] >= memJobs[i]) ):
          Allocated[j] = -1
          nonAllocated[j] = 0
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

      #store all values in free memory and assigns zero to allocated and -1 to nonAllocated blocks 
      for i in range(len(memBlockSize)):
            freeMem.append(memBlockSize[i])
            Allocated.append(0)
            nonAllocated.append(-1)


      print("Mem:" , freeMem)
      print("Jobs:" , memJobs)

      # Function call for the first fit algorithm
      firstFit(memJobs, freeMem, memBlockSize)

      print("Busy:" , busyMem)
      print("freeMem:" , freeMem)
      print("id:" , identity )
      print("Allocated:" , Allocated)
      print("nonAllocated:" , nonAllocated )

     #Allocats  the free memory location ID to freeLocId 
      for i in range(len(nonAllocated)):
          if(nonAllocated[i] == -1):
              freeLocId.append(i)
               

      print("remainID:", freeLocId)
      print("len:", len(freeLocId+identity))

      print("Memory location \t|", "memory BlockSize \t|", "Job Number\t|", "Job Size\t|", "Status\t|")
      for mem in range(len( memBlockSize)):
          if( Allocated[mem] == -1): 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t| {4} \t\t\t\t".format(identity[mem], memBlockSize[ identity[mem]  ], mem+1, memJobs[mem], status(True)))
          else: 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3} \t\t\t\t| {4}".format(freeLocId[mem], memBlockSize[ freeLocId[mem] ], mem+1, "____", status(False) ))