import urllib.request as req
def getData(url):
    #建立一個Request物件， 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "Cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼.
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")  #用 BeautifulSoup 協助解析 HTML 格式文件
    titles=root.find_all("div", class_="title")  #尋照class="title" 的div標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    #抓上一頁連結
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]
pageURL="https://www.ptt.cc/bbs/gossiping/index.html"
count=0
while count<5:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
    print("****************************")