#%%
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)

#%%
if ret:
  print(ret)
else:
  print('A requisição falhou')
  
# %%
ret.text

# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
print(f"20 Dólares hoje custam {(float(dolar['bid']) * 20):.2f} reais")

# %%
def cotacao(valor, moeda):
  url = f'https://economia.awesomeapi.com.br/last/{moeda}'
  ret = requests.get(url)
  dolar = json.loads(ret.text)[moeda.replace('-','')]
  print(f"{valor} {moeda[:3]} hoje custam {(float(dolar['bid']) * valor):.2f} {moeda[-3:]}")
  
# %%
cotacao(20, 'USD-BRL')

# %%
cotacao(20, 'JPY-BRL')

# %%
def error_check(func):
  def inner_func(*args, **kwargs):
    try:
      func(*args, **kwargs)
    except:
      print(f"{func.__name__} falhou")
  return inner_func

#%%
@error_check
def multi_moeda(valor, moeda):
  url = f'https://economia.awesomeapi.com.br/last/{moeda}'
  ret = requests.get(url)
  dolar = json.loads(ret.text)[moeda.replace('-','')]
  print(f"{valor} {moeda[:3]} hoje custam {(float(dolar['bid']) * valor):.2f} {moeda[-3:]}")
  

#%%
multi_moeda(20, "USD-BRL")
multi_moeda(20, "EUR-BRL")
multi_moeda(20, "BTC-BRL")
multi_moeda(20, "JPY-BRL")
multi_moeda(20, "RPL-BRL")

# %%
import backoff
# %%
