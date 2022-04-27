import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.r6esportsbr.com')
except urllib.error.URLError:
    print('O site r6esportsbr não está acessível no momento.')
else:
    print('Consegui acessar o site r6esportsbr com sucesso!')
    print(site.read)