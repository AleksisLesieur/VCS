import os

import shutil

print('current directory', os.getcwd())

os.chdir('../..\Desktop')

print('current directory', os.getcwd())

os.mkdir('naujas_folderis')

os.chdir('naujas_folderis')

os.makedirs('kitas_naujas_folderis')

os.chdir('kitas_naujas_folderis')

print('current directory', os.getcwd())

with open('text.txt', 'w') as file:
    file.write('Aciu uz desimtuka is testo')

with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

shutil.copy('text.txt', 'copy_text.txt')

os.rename('text.txt', 'better_name.txt')

print('current directory', os.getcwd())

if os.path.exists('better_name.txt') and os.path.exists('copy_text.txt'):
    os.remove('copy_text.txt')

os.chdir('../../')

print('current directory', os.getcwd())

shutil.rmtree('naujas_folderis')
