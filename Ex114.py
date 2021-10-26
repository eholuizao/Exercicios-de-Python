import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("Site não está acessível.")
else:
    print("Site está acessível.")
