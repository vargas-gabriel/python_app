import requests 
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Dr-Martens-Unisex-8-Tie-Medium/dp/B079RKCWGF/ref=sr_1_1_sspa?crid=3QCAUYK3O5TC0&dchild=1&keywords=doc+martens+mens+boots&qid=1603847268&sprefix=doc+mar%2Caps%2C180&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVVBUQlQ5Q0oxRlhLJmVuY3J5cHRlZElkPUEwMTEyOTgyMkJDRTg3RVNROTgxWSZlbmNyeXB0ZWRBZElkPUEwMTM2NDcxMVdXNE1YM0k5VThRTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float (price[0:5])

    if(converted_price < 55.00):
        send_mail()
    print(converted_price)
    print(title.strip())

    if (converted_price < 45.00):
        send_mail():
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.ehlo()
    server.login('intrapols@gmail.com')

    subject = 'Price went down'
    body = 'https://www.amazon.com/Dr-Martens-Unisex-8-Tie-Medium/dp/B079RKCWGF/ref=sr_1_1_sspa?crid=3QCAUYK3O5TC0&dchild=1&keywords=doc+martens+mens+boots&qid=1603847268&sprefix=doc+mar%2Caps%2C180&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVVBUQlQ5Q0oxRlhLJmVuY3J5cHRlZElkPUEwMTEyOTgyMkJDRTg3RVNROTgxWSZlbmNyeXB0ZWRBZElkPUEwMTM2NDcxMVdXNE1YM0k5VThRTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    msg = f"Subject {subject}\n\n{body}"

    server.sendmail(
        'intrapols@gmail.com'
        msg 
    )
    print('email has been sent')

    server.quit()

    check_price():
