
### IMPORTS ###
import random

# Libraries
import numpy as np
from hist_service import HistWorker
from crypto_evolution import CryptoFolio
# Local
from peas.peas.networks.rnn import NeuralNetwork

class Trading_task(Object):

    EPSILON = 1e-100

    start_idx = 0


    def __init__(self):
        self.hs = HistWorker()
        self.end_idx = len(self.hs.currentHists["DASH"])
        self.port = CryptoFolio()
        self.strt_amnt = self.port.start

    
    def evaluate(self, network, verbose=False):
        if not isinstance(network, NeuralNetwork):
            network = NeuralNetwork(network)
        
        network.make_feedforward()
