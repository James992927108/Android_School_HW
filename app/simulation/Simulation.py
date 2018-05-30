import json
import time

import numpy as np
from app import Config
from app.logging import info
from app.network.Network import Network
from colorama import Fore

import traci
import traci.constants as tc


def current_milli_time(): return int(round(time.time() * 1000))


class Simulation(object):
    """ here we run the simulation in """

    # the current tick of the simulation
    tick = 0

    # last tick time
    lastTick = current_milli_time()


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

        complete_Veh_num = 0
        incomplete_Veh_num = 0  

        while cls.tick < 100:   
            # Do one simulation step
            cls.tick += 1
            traci.simulationStep()      

            # print np.array(traci.vehicle.getIDList()).shape
            # print traci.vehicle.getIDCount()
            ArrivedIDList = traci.simulation.getArrivedIDList()
            if ArrivedIDList is not None:
                
                for vehID in traci.vehicle.getIDList():
                    print ("step {} vehID {} WaitingTime {} Distance {}".format(
                        cls.tick,
                         vehID,
                         traci.vehicle.getWaitingTime(vehID),
                         traci.vehicle.getDistance(vehID)
                         ))

                # for ArrivedID in ArrivedIDList:
                #     print("Step:{} CarID:{}".format(
                #         cls.tick,
                #         ArrivedID
                #         ))
                #     complete_Veh_num += 1
        
        print complete_Veh_num
        incomplete_Veh_num = traci.vehicle.getIDCount()
        print incomplete_Veh_num

         
        # print(traci.simulation.getContextSubscriptionResults())
        
            # # if (cls.tick % 100) == 0 and Config.parallelMode is False:
            # print("{} -> Step:{}# Driving cars: {} / {} # avgTripDuration: {} ({}) # avgTripOverhead:{} "
            #         .format(
            #             str(Config.processID),
            #             str(cls.tick),
            #             str(traci.vehicle.getIDCount()),
            #             str(CarRegistry.totalCarCounter),
            #             str(CarRegistry.totalTripAverage),
            #             str(CarRegistry.totalTrips),
            #             str(CarRegistry.totalTripOverheadAverage)
            #         ))
