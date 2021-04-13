class Segment:

    def __init__(self, segmentNo, size, jobId):
        self.segmentNo = segmentNo
        self.size = size
        self.jobId =  jobId
        self.pointer = None
        self.status = ''

    
    def setStatus(self, status ):
        self.status = status
    
    def setPointerToPMT(self, pointer):
        self.pointer = pointer 

    def getSegmentNo(self):
        return self.segmentNo

    def getSize(self):
        return self.size
    
    def getStatus(self):
        return self.status
    
    def getPMT(self):
        return self.pointer
    