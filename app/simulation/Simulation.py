import json
import time

import numpy as np
from app import Config
from app.logging import info
from app.network.Network import Network
from app.entitiy.Car import Car

from colorama import Fore

import traci
import traci.constants as tc


class Simulation(object):
    """ here we run the simulation in """

    # the current tick of the simulation
    tick = 0

    complete_Veh_num = 0
    incomplete_Veh_num = 0

    total_waitingTime = 0
    total_duration = 0
    carList = {}

    @classmethod
    def start(cls):
        """ start the simulation """
        info("# Start adding initial cars to the simulation", Fore.MAGENTA)
        cls.loop()

    @classmethod
    # @profile
    def loop(cls):
        """ loops the simulation """
        # start listening to all cars that arrived at their target
        traci.simulation.subscribe((tc.VAR_ARRIVED_VEHICLES_IDS,))
        # while traci.simulation.getMinExpectedNumber() > 0:

        for tlsid in Network.tlsIds:
            print traci.trafficlight.getPhaseDuration(str(tlsid))
            # print "{} {}".format(tlsid,traci.trafficlight.getPhaseDuration(str(tlsid)) / 1000 )
                
        while cls.tick < 1:
            # Do one simulation step
            cls.tick += 1
            traci.simulationStep()

            for vehID in traci.vehicle.getIDList():
                c = Car(vehID)
                cls.carList[c.id] = c
            arrivedIDList = traci.simulation.getArrivedIDList()
            if arrivedIDList is not None:
                for vehID in arrivedIDList:
                    cls.carList[vehID].duration = cls.tick
                cls.complete_Veh_num += 1

        cls.incomplete_Veh_num = traci.vehicle.getIDCount()       
        for i in cls.carList:
            cls.total_waitingTime += cls.carList[i].waitingTime
            cls.total_duration += cls.carList[i].duration
        print "waitingTime:{} duration:{}".format(cls.total_waitingTime,cls.total_duration)

