from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        """
            Constructor for the `Block` class.
            :param index:         Unique ID of the block.
            :param transactions:  List of transactions.
            :param timestamp:     Time of generation of the block.
            :param previous_hash: Hash of the previous block in the chain which this block is part of.                                        
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash # Adding the previous hash field
 
    def compute_hash(self):
        """
            Returns the hash of the block instance by first converting it
            into JSON string.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True) # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
 
    def __init__(self):
        """
            Constructor for the `Blockchain` class.
        """
        self.chain = []
        self.create_genesis_block()
 
    def create_genesis_block(self):
        """
            A function to generate genesis block and appends it to
            the chain. The block has index 0, previous_hash as 0, and
            a valid hash.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
 
    @property
    def last_block(self):
        """
            A quick pythonic way to retrieve the most recent block in the chain. Note that
            the chain will always consist of at least one block (i.e., genesis block)
        """
        return self.chain[-1]


#hahahahahahahah