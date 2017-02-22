class Node:
	def __init__(self, cargo=None, next=None): 
	    self.car = cargo 
	    self.cdr = next    
  	def __str__(self): 
	    return str(self.car)

	def get_data(self):
		return self.car
	def set_data(self, cargo):
		self.car = cargo
	def get_next(self):
        return self.cdr
    def set_next(self,next)
    	self.cdr = next