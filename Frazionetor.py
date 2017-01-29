import telepot
import telepot.namedtuple
import string
import time
import sys
from fractions import Fraction
from pprint import pprint

# Funzione che viene eseguita all'arrivo di ogni nuovo messaggio
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #m = telepot.namedtuple.Message(**msg)

    chat_id = msg['chat']['id']
    command_input = msg['text']

    print(content_type, chat_type, chat_id)

    if command_input == '/help':

        help_text = '''Salve, puoi utilizzare il comando /frazionifica\
                    per iniziare a semplificare le frazioni mentre puoi\
                    usare il comando /cronologia per controllare la\
                    cronologia dei tuoi calcoli.\

                    Puoi contattare lo sviluppatore su github.com/Azzeccagarbugli'''

        bot.sendMessage(chat_id, help_text)

    elif command_input == '/frazionifica':
        input_numeratore_str = 'Inserisci il numeratore della frazione'
        ####
        text_input_numeratore = msg['text'].lower()
        number_presence_numeratore = text_input_numeratore.isdigit()
        bot.sendMessage(chat_id, input_numeratore_str)

        while number_presence_numeratore == False:
            print(text_input_numeratore)

            text_messaggeNUM_error = '''Stupido, devi inserire il numeratore non altre cose!\
                                        Prova a usare quel piccolo cervello che ti ritrovi e inserisci un numeratore valido'''

            bot.sendMessage(chat_id, text_messaggeNUM_error)

            new_tentativo_numeratore = msg['text'].islower()
            number_presence_numeratore_T2 = new_tentativo_numeratore.isdigit()

            if number_presence_numeratore_T2 == False:
                insulto_str = "Sei proprio un deficente."
                bot.sendMessage(chat_id, insulto_str)

        else:
            numeratore_CONCRETO = text_input_numeratore
            numeratore_CONCRETO_str = "Il numeratore che hai inserito è: %s" % (numeratore_CONCRETO)
            bot.sendMessage(chat_id, numeratore_CONCRETO_str)


    elif command_input == '/cronologia':
        insulto_str1 = "Sei proprio un deficente."
        bot.sendMessage(chat_id, insulto_str1)

    else:
        insulto_str2 = "Sei proprio un deficente."
        bot.sendMessage(chat_id, insulto_str2)


bot = telepot.Bot('307702349:AAExqlFD-IwaV9F1ZJXRAbGpuAIABO7wWgg')
bot.message_loop(handle)
response = bot.getUpdates() #Ricevo info su utenti che usano il bot
pprint(response)

while 1:
    time.sleep(10)


