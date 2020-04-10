import random

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
jobId = 0

# Creates random memomory size and locations
def randMem(start, stop, steps):
       memReq = []
       for memories in range(20):
           randJb = random.randrange(start, stop, steps)
           memReq.append(randJb)
       return memReq

#This gets the status 
def status(stat):
    if stat == -1:
        return "Busy"
    elif stat == 0: 
        return "Free"
    else: return("Null Entry")

#To check the firstfit and allocates memory dynamically
def firstFit(memJobs, freeMem, memBlockSize):
  # Using linear search this line checks if the memory size is greater than or equals to the mem job size
     for i in range(len(memJobs)): 
      for j in range(len(memJobs)):
        if(Allocated[j] == 0 and ( memJobs[i]  <= memBlockSize[j] )):
          Allocated[j] = -1
          nonAllocated[j] = 0
          allocatedJobs.append(memJobs[i])
          busyMem.append(memBlockSize[j])
          frag.append(memBlockSize[j] - memJobs[i])
          freeMem[j ] = -1
          freeJob[j] = -1
          identity.append(j) 
          break 

def deallocation(allocated, memorySize):
    size = int(input("Enter size to deallocate: "))

    if(allocated[size - 1] != -1 and allocated[size + 1] != -1):
              memorySize[size - 1] = memorySize[size - 1] + memorySize[size] + memorySize[size + 1]
              print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| {2} \t\t\t\t| {3} \t\t\t\t| {4} \t\t\t\t".format( size - 1, memBlockSize[ size - 1], "____", "____", status(0)))
              print("\tLoc {0} \t\t\t\t| {1}K \t\t\t\t| {2} \t\t\t\t| {3} \t\t\t\t| {4} \t\t\t\t".format(size + 1 , "____", "____", "____", status(-2)))
              memBlockSize.pop(size)

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


    print("Memory:", freeMem)
    print("Jobs:" , memJobs)

    # Function call for the first fit algorithm
    firstFit(memJobs, freeMem, memBlockSize)
            
    #Pre output
    print("Busy Memory:" , busyMem)
    print("free Memory:" , freeMem)
    print("Busy Jobs:" , allocatedJobs)
    print("id:" , identity )
    print("Allocated Memory( 0 ):" , Allocated)
    print("nonAllocated Memory ( -1 ):" , nonAllocated )

    #Allocates  the free memory location ID to freeLocId 
    for i in range(len(nonAllocated)):
        if(nonAllocated[i] == -1):
            freeLocId.append(i)

    #remove all -1 from list to be reused
    for i in range(0, freeMem.count(-1)):
        freeMem.remove(-1)
        freeJob.remove(-1)

    def firstFitOutput():
        print("\tMemory location \t\t|", "memory BlockSize \t\t|", "Job Number\t\t\t|", "Job Size\t\t\t|", "Status\t\n")
        for mem in range(len( busyMem )):
            if( Allocated[mem] == -1): 
                print("\tLocation {0} \t\t\t\t| {1}K \t\t\t\t| J{2} \t\t\t\t| {3}K \t\t\t\t| {4} \t\t\t\t".format(identity[ mem ] , busyMem[ mem ], mem+1, allocatedJobs[mem], status(-1)))
                        
        for mem in range(len(freeMem)):  
            print("\tLocation {0} \t\t\t\t| {1}K \t\t\t\t| {2} \t\t\t| {3} \t\t\t\t| {4}".format( freeLocId[mem], freeMem[ mem ], " ___ " , "___", status(0) ))
      
    #function call for output
    #   generalOutput()
    firstFitOutput()

    counter = 0
    print("""
            Select any memory location to deallocate, 
            which is between two free memory
                
            1) Enter ( -1 ) to exit..
            2) Enter ( 1 ) to deallocate
            3) Enter ( 2 ) to see the First fit allocation
        """)
    option = int(input("Enter any option: "))

    while(option != -1):
        if(option == 1):
            print( deallocation(Allocated, memBlockSize) )
        elif(option == 2):
            firstFitOutput()
        
        print("""
                Select any memory location to deallocate, 
                which is between two free memory
                
                1) Enter ( -1 ) to exit..
                2) Enter ( 1 ) to deallocate
                3) Enter ( 2 ) to see the First fit allocation

        """)
        option = int(input("Enter any option: "))
