from datetime import datetime
from textwrap import wrap
import time
import subprocess

from pykeyboard import PyKeyboard

k = PyKeyboard()
cmds = [
    'up',
    'down',
    'left',
    'right',
    'a',
    'b',
    'start',
    'select',
    'save',
    'reload',
]

cmdkeys = [
    k.up_key,
    k.down_key,
    k.left_key,
    k.right_key,
    'a',
    'b',
    k.return_key,
    k.shift_key,
    k.function_keys[5],
    k.function_keys[7],
]

# clear the screen
print('\n' * 100)

# poverty logger
def tp_logger(nick, text):
    stamp = datetime.now().strftime('[%m.%d.%y %H:%M:%S] ')
    print('<' + nick + '> ', text)
    with open('log_tildeplays.log', 'a') as f:
        f.write(stamp + '<' + nick + '> ' + text + '\n')
    line = '<' + nick + '>  ' + text
    output = wrap(line, width=25)
    with open('log.txt', 'a') as chat:
        for i in output:
            chat.write(i + '\n')


def presskey(key):
    k.press_key(key)
    time.sleep(0.15)
    k.release_key(key)


def run(nick, text):
    subprocess.call('xdotool search --name "FCEUX 2.2.2" windowactivate', shell=True)
    if text.startswith('tildeplaysbot:'):
        text = ''.join([i + ' ' for i in text.split(' ')[1:]]).strip()
        tp_logger(nick, text)
    if text.startswith('!ff'):
        tp_logger(nick, text)
    if text in cmds:
        tp_logger(nick, text)
        presskey(cmdkeys[cmds.index(text)])
    else:
        pass
