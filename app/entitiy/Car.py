import traci

class Car:
    def __init__(self,id):
        self.id = id
        self.waitingTime = self._getAccumulatedWaitingTime(id)
        self.duration = 0

    @classmethod
    def _getAccumulatedWaitingTime(self,id):
        return traci.vehicle.getAccumulatedWaitingTime(id)
    
    # @classmethod
    # def _getDistance(self,id):
    #     return traci.vehicle.getDistance(id)
    
    # @classmethod
    # def _getSpeed(self,id):
    #     return traci.vehicle.getSpeed(id)
    
    # @classmethod
    # def _getduration(self,id):
    #     speed = self ._getSpeed(id)
    #     print speed   
    #     if speed == 0 :
    #         speed = 1
    #     return self._getDistance(id)
