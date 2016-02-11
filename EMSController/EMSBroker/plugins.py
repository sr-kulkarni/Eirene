import consul

class ConsulPlugin:
	
	#More Try/Except blocks needed here. 
	#This is bare minimum functionality.Skeleton seems to be working ok
	
	def __init__(self,params=None):
		print "Consul Initiated!"
		self.client = consul.Consul(params)


	def putService(self,servDict,params=None):
        	
		if params==None :self.client = consul.Consul()
                else: self.client = consul.Consul(params)
		try:
                	for item in servDict.items():
                        	self.client.agent.service.register(name=item[0],address=item[1])
        	except:
                	raise Exception("Some problem with Consul!")

	def getService(self,params=None):
        	sDict = {}

		if params==None :self.client = consul.Consul()
		else: self.client = consul.Consul(params)

		serviceList = self.client.agent.services()
		for item in serviceList.items():
			if item[0] == "consul":pass
			else:
				sDict[item[0]] = item[1]['Address']

        	return sDict

	def getServiceDetails(self,name,params=None):
		sDict = {}

		if params==None :self.client = consul.Consul()
                else: self.client = consul.Consul(params)
		if name=="consul":
			return sDict		
	
		serviceList = self.client.agent.services()
                for item in serviceList.items():
			if item[0]==name:
				sDict[item[0]] = item[1]['Address']
				return sDict
		return sDict
	
	def deleteService(self,name,params=None):
		if params==None :self.client = consul.Consul()
                else: self.client = consul.Consul(params)
		if name=="consul":return
		serviceList = self.client.agent.services()
                for item in serviceList.items():
                        if item[0]==name:
				self.client.agent.service.deregister(item[1]['ID'])










