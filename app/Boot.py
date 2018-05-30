import os, sys


sys.path.append(os.path.join(os.environ.get("SUMO_HOME"), "tools"))

from app.logging import info
from app.network.Network import Network
from app.simulation.Simulation import Simulation

from colorama import Fore
from sumo import SUMOConnector, SUMODependency
import Config
import traci, sys, os
import thread
import time


# uuid4()
def start(processID, parallelMode,useGUI):
    """ main entry point into the application """
    Config.processID = processID
    Config.parallelMode = parallelMode
    Config.sumoUseGUI = useGUI

    # Check if sumo is installed and available
    SUMODependency.checkDeps()
    info('# SUMO-Dependency check OK!', Fore.GREEN)

    # Load the sumo map we are using into Python
    Network.loadNetwork()
    info(Fore.GREEN + "# Map loading OK! " + Fore.RESET)
    info(Fore.CYAN + "# Nodes: " + str(Network.nodesCount()) + " / Edges: " + str(Network.edgesCount()) + Fore.RESET)

    # Start sumo in the background
    SUMOConnector.start()
    info("\n# SUMO-Application started OK!", Fore.GREEN)

    # Start the simulation
    Simulation.start()
    # Simulation ended, so we shutdown
    info(Fore.RED + '# Shutdown' + Fore.RESET)
    
    traci.close()
    sys.stdout.flush()
    return None
