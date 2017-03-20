import telepot
import sys
import time
import datetime

machine_state = 0

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

    chat_id = msg['chat']['id']
    command_input = msg['text']

    history_frazionifica = []

    print(content_type, chat_type, chat_id)

    if machine_state == 0 and content_type == 'text':

        if command_input == '/start' or command_input == '/start@FrazionetorBot':

            start_text = '''Benvenuto nel futuro! Inzia a digitare un comando per cominciare un'esperienza metafisica'''
            bot.sendMessage(chat_id, start_text)

            machine_state = 1

    elif machine_state == 1 and content_type == 'text':

        if command_input == '/help' or command_input == '/help@FrazionetorBot':

            help_text = "Salve, puoi utilizzare il comando /frazionifica per iniziare a semplificare"
            help_text += "le frazioni mentre puoi usare il comando /cronologia per controllare la cronologia"
            help_text += "dei tuoi calcoli.\nPuoi contattare lo sviluppatore su github.com/Azzeccagarbugli"
            bot.sendMessage(chat_id, help_text)

            machine_state = 1

        elif command_input == '/frazionifica' or command_input == '/start@FrazionetorBot':

            numerator_text = 'Inserisci il numeratore della frazione che vuoi semplificare'
            bot.sendMessage(chat_id, numerator_text)

            machine_state = 2

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
            bot.sendMessage(chat_id, ("%s" % semplificazione), parse_mode = "Markdown")

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
            print(numeratore)
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
            print(denominatore)
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


bot = telepot.Bot('TOKEN')
bot.message_loop(handle)

print('Vediamo quello che succede ...')

while 1:
    time.sleep(10)
