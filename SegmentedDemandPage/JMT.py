class JobTable:

    def  __init__(self, jobId, size):
        self.jobId = jobId
        self.size = size
        self.pointer = None

    
    def setPointer(self, pointer):
        self.pointer  = pointer
        
    def getJobId(self):
        return self.jobId
    
    def getSize( self ):
        return self.size
    
    def getPointer(self):
        return self.pointer 