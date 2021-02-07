# "Telegram Auto Forwarder" From "MaCo"
#
# Website:   http://man-va-code.ir
# GitHub:    https://github.com/man-va-code
# Instagram: https://instagram.com/man_va_code
# Eitaa:     https://eitaa.com/man_va_code
# Twitter:   https://twitter.com/man_va_code
# Soroush:   https://what.sapp.ir/man_va_code
# Rubika:    https://rubika.ir/man_va_code
# Youtube:   https://youtube.com/channel/UCZahV_BJmf83ybUd6krfClA
# Virgool:   https://virgool.io/@man_va_code
# Facebook:  https://facebook.com/man.va.code
# Aparat:    https://aparat.com/man_va_code
# Telegram:  https://t.me/man_va_code
#
# this app uses a fork of " https://github.com/tdlib/td " version " v1.7.0 " and i just change some part of it
# for forward and view new messages that this telegram client recive from server.
#
# special thanks from:
# Aliaksei Levin (levlam@telegram.org), Arseny Smirnov (arseny30@gmail.com),
# Pellegrino Prevete (pellegrinoprevete@gmail.com)
#
from ctypes.util import find_library
from ctypes import CDLL, c_int, c_char_p, c_double, CFUNCTYPE
import json
import sys
import time
import os.path
import platform

# load shared library

app_path = os.path.dirname(os.path.abspath(__file__))

operating_system = platform.system()

tdjson_path = None

if ((operating_system == "Linux") and (os.path.isfile(app_path + "/dependencies/linux/tdjson.so"))):
    tdjson_path = app_path+"/dependencies/linux/tdjson.so"
    
if ((operating_system == "Windows") and (os.path.isfile(app_path + "\\dependencies\\windows\\tdjson.dll"))):
    tdjson_path = app_path+"\\dependencies\\windows\\tdjson.dll"

# check existing dependencies
if tdjson_path is None:
    print('can\'t find tdjson library')
    quit()
tdjson = CDLL(tdjson_path)

# load TDLib functions from shared library
_td_create_client_id = tdjson.td_create_client_id
_td_create_client_id.restype = c_int
_td_create_client_id.argtypes = []

_td_receive = tdjson.td_receive
_td_receive.restype = c_char_p
_td_receive.argtypes = [c_double]

_td_send = tdjson.td_send
_td_send.restype = None
_td_send.argtypes = [c_int, c_char_p]

_td_execute = tdjson.td_execute
_td_execute.restype = c_char_p
_td_execute.argtypes = [c_char_p]

fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

_td_set_log_fatal_error_callback = tdjson.td_set_log_fatal_error_callback
_td_set_log_fatal_error_callback.restype = None
_td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]

# initialize TDLib log with desired parameters
def on_fatal_error_callback(error_message):
    None
    print('TDLib fatal error: ', error_message)
    sys.stdout.flush()

def td_execute(query):
    query = json.dumps(query).encode('utf-8')
    result = _td_execute(query)
    if result:
        result = json.loads(result.decode('utf-8'))
    return result

c_on_fatal_error_callback = fatal_error_callback_type(on_fatal_error_callback)
_td_set_log_fatal_error_callback(c_on_fatal_error_callback)

# setting TDLib log verbosity level to 1 (errors)
#print(str(
td_execute({'@type': 'setLogVerbosityLevel', 'new_verbosity_level': 1, '@extra': 1.01234})#).encode('utf-8'))

# create client
client_id = _td_create_client_id()

# simple wrappers for client usage
def td_send(query):
    query = json.dumps(query).encode('utf-8')
    _td_send(client_id, query)

def td_receive():
    result = _td_receive(1.0)
    if result:
        result = json.loads(result.decode('utf-8'))
    return result

# another test for TDLib execute method
#print(str(
td_execute({'@type': 'getTextEntities', 'text': '@telegram /test_command https://telegram.org telegram.me', '@extra': ['5', 7.0, 'ä']})#).encode('utf-8'))

# start the client by sending request to it
td_send({'@type': 'getAuthorizationState', '@extra': 1.01234})

#################################################

# main variables

base_message_id = 0
message_id = 0
rotate_step = 1
idle_counter = 0
file_name = "config.txt"

#################################################

# function for working with files and read/write configs

def config_read_write(file_name, config_name):
    if(not(os.path.isfile(file_name))):
        file = open(file_name,"w")
        file.close()

    if(os.path.isfile(file_name)):

        file = open(file_name,"r")
        file_read = file.readlines()
        file.close()

        file_lines = len(file_read)

        if (file_lines == 0):
            firstline = (config_name + '=')
            file_read = [firstline]
            file_lines = 1

        line_counter = 1
        line_contant = [None]

        for loop_line in range(file_lines):
            if ( '=' in file_read[loop_line]):
                line_contant = file_read[loop_line].split("=", 1)
                if (line_contant[0] == config_name):
                    if( (line_contant[1] == '\n' ) or (line_contant[1] == '' ) or (line_contant[1] == None ) ):
                        input_value = (input("Please enter your "+config_name+": "))
                        input_value = input_value.split(" ", 1)
                        input_value = input_value[0].strip()
                        if ( (loop_line == 0) ):
                            file_read[loop_line] = (config_name + '=' + (input_value + '\n') ) 
                        if( (loop_line > 0) and ('\n' in file_read[loop_line - 1] ) ):
                                file_read[loop_line] = ( config_name + '=' + (input_value + '\n') ) 
                        if( (loop_line > 0) and ('\n' not in file_read[loop_line - 1] ) ):
                            file_read[loop_line] = ( '\n' + config_name + '=' + (input_value + '\n') )
                        file = open(file_name,"w")
                        file.writelines(file_read)
                        file.close()
                        print ("Your " + config_name + " Set To: " + input_value + '\n')
                        return (input_value.strip())
                    else:
                        line_contant = line_contant[1].split(" ", 1)
                        return (line_contant[0].strip())

            if ( ( (line_contant[0] != config_name) ) and (line_counter == file_lines)):
                input_value = (input("Please enter your "+config_name+": "))
                input_value = input_value.split(" ", 1)
                input_value = input_value[0].strip()
                if( '\n' in file_read[loop_line] ):
                    file_read.insert( line_counter, (config_name + "=" + (input_value +'\n'))) 
                if( '\n' not in file_read[loop_line] ):
                    file_read.insert( line_counter, ( '\n' + config_name + "=" + (input_value +'\n'))) 
                file = open(file_name,"w")
                file.writelines(file_read)
                file.close()
                print ("Your " + config_name + " Set To: " + input_value + '\n')
                return (input_value.strip())

            line_counter += 1

#################################################

# draw rotating line function

def draw_rotating_line(rotate_step):

    if(rotate_step == 4):
        sys.stdout.write('\\')
        sys.stdout.write('\b')
        sys.stdout.flush()
        rotate_step = 1

    if(rotate_step == 3):
        sys.stdout.write('-')
        sys.stdout.write('\b')
        sys.stdout.flush()
        rotate_step = 4

    if(rotate_step == 2):
        sys.stdout.write('/')
        sys.stdout.write('\b')
        sys.stdout.flush()
        rotate_step = 3

    if (rotate_step == 1):
        sys.stdout.write('|')
        sys.stdout.write('\b')
        sys.stdout.flush()
        rotate_step = 2

    return (rotate_step)

#################################################

# not event counter function

def not_event(idle_counter):
    idle_counter += 1
    if (idle_counter <= 9):
        sys.stdout.write('# ')
        sys.stdout.write(str(idle_counter))
        sys.stdout.write('\b\b\b')
        #sys.stdout.flush()

    if (idle_counter > 9 and idle_counter <= 99):
        sys.stdout.write('# ')
        sys.stdout.write(str(idle_counter))
        sys.stdout.write('\b\b\b\b')
        #sys.stdout.flush()

    if(idle_counter == 100):
        sys.stdout.write('# 100')
        sys.stdout.write('\nDone.')
        sys.stdout.flush()
        sys.exit()

    sys.stdout.flush()
    return (idle_counter)

#################################################

# save and read configs in "config.txt" file

my_api_id = config_read_write(file_name , "api_id")
my_api_hash = config_read_write(file_name , "api_hash")
my_chat_id = config_read_write(file_name , "chat_id")
#################################################

# select run mode of app

try:
    run_mode = None
    run_mode = input("Please select run mode:\n'1' -> Sync\n'5' -> Sync & View\n'9' -> Sync & View & Forward : ")
    sys.stdout.write('Working ')
except (KeyboardInterrupt):
    print ("\nExit")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

#################################################

# main events cycle

try:
    while True:

        # recive events
        event = td_receive()

        # call draw_rotating_line function when app is working
        rotate_step = draw_rotating_line(rotate_step)

        #call not_event when app is idle and then, exit after some time
        if (not event):
            idle_counter = not_event(idle_counter)


        # timer for normalising app working speed and decrease process pressure on system
        time.sleep(0.3)

        # if app recive an event
        if event:
            # process authorization states
            if event['@type'] == 'updateAuthorizationState':
                auth_state = event['authorization_state']

                # if client is closed, we need to destroy it and create new client
                if auth_state['@type'] == 'authorizationStateClosed':
                    break

                # set TDLib parameters
                # you MUST obtain your own api_id and api_hash at https://my.telegram.org
                # and use them in the setTdlibParameters call
                if auth_state['@type'] == 'authorizationStateWaitTdlibParameters':
                    td_send({'@type': 'setTdlibParameters', 'parameters': {
                                                        'database_directory': 'tdlib',
                                                        'use_message_database': True,
                                                        'use_secret_chats': True,
                                                        'api_id': my_api_id,
                                                        'api_hash': my_api_hash,
                                                        'system_language_code': 'en',
                                                        'device_model': 'Desktop',
                                                        'application_version': '1.0',
                                                        'enable_storage_optimizer': True}})

                # set an encryption key for database to let know TDLib how to open the database
                if auth_state['@type'] == 'authorizationStateWaitEncryptionKey':
                    td_send({'@type': 'checkDatabaseEncryptionKey', 'encryption_key': ''})

                # enter phone number to log in
                if auth_state['@type'] == 'authorizationStateWaitPhoneNumber':
                    phone_number = input('\nPlease enter your phone number: ')
                    td_send({'@type': 'setAuthenticationPhoneNumber', 'phone_number': phone_number})

                # wait for authorization code
                if auth_state['@type'] == 'authorizationStateWaitCode':
                    code = input('Please enter the authentication code you received: ')
                    td_send({'@type': 'checkAuthenticationCode', 'code': code})

                # wait for first and last name for new users
                if auth_state['@type'] == 'authorizationStateWaitRegistration':
                    first_name = input('Please enter your first name: ')
                    last_name = input('Please enter your last name: ')
                    td_send({'@type': 'registerUser', 'first_name': first_name, 'last_name': last_name})

                # wait for password if present
                if auth_state['@type'] == 'authorizationStateWaitPassword':
                    password = input('Please enter your password: ')
                    td_send({'@type': 'checkAuthenticationPassword', 'password': password})

            # sync
            if ((run_mode != '5') or (run_mode != '9')):
                None

            # sync & view
            if (run_mode == '5'):
                if (event['@type']=='updateNewMessage'):
                    chat_id = str(event['message']['chat_id'])
                    message_id = event['message']['id']

                if (message_id != base_message_id and chat_id != my_chat_id):
                    base_message_id = message_id
                    td_send({'@type': 'viewMessages', 'chat_id': chat_id, 'message_thread_id': 0, 'message_ids': [message_id], 'force_read': 1 })

            # sync & view & forward
            if (run_mode == '9'):
                if (event['@type']=='updateNewMessage'):
                    chat_id = str(event['message']['chat_id'])
                    message_id = event['message']['id']

                if (message_id != base_message_id and chat_id != my_chat_id):
                    base_message_id = message_id
                    td_send({'@type': 'forwardMessages', 'chat_id': my_chat_id, 'from_chat_id': chat_id, 'message_ids': [message_id] })
                    td_send({'@type': 'viewMessages', 'chat_id': chat_id, 'message_thread_id': 0, 'message_ids': [message_id], 'force_read': 1 })

except (KeyboardInterrupt):
    print ("\nExit")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
