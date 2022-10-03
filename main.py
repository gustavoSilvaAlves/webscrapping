from bs4 import BeautifulSoup
import requests
import smtplib
import email.message

URL = "https://www.lenovo.com/br/pt/laptops/ideapad/serie-300/IdeaPad-3-15ITL6/p/82MD000FBR"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('div', class_='headerContainer').get_text().strip()

valor = soup.find('div', class_='cta-group-price').get_text().strip()

num_valor = valor[16:21]
num_valor = num_valor.replace('.','')
num_valor = float(num_valor)


def send_email():
    email_content = """
    https://www.lenovo.com/br/pt/laptops/ideapad/serie-300/IdeaPad-3-15ITL6/p/82MD000FBR   
    """
    msg = email.message.Message()
    msg['Subject'] = 'Lenovo IdeaPad3i baixou!!!'

    msg['From'] = 'usuario887733666@gmail.com'
    msg['To'] = 'usuario887733666@gmail.com'
    password = 'user96790'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['from'], [msg['To']], msg.as_string())

    print("Sucesso ao enviar email")


if(num_valor<=2800):
    print("O preço baixou!!!")
else:
    print("O preço ta caro")


