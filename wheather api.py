import requests

url ="http://api.weatherapi.com/v1/current.json"

access_key = "3594e1b209c549958f8134453231401"

sehir = input("Şehir giriniz: ")

response = requests.get(url,params={

    "key": access_key,
    "q": sehir
})
sonuc = response.json() 

sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havadurumu} derece ve {text}.")