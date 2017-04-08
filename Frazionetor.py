from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import telepot
import sys
import time
import wolframalpha
import re

machine_state = 0
client = wolframalpha.Client("API")

# Funzione usata per semplificare le frazioni inserite dall'utente
def Semplifica(numeratore, denominatore):
    i = 0

    if numeratore > denominatore:
        i = denominatore
    else:
        i = numeratore

    while i > 0:
        if numeratore % i == 0 and denominatore % i == 0:
            numeratore = numeratore / i
            denominatore = denominatore / i
            if (numeratore != numeratore / i) and (denominatore != denominatore / i):
                semplificazione = ("La frazione semplificata è: *{0}*/*{1}*".format(numeratore, denominatore))
                return semplificazione
                break
            else:
                n_semplificazione = ("La frazione non può essere ridotta ai minimi termini: *{0}*/*{1}*".format(numeratore, denominatore))
                return n_semplificazione
                break
        i = i - 1

# Funzione che viene eseguita all'arrivo di ogni nuovo messaggio
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    global machine_state
    global numeratore
    global denominatore

    fatt = 'Fattorizzazione'
    appr_dec = 'Approsimazione decimale'
    egiz = 'Frazione egizia'
    graf = 'Grafico a torta'

    chat_id = msg['chat']['id']
    command_input = msg['text']

    print(content_type, chat_type, chat_id)

    if machine_state == 0 and content_type == 'text':

        if command_input == '/start' or command_input == '/start@FrazionetorBot':

            start_text = '''Benvenuto nel futuro! Inzia a digitare un comando per cominciare un'esperienza metafisica'''

            bot.sendMessage(chat_id, start_text)

            machine_state = 1

    elif machine_state == 1 and content_type == 'text':

        if command_input == '/help' or command_input == '/help@FrazionetorBot':

            help_text = "Salve, puoi utilizzare il comando /frazionifica per iniziare a semplificare"
            help_text += "le frazioni mentre puoi usare il comando /frazionificastronger per ricevere informazioni molto "
            help_text += "più dettagliate sull'ultima frazione semplificata.\nPuoi contattare lo sviluppatore su github.com/Azzeccagarbugli"

            bot.sendMessage(chat_id, help_text)

            machine_state = 1

        elif command_input == '/frazionifica' or command_input == '/frazionifica@FrazionetorBot':

            numerator_text = 'Inserisci il numeratore della frazione che vuoi semplificare'

            bot.sendMessage(chat_id, numerator_text)

            machine_state = 2

        elif command_input == '/frazionificastronger' or command_input == '/frazionificastronger@FrazionetorBot':

            markup = ReplyKeyboardMarkup(keyboard=[
                         [fatt],
                         [appr_dec],
                         [egiz],
                         [graf]
                     ])

            frazionifica_stronger_text = "Seleziona una voce per ottenere maggiori informazioni sull'ultima frazione semplificata"

            bot.sendMessage(chat_id, frazionifica_stronger_text, reply_markup=markup)

            machine_state = 6

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''
            bot.sendMessage(chat_id, problem_text)

            machine_state = 1

    elif machine_state == 2 and content_type == 'text':

        if command_input.isdigit() == True:

            numeratore = int(command_input)
            denominatore_text = "Inserisci il denominatore della frazione che vuoi semplificare"

            bot.sendMessage(chat_id, denominatore_text)

            machine_state = 3

        elif command_input.isdigit() == False:

            numeratore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un "
            numeratore_problem_text += " numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"

            bot.sendMessage(chat_id, numeratore_problem_text)

            machine_state = 4

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''

            bot.sendMessage(chat_id, problem_text)

            machine_state = 1

    elif machine_state == 3 and content_type == 'text':

        if command_input.isdigit() == True:

            denominatore = int(command_input)
            semplificazione = Semplifica(numeratore, denominatore)

            url_frazione = 'http://www.wolframalpha.com/input/?i={0}%2F{1}'.format(numeratore, denominatore)

            keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                   InlineKeyboardButton(text='Maggiori dettagli', url=url_frazione)
               ]])

            bot.sendMessage(chat_id, ("%s" % semplificazione), parse_mode = "Markdown", reply_markup = keyboard)

            machine_state = 1

        elif command_input.isdigit() == False:

            denominatore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un"
            denominatore_problem_text += " numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"

            bot.sendMessage(chat_id, denominatore_problem_text)

            machine_state = 5

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''

            bot.sendMessage(chat_id, problem_text)

            machine_state = 1

    elif machine_state == 4 and content_type == 'text':

        if command_input.isdigit() == True:

            numeratore = int(command_input)
            denominatore_text = "Inserisci il denominatore della frazione che vuoi semplificare"

            bot.sendMessage(chat_id, denominatore_text)

            machine_state = 3

        elif command_input.isdigit() == False and command_input == 'q' and content_type == 'text':

            bot.sendMessage(chat_id, "Sei uscito dal comando /frazionifica, seleziona un altro comando per proseguire")

            machine_state = 1

        elif command_input.isdigit() == False and content_type == 'text':

            numeratore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un"
            numeratore_problem_text += " numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"

            bot.sendMessage(chat_id, numeratore_problem_text)

            machine_state = 4

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''

            bot.sendMessage(chat_id, problem_text)

            machine_state = 1

    elif machine_state == 5 and content_type == 'text':

        if command_input.isdigit() == True:

            denominatore = int(command_input)
            semplificazione = Semplifica(numeratore, denominatore)

            bot.sendMessage(chat_id, ("%s" % semplificazione), parse_mode = "Markdown")

            machine_state = 1

        elif command_input.isdigit() == False and command_input == 'q' and content_type == 'text':

            bot.sendMessage(chat_id, "Sei uscito dal comando /frazionifica, seleziona un altro comando per proseguire")

            machine_state = 1

        elif command_input.isdigit() == False and content_type == 'text':

            denominatore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un"
            denominatore_problem_text += " numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"

            bot.sendMessage(chat_id, denominatore_problem_text)

            machine_state = 5

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''

            bot.sendMessage(chat_id, problem_text)

            machine_state = 1

    elif machine_state == 6:

        res = client.query(str(numeratore) + '/' + str(denominatore))

        if command_input == fatt and content_type == 'text':

            pattern_fatt = '\'@title\': \'Prime factorization\'(.+)'
            pattern_fatt_final = '\'plaintext\': \'(.+)\''

            found_fatt = ''
            found_fatt_final = ''

            for pod in res.pods:
                try:
                    found_fatt = re.findall(pattern_fatt, str(pod))
                    found_fatt_final = re.findall(pattern_fatt_final, str(found_fatt))
                    if len(found_fatt_final):
                        found_fatt_final = found_fatt_final[0]
                        break
                    else:
                        found_fatt_final = 'Modalità non disponibile in questo caso'
                except IndexError:
                    found_fatt_final = ''

            bot.sendMessage(chat_id, found_fatt_final)

            machine_state = 1

        elif command_input == appr_dec and content_type == 'text':

            pattern_appr = '\'@title\': \'Decimal approximation\'(.+)'
            pattern_appr_final = '\'plaintext\': \'(.+?)\''

            found_appr = ''
            found_appr_final = ''

            for pod in res.pods:
                try:
                    found_appr = re.findall(pattern_appr, str(pod))
                    found_appr_final = re.findall(pattern_appr_final, str(found_appr))
                    if len(found_appr_final):
                        found_appr_final = found_appr_final[0]
                        break
                    else:
                        found_appr_final = 'Modalità non disponibile in questo caso'
                except IndexError:
                    found_appr_final = ''

            bot.sendMessage(chat_id, found_appr_final)

            machine_state = 1

        elif command_input == egiz and content_type == 'text':

            pattern_egiz = '\'@title\': \'Egyptian fraction expansion\'(.+)'
            pattern_egiz_final = '\'plaintext\': \'(.+?)\''

            found_egiz = ''
            found_egiz_final = ''

            for pod in res.pods:
                try:
                    found_egiz = re.findall(pattern_egiz, str(pod))
                    found_egiz_final = re.findall(pattern_egiz_final, str(found_egiz))
                    if len(found_egiz_final):
                        found_egiz_final = found_egiz_final[0]
                        break
                    else:
                        found_egiz_final = 'Modalità non disponibile in questo caso'
                except IndexError:
                    found_egiz_final = ''

            bot.sendMessage(chat_id, found_egiz_final)

            machine_state = 1

bot = telepot.Bot('TOKEN')
bot.message_loop(handle)

print('Vediamo quello che succede ...')

while 1:
    time.sleep(10)
