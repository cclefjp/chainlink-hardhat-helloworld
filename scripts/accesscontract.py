from web3 import Web3
from web3.contract import Contract

print('a')
w3 = Web3(Web3.HTTPProvider('http://172.17.0.2:8545'))

print('w3.isConnected:', w3.isConnected())

print('b')
hwadd = '0xf44872063E64Ac342E92baB69c3478B159bEa180'

print('c')
abi = '[{"inputs":[{"internalType":"string","name":"initialMessage","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"message","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"newMessage","type":"string"}],"name":"updateMessage","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
hwc = w3.eth.contract(hwadd, abi=abi)

from pprint import pprint
pprint(hwc.__dict__)

print('d')

print('e')
message_func = hwc.functions.message()

print('f')
message_result = message_func.call()
print('message_result:', message_result)