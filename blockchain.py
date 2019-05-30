from simpleblock import *

class Blockchain: 
    maxNonce = 2**32
    diff = 10
    target = 2 ** (256-diff)
    block = Block("Genesis")
    head = block
    
    def add(self,block):
        block.previous_hash = self.block.hash()
        block.blockNumber = self.block.blockNumber + 1
        
        self.block.next = block
        self.block = self.block.next
        
    def mine(self,block):
        for n in range(self.maxNonce):
            if int(block.hash(),16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce +=1
