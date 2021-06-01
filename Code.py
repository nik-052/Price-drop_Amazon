import requests
URL="https://www.amazon.in/Test-Exclusive-712/dp/B07DJCJBB3/ref=sr_1_5?crid=32QQRXPGWCCYF&dchild=1&keywords=samsung+mobile&qid=1601649146&sprefix=samsu%2Caps%2C396&sr=8-5"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
from bs4 import BeautifulSoup
import smtplib   #importing all the libraries required.   Finding the agent


def check_price():
    page=requests.get(URL, headers=headers )
    soup=BeautifulSoup(page.content,'html.parser')
    #soup.prettify()
    title=soup.find(id='productTitle').get_text()
    price=soup.find(id='priceblock_dealprice').get_text()
    pr_cnv=float(price[:-3])
    
    if pr_cnv>19.000:
        mail()

    print(title.strip())
    print(pr_cnv)                        #Checking the price drop function
    
    
def mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('id','pass')   #put your id and password
    subject="Price fell Down!"
    body="Check Amazon Website  : https://www.amazon.in/Test-Exclusive-712/dp/B07DJCJBB3/ref=sr_1_5?crid=32QQRXPGWCCYF&dchild=1&keywords=samsung+mobile&qid=1601649146&sprefix=samsu%2Caps%2C396&sr=8-5 "
    msg=f"Subject:{subject} \n\n{body}"                   # this is a particular item in amazon
    
    server.sendmail('sender','rcv',msg) # put sender id and reciever emai-id
    print("EMAIL SENT")
    server.quit()               # sends an email
    
check_price()           # calling the main function
    
    
    
