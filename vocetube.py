#coding: utf-8

from pytube import YouTube


def click(x):
    r = str(x)
    link = x
    YouTube(link).streams.first().download()
    print("Video Baixado")
def clickp(x):
	pl=Playlist(x)
	pl.download_all()
	print("Playlist Baixada")


print('{:=^45}'.format('py_societ'))
print("\033[32mVoce\033[0;0m\033[31mtube\033[0;0m")
print('{:=^45}'.format('dev《kailp * feb,18'))

print('\033[40;1;39m Escolha uma opção:\033[0;0m')
print('\033[46;1;33m1.Video\n\033[0;0m\033[46;1;33m2.Playlist\033[0;0m')
x = input('.....: ')
res = input('\033[0;0m\nCole o link do Video: ')
if(x=='1'):
	click(res)
if(x=='2'):
	clickp(res)
else:
	print('escolha invalida')

    
    