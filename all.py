from ZakaZaka import *
from SteamPay import *
from SteamBuy import *
from SteamSearch import *

name=input()
print('Steam\n'+ResultOfSearch(name)[0])
print('ZakaZaka\n'+GetPriceFromZakaZaka(name))
print('SteamPay\n'+GetPriceFromSP(name))
print('SteamBuy\n'+GetPriceFromSB(name))
