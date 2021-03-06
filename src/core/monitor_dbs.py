"""
@package simulator
monitor_dbs module
"""
from queue import Queue
from .common import Common
from .peer_dbs import Peer_DBS

class Monitor_DBS(Peer_DBS):
    
    def __init__(self,id):
        super().__init__(id)
        self.buffer_size //= 2
        print("DBS initialized by monitor")

    def say_hello(self, peer):
        hello = (-1,"H")
        Common.UDP_SOCKETS[peer].put((self.id,hello))
        print("Hello sent to", peer)

    def connect_to_the_splitter(self):
        hello = (-1,"M")
        self.splitter["socketTCP"].put((self.id,hello))

    def complain(self, chunk_position):
        lost = (chunk_position,"L")
        self.splitter["socketUDP"].put((self.id,lost))


