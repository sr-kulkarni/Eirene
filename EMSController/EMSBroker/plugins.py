import consul

class ConsulPlugin:
	
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
			sDict[item[0]] = item[1]['Address']

        	return sDict











