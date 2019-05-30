from blockchain import *

blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))
    
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
 
