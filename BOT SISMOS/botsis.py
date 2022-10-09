from cgitb import html
from email import message
from lib2to3.pytree import convert
from bs4 import BeautifulSoup
import requests
import schedule

#BY:JUANHG (T4RS)

def sis_scraping1():
    url = requests.get('http://www.ssn.unam.mx/')
    soup = BeautifulSoup(url.content, 'html.parser')
    resultado1 = soup.find(id='recent_event_row_strong_1')
    
    format_result1 = resultado1.text


    return format_result1

def sis_scraping2():
     url = requests.get('http://www.ssn.unam.mx/')
     soup = BeautifulSoup(url.content, 'html.parser')
     resultado2 = soup.find(id='recent_event_row_strong_2')

     format_result2 = resultado2.text


     return format_result2
 
def sis_scraping3():
     url = requests.get('http://www.ssn.unam.mx/')
     soup = BeautifulSoup(url.content, 'html.parser')
     resultado3 = soup.find(id='recent_event_row_strong_3')

     format_result3 = resultado3.text


     return format_result3


def sis_scraping4():
     url = requests.get('http://www.ssn.unam.mx/')
     soup = BeautifulSoup(url.content, 'html.parser')
     resultado4 = soup.find(id='recent_event_row_strong_4')

     format_result4 = resultado4.text


     return format_result4


def sis_scraping5():
     url = requests.get('http://www.ssn.unam.mx/')
     soup = BeautifulSoup(url.content, 'html.parser')    
     resultado5 = soup.find(id='recent_event_row_strong_5')

     format_result5 = resultado5.text


     return format_result5
    



def bot_send_text(bot_menssage):
    bot_token = '5669472290:AAGqYfXYEzuDxM8NYdxpQMKZIEB3XObBIIY'
    bot_chatID = '5686626420'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_menssage
    
    response = requests.get(send_text)

    return response


def reportes():

   bot_send_text('Estos son los ultimos sismos registrados: ') 

   bot_send_text(sis_scraping1())
   print('Envio 1...')
    
   bot_send_text(sis_scraping2())
   print('Envio 2...')

   bot_send_text(sis_scraping3())
   print('Envio 3...')

   bot_send_text(sis_scraping4())
   print('Envio 4...')

   bot_send_text(sis_scraping5())
   print('Envio 5...')

   bot_send_text('')


if __name__ == '__main__':
    schedule.every(10).seconds.do(reportes)

    while True:
        schedule.run_pending()


