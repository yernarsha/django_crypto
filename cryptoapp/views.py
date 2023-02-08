from django.shortcuts import render

import requests
import json

# Create your views here.

def home(request):
    r = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(r.content)
#    print(api)

    r2 = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')
    api2 = json.loads(r2.content)

    return render(request, 'cryptoapp/index.html', {"api": api, "price": api2})

def prices(request):
    if request.method == "POST":
        crypto = request.POST['crypto']

        r = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto.upper()}&tsyms=USD,EUR')
        api = json.loads(r.content)
        return render(request, 'cryptoapp/prices.html', {'crypto': api, 'search': crypto})
    
    return render(request, 'cryptoapp/prices.html', {})