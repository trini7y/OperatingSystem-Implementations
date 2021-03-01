import random
# import memory_blocks
# import jobs

freeMem = []
busyMem = []
identity = []
freeJob = []
busyJob = []
frag = []
Allocated = []
nonAllocated = []
freeLocId = []
allocatedJobs = []
remainingJobs = []
jobId = []


# memObject = memory_blocks.MemoryBlocks(identity, busyMem, frag)



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
            allocatedJobs.append(memJobs[i])
            busyMem.append(memBlockSize[j])
            frag.append(memBlockSize[j] - memJobs[i])
            freeMem[j] = -1
            freeJob[j] = -1
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
            freeJob.append(memJobs)
            Allocated.append(0)
            nonAllocated.append(-1)


      print("Mem:", freeMem)
      print("Jobs:" , memJobs)

      # Function call for the first fit algorithm
      firstFit(memJobs, freeMem, memBlockSize)

      print("Busy:" , busyMem)
      print("Busy Jobs:" , allocatedJobs)
      print("freeMem:" , freeMem)
      print("id:" , identity )
      print("Allocated:" , Allocated)
      print("nonAllocated:" , nonAllocated )

     #Allocats  the free memory location ID to freeLocId 
      for i in range(len(nonAllocated)):
          if(nonAllocated[i] == -1):
              freeLocId.append(i)

      #remove all -1 from list to be reused
      for i in range(0, freeMem.count(-1)):
            freeMem.remove(-1)
            freeJob.remove(-1)

      print("remainID:", freeLocId)
      print("len:", len(freeLocId+identity))

      print("Memory location \t|", "memory BlockSize \t|", "Job Number\t|", "Job Size\t|", "Status\t|")


      for mem in range(len( busyMem )):
          if( Allocated[mem] == -1): 
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t| {4} \t\t\t\t".format(identity[ mem ] , busyMem[ mem ], mem+1, allocatedJobs[mem], status(True)))
                
      for mem in range(len(freeMem)):  
                print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| {2} \t\t\t| {3} \t\t\t\t| {4}".format( freeLocId[mem], freeMem[ mem ], " ___ " , "___", status(False) ))

# print(memObject.getmemBlockSize())