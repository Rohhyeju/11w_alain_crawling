import urllib.request as req
from bs4 import BeautifulSoup
f = open("./10조_노혜주_출력결과.txt", "w")

week_num = 1
ranking=1
while True:
  code = req.urlopen("https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&CID=0&Year=2022&Month=1&Week={}&BestType=Bestseller&SearchSubBarcode=".format(week_num))
  soup = BeautifulSoup(code, "html.parser")
  
  title = soup.select("a.bo3 > b")
  
  if week_num == 6:
    break

  for i in range(len(title)): 
    print(f'{week_num}주차 {ranking}위 {title[i].string}')
    f.write(f'{week_num}주차 {ranking}위 {title[i].string} \n')
    ranking +=1
  week_num += 1
  ranking=1
f.close()

import urllib.request as req
from bs4 import BeautifulSoup
f = open("./10조_송민정_출력결과.txt", "w")
a=[]
b=[]
c=[]
d=[]
e=[]

#학생1이 크롤링한 코드를 이용하여 순위에 따른 책이름을 출력함.
week_num = 1
ranking=1


while True:
  code = req.urlopen("https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&CID=0&Year=2022&Month=1&Week={}&BestType=Bestseller&SearchSubBarcode=".format(week_num))
  soup = BeautifulSoup(code, "html.parser")
  
  title = soup.select("a.bo3 > b")
  
  if week_num == 6:
    break

  for i in range(len(title)):
    if week_num==1 :
      a.append(title[i].string)

    elif week_num==2:
      b.append(title[i].string)
    elif week_num==3:
      c.append(title[i].string)
    elif week_num==4:
      d.append(title[i].string)
    else :
      e.append(title[i].string)

  week_num += 1
  ranking=1

num=int(input('알고싶은 책의 순위를 입력하세요.:'))
print(f'1주차 {num}위는 {a[num-1]}입니다.')
f.write(f'1주차 {num}위는 {a[num-1]}입니다. \n')
print(f'2주차 {num}위는 {b[num-1]}입니다.')
f.write(f'2주차 {num}위는 {b[num-1]}입니다. \n')
print(f'3주차 {num}위는 {c[num-1]}입니다.')
f.write(f'3주차 {num}위는 {c[num-1]}입니다. \n')
print(f'4주차 {num}위는 {d[num-1]}입니다.')
f.write(f'4주차 {num}위는 {d[num-1]}입니다. \n')
print(f'5주차 {num}위는 {e[num-1]}입니다.')
f.write(f'5주차 {num}위는 {e[num-1]}입니다. \n')

code = req.urlopen("https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&CID=0&Year=2022&Month=1&Week=5&BestType=MonthlyBest&SearchSubBarcode=")
soup = BeautifulSoup(code, "html.parser")

k=num-1

title2 = soup.select("a.bo3 > b")

  
print(f'1월 종합 {num}위는 {title2[k].string}입니다.')
f.write(f'1월 종합 {num}위는 {title2[k].string}입니다. \n')
f.close()
