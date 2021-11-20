import requests

url = 'https://www.douban.com/game/25931998/comments?start=20&sort=score'
my_headers={
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
r = requests.get(url, headers=my_headers)


print(r.status_code)
# print(r.text)

from lxml import etree
selector=etree.HTML(r.text)

selector.xpath('//div[@class="user-info"]')


username=selector.xpath('//div[@class="user-info"]/a/text()')
print(username)
len(username)

star=selector.xpath('//div[@class="user-info"]/span[2]/@class')
print(star)
len(star)

comment = selector.xpath('//span[@class="short"]/text()')
print(comment)
len(comment)


temp = selector.xpath('//div[@class="user-info"]')
if not temp[0].xpath('./span[2]/@class'):
    print("allstar0")

for everyElement in temp:
    username = everyElement.xpath('./a/text()')
    star = everyElement.xpath('./span[2]/@class')
    if not star:
        start = []
        star.append("allstar0")
    print(f"{username}::{star}")


temp1 = selector.xpath('//div[@class="info"]')
for everyElememt in temp1:
    username = everyElememt.xpath('./div/a/text()')
    star = everyElememt.xpath('./div/span[2]/@class')
    if not star:
        star.append("allstar0")
    comment = everyElememt.xpath('./p/span[@class="short"]/text()')
    print(f"{username}::{star}::{comment}")

temp2 = selector.xpath('//div[@class="info"]')
# 以追加写入方式打开文件
with open("./game_short.txt", "w+") as f:
    for everyElement in temp2:
        username = everyElement.xpath('./div/a/text()')
        star = everyElement.xpath('./div/span[2]/@class')
        if not star:
            star.append("allstar0")
        comment = everyElement.xpath('./p/span[@class="short"]/text()')
        game_short = f"{username}::{star}::{comment}=="
        f.write(game_short)
