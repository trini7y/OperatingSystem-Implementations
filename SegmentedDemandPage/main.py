from random import random, randrange
import JMT
import MMT
import SMT

jobsList = []
memoryList = []
tableId = []
segTable = []

jobTable = JMT.JobTable(tableId, jobsList)
memoryTable = MMT.mainMemory(tableId, memoryList)
    
def randMem(start, stop, steps):
       memReq = []
       for memories in range(10):
           randJb = randrange(start, stop, steps)
           memReq.append(randJb)
       return memReq

jobs = randMem(100, 300, 5)
memory = randrange(5, 60, 5)


for identity in range(10):
    tableId.append(identity)
    jobsList.append( jobs[identity] )
    memoryList.append(memory)

print("Job Table", jobTable.getSize() )


def createSegment():
        sizes = jobTable.getSize()
        segment = {}
        segList = []
        i = 0
        total = 0
        for key, value in enumerate( sizes ):
            # print(sizes[key])
            while ( sizes[key] > 0 ):
                n = int( ( random() * ( 0.5 * sizes[key] ) + 60) )
                if(sizes[key] < 60):
                    n = sizes[key]
                sizes[key] -= n
                segList.append(n)
                # mapSeg = [ i for i in range(len( segList )) if (segList[i] + segList[i+1] ) == segList[i]]
                # segment[value] = mapSeg
                # segments = SMT.Segment(i, n, jobTable.jobId())
                
                i += 1
            # print(segments.jobId()) 
        print("Segment",segList)   
        return segment

# def twoSum(targ, nums):
#     found = {}
#     for num in targ:
#         target = num
#         for key, value in enumerate(nums):
#             sub = target - value
#             if sub in found :
#                 return[ found[value], key]
#             else:
#                 found[key] = value
#     return found

# print( twoSum(jobTable.getSize(), ) )
# createSegment()
print(createSegment() )

# for i in 
# if __name__ == "__main__":
   
   