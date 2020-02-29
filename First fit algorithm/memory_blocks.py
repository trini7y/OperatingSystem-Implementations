class MemoryBlocks:
	
	def __init__(this, memLocation, memBlockSize, status):

		this.memLocation = memLocation
		this.memBlockSize = memBlockSize
		this.status = status
	
	#getter for memory blocks
	def getmemLocation():
		return this.memLocation

	def getmemBlockSize():
		return this.memBlockSize

	def getStatus():
		return this.status

	#setters for memory blocks
	def setmemLocation(this, memLocation):
		this.memLocation = memLocation

	def setmemBlockSize(this, memBlockSize):
		this.memBlockSize = memBlockSize

	def setStatus(this, status = False):
		this.status = status