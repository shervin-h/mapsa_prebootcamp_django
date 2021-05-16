import random
import json
from web3 import Web3

MAIN_URL = "https://mainnet.infura.io/v3/bb055071bba745488eda95512a6d0035"
URL = 'https://8cf41633363c49a584fbfb0b556a5927.ropsten.rpc.rivet.cloud/'
URL = 'wss://ropsten.infura.io/ws/v3/bb055071bba745488eda95512a6d0035'

w3 = Web3(Web3.WebsocketProvider(URL))
# w3 = Web3(Web3.HTTPProvider(URL))


def _checking(_addr):
    '''
    ورودی تابع که استرینگ است که چک میشود ایا ادرس معتبری هست یا خیر
    false یا addrress در نهایت
    خارج میشود
    '''
    if not isinstance(_addr, str):
        print("ادرس بد وارد کردی باید یک استرینگ باشه")
        return False
    try:
        if not w3.isConnected():
            print("نت مشکل داره ")
            return False
        addr_ = Web3.toChecksumAddress(_addr)
        if not _addr:
            print("ادرس بدی وارد کردی شرمنده تم")
            return False
        return addr_
    except Exception as e:
        print(e)
        print("یه مشکلی وجود داره ×ـ× مثلا نتت ضعیفه")
        return False


def balance(_addr: str) -> float:
    """
    اینجا ادرس خواسته رو به تابع بدید
    توی خروجی یه عدد میده که همون باقیمانده ی حسابش هستش :)
    """
    addr_ = _checking(_addr)
    return float(w3.eth.get_balance(addr_) / 10**18)


def transfer(_to_addr: str, _value: float, private_key: str, public_key: str , n = 0 ):
    to_addr_ = _checking(_to_addr)
    public_key = _checking(public_key)
    if to_addr_ and public_key:
        try:
            if balance(public_key) < _value:
                print("پول ت کمه ، نمیتونی کمک کنی ")
                return False
            p = w3.eth.gas_price
            if n == 0:
                n = w3.eth.get_transaction_count(public_key)
            trancation = {
                'from': public_key,
                'to': to_addr_,
                "gas": "0x200000",
                "gasPrice": p,
                "nonce": n,
                "value": int(_value * 10**18),
            }
            raw_trx = w3.eth.account.privateKeyToAccount(
                private_key).sign_transaction(trancation)
            res = w3.eth.send_raw_transaction(raw_trx.rawTransaction).hex()
            return res
        except Exception as e:
            print(e)
            print("یک اتفاقی افتاده که من نمیدونم ....")
            return 0


# print (
#     transfer(acc.address ,
#                 0.01,
#                 "a49443970e8c717e218d312c0a7d1b390bea090cd3809011fd5cb926851f2e2b",
#                 "0xAf77fB90baCE88edad8be674232C4a072BdC29A3")
#     )

navid_wallet = "0xAf77fB90baCE88edad8be674232C4a072BdC29A3"
navid_private_key = "a49443970e8c717e218d312c0a7d1b390bea090cd3809011fd5cb926851f2e2b"

my_wallet = "0x9200e872f21B28E61600a62A3628ff30688e107C"
my_private_key = "e3aa1cb4960222f0731a884d96c377fa00ba64424fd0bb76ba97bb7fe272d937"

wallets = eval(open('wallets.json', 'r').read())


random_list = list()
random_balances = list()
for i in range(20):
    index = random.randint(0, len(wallets)-1)

    random_list.append(wallets[index])
    random_balances.append(balance(wallets[index]))


wallets_and_their_balances = dict(zip(random_list, random_balances))
mean = sum(random_balances)/len(random_balances)

print(mean)
print(wallets_and_their_balances)

for k, v in wallets_and_their_balances.items():
    if v < mean/10:
        transfer(k, 0.05, "e3aa1cb4960222f0731a884d96c377fa00ba64424fd0bb76ba97bb7fe272d937", "0x9200e872f21B28E61600a62A3628ff30688e107C")

print(balance(my_wallet))

# by Shervin Hasanzadeh
