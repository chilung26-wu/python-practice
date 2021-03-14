import urllib.request

url = "https://nbk.acad.ncku.edu.tw/netcheckin/images/Logo.png"
response = urllib.request.urlopen(url)
img = response.read()
response.close()
fp = open("fchart05.png", "wb")
fp.write(img)
fp.close()


