"""
@package p2psp-simulator
splitter_core module
"""
import time
from .common import Common

class Splitter_core():
    
    def __init__(self):
        self.id = "S"
        self.alive = True
        self.chunk_number = 0
        print("Splitter Core initialized")
        
    def send_chunk(self, message, destination):
        if __debug__:
            print("S -",self.chunk_number, "->", destination)
        
        Common.UDP_SOCKETS[destination].put((self.id,message))

        
    def receive_chunk(self):
        time.sleep(0.05) #bit-rate control
        #C->Chunk, L->Lost, G->Goodbye, B->Broken, P->Peer, M->Monitor, R-> Ready
        return "C"

    def handle_arrivals(self):
        while(self.alive):
            #Thread(target=self.handle_a_peer_arrival).start()
            self.handle_a_peer_arrival()
    
    def run(self):
        raise NotImplementedError
