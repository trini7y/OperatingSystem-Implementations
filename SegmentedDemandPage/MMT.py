class mainMemory:

    def __init__(self, memoryId, address):
        self.memoryId = memoryId
        self.address = address
        self.status = ''
        self.pageFrameNo = None
    
    def getMemoryId( self ):
        return self.memoryId
    
    def getAddress( self ):
        return self.address
    
    def getStatus( self ):
        return self.address

    def getPageFrameNo( self ):
        return self.pageFrameNo
        
    def setStatus(self, status):
        self.status = status
    
    def setPageFrameNo(self, pageFrameNo):
        self.pageFrameNo =  pageFrameNo