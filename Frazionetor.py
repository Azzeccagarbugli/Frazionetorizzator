import telepot
import time
from fractions import gcd

machine_state = -1


class Frazione:
    numeratore = 1
    denominatore = 1

    def __init__(self, numeratore, denominatore):
        self.numeratore = int(numeratore)
        self.denominatore = int(denominatore)

    # Funzione usata per semplificare le frazioni inserite dall'utente
    def Semplifica(self):
        gcd_val = gcd(self.numeratore, self.denominatore)

        self.numeratore = self.numeratore / gcd_val
        self.denominatore = self.denominatore / gcd_val

        frazione_sw = ("La frazione semplificata è: *{0}*/*{1}*".format(self.numeratore, self.denominatore))
        return frazione_sw


# Funzione che viene eseguita all'arrivo di ogni nuovo messaggio
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    global machine_state
    global numeratore
    global denominatore

    chat_id = msg['chat']['id']
    command_input = msg['text']

    print(content_type, chat_type, chat_id)

    if machine_state == -1 and content_type == 'text':

        if command_input == '/start' or command_input == '/start@FrazionetorBot':

            start_text = '''Benvenuto nel futuro! Inzia a digitare un comando per cominciare un'esperienza metafisica'''
            bot.sendMessage(chat_id, start_text)

            machine_state = 0

    elif machine_state == 0 and content_type == 'text':

        if command_input == '/help' or command_input == '/help@FrazionetorBot':

            help_text = "Salve, puoi utilizzare il comando /frazionifica per iniziare a semplificare"
            help_text += "le frazioni mentre puoi usare il comando /cronologia per controllare la cronologia"
            help_text += "dei tuoi calcoli.\nPuoi contattare lo sviluppatore su github.com/Azzeccagarbugli"
            bot.sendMessage(chat_id, help_text)

            machine_state = 1


    elif machine_state == 1 and content_type == 'text':

        if command_input == '/frazionifica' or command_input == '/frazionifica@FrazionetorBot':

            numerator_text = 'Inserisci il numeratore della frazione che vuoi semplificare'
            bot.sendMessage(chat_id, numerator_text)

            machine_state = 2

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''
            bot.sendMessage(chat_id, problem_text)

            machine_state = 0

    elif machine_state == 2 and content_type == 'text':

        if command_input.isdigit() == True:

            numeratore = int(float(command_input))

            denominatore_text = "Inserisci il denominatore della frazione che vuoi semplificare"
            bot.sendMessage(chat_id, denominatore_text)

            machine_state = 6

        elif command_input.isdigit() == False:

            numeratore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un"
            numeratore_problem_text += "numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"
            bot.sendMessage(chat_id, numeratore_problem_text)

            machine_state = 5

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''
            bot.sendMessage(chat_id, problem_text)

            machine_state = 0

    elif machine_state == 6 and content_type == 'text':

        if command_input.isdigit() == True:

            denominatore = int(float(command_input))

            Fraz = Frazione(numeratore, denominatore)
            msg = Fraz.Semplifica()
            print(Fraz, msg, numeratore, denominatore)
            bot.sendMessage(chat_id, ("%s" % msg), parse_mode = "Markdown")

            machine_state = 1

        elif command_input.isdigit() == False:

            numeratore_problem_text = "Quello che hai inserito non è un valore numerico! Inserisci un"
            numeratore_problem_text += "numero o altrimenti premi la lettera 'q' per uscire dal comando /frazionifica"
            bot.sendMessage(chat_id, numeratore_problem_text)

            machine_state = 8

        else:

            problem_text = '''Cosa cavolo sono queste cose?! Mi stai prendendo per un deficente forse?'''
            bot.sendMessage(chat_id, problem_text)

            machine_state = 0

bot = telepot.Bot('TOKEN')
bot.message_loop(handle)

print('Vediamo quello che succede ...')

while 1:
    time.sleep(10)
