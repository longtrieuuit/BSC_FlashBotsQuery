# import dependencies
import pickle,json
from web3 import Web3, HTTPProvider

# instantiate a web3 remote provider
w3 = Web3(HTTPProvider('https://bsc-dataseed1.binance.org/'))


file_path = 'abi/FalshQuey.ABI'
with open(file_path) as json_file:
    ContractAbi = json.load(json_file)


ContractAddress = '0xa37E1C602E97c482d2e2aD6050c2346a654454Ed'
FlashQuery = w3.eth.contract(address=ContractAddress, abi=ContractAbi)

pair_list =[ Web3.toChecksumAddress("0x3b9aa711d1d90a4f8639f66c227881729a3317f2")]
for i in range(2):
    QueryResult = FlashQuery.functions.getReservesByPairs(pair_list).call()
    decimals = 18
    precision = 10 ** int(decimals)
    print(QueryResult)

    # for reserve0, reserve1, reserve2  in QueryResult:
    #     print(reserve0/precision, reserve1/precision, reserve2 )



# print(reserve0, reserve1, reserve2 )
