class MemoryBlocks:

	status = True

	def __init__(self, id, memBlockSize, fragmentation):
		self.id = id
		self.memBlockSize = memBlockSize
		self.fragmentation = fragmentation
		
	
	#getter for memory blocks
	def getmemBlockSize(self):
		return self.memBlockSize
	       
	def getFragmentation(self):
		return self.fragmentation

	def checkStatus(self, status):
		if(self.status == True):
			return "Busy"
		else: return "Free"
	
