from pprint import pprint
import telepot
import telepot.namedtuple
import string
import time
import sys
import re
from fractions import Fraction

# Funzione che viene eseguita all'arrivo di ogni nuovo messaggio
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #m = telepot.namedtuple.Message(**msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])
        text_input = msg['text'].lower()
        number_presence = text_input.isdigit()
        print (number_presence)
    
        if number_presence == False:
            answer_false_output = 'Sei un fasullo! Inserisci valori numerici'
            print (number_presence)
            bot.sendMessage(chat_id, answer_false_output)
        
        elif number_presence == True:
            answer_true_output = 'Sei un mito!'
            print (number_presence)
	    
            text_input = fraction
            tmp = re.findall('\\b\\d+\\b', fraction)
            tmp_fraction = [int(i) for i in tmp]
            
            numeratore = temp_fraction[0]
            denominatore = temp_fraction[1]
            
            frazione = Fraction(numeratore, denominatore)
            print (frazione)
            
            bot.sendMessage(chat_id, answer_true_output)
       
        else:
            answer_unknow_output = 'Inserisci dei caratteri validi deficente'
            #bot.sendMessage(chat_id, answer_unknow_output)

bot = telepot.Bot('TOKEN')
bot.message_loop(handle)
response = bot.getUpdates() #Ricevo info su utenti che usano il bot
pprint(response)

while 1:
    time.sleep(10)

