class mainMemory:

    def __init__(self, memoryId, size):
        self.memoryId = memoryId
        self.size = size
        self.status = ''
        self.pageFrameNo = None
    
    def getMemoryId( self ):
        return self.memoryId
    
    def getSize( self ):
        return self.size
    
    def getStatus( self ):
        return self.status

    def getPageFrameNo( self ):
        return self.pageFrameNo
        
    def setStatus(self, status):
        self.status = status
    
    def setPageFrameNo(self, pageFrameNo):
        self.pageFrameNo =  pageFrameNo