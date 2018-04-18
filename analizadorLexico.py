import ply.lex as lex
import re
import codecs
import os
import sys


palabrasReservadas=['INICIAR','FINALIZAR','SI','ENTONCES','MIENTRAS','HACER','LLAMAR','CONST',
                    'VAR','PROCESO','SALIDA','ENTRADA','SINO']

tokens=palabrasReservadas+['ID','NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION','ODD','ASIGNACION','COMPARATIVOS','MENORQ',
        'IMENORQ','MAYORQ','IMAYORQ','IPARENT','DPARENT','COMA','SEMICOMA','PUNTO','UPDATE']

t_ignore= ' \t\n'
t_SUMA=r'\+'
t_ASIGNACION=r'='
t_RESTA=r'\-'
t_MULTIPLICACION=r'\*'
t_DIVISION=r'/'
t_ODD=r'OOD'
t_COMPARATIVOS=r'<>'
t_MENORQ=r'<'
t_IMENORQ=r'<='
t_MAYORQ=r'>'
t_IMAYORQ=r'>='
t_IPARENT=r'\('
t_DPARENT=r'\)'
t_COMA=r','
t_SEMICOMA=r';'
t_PUNTO=r'\.'
t_UPDATE=r':='

def buscarFicheros(directorio):
    ficheros=[]
    numArchivo=''
    respuesta=False
    cont=1
    for base,dirs,files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print (str(cont)+"."+file)
        cont=cont+1
    while respuesta == False:
        numArchivo= input('\nNumero del test: ')
        for file in files :
            if file==files[int(numArchivo)-1]:
                respuesta=True
                break
    print ("has escogido \"%s\"\n" %files[int(numArchivo)-1])
    return files[int(numArchivo)-1]
    
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper()in palabrasReservadas:
        t.value=t.value.upper()
        t.type=t.value
    return t
def t_COMENTARIO(t):
    r'\#.*'
    pass
def t_NUMERO(t):
    r'\d+'
    t.value=int(t.value)
    return t
def t_error(t):
    print ("caracter ilegal :  '%s'"%t.value[0])
    t.lexer.skip(1)

directorio = "/Users/HP-PC/Documents/python programas/analizador lexico/test/"
archivo= buscarFicheros(directorio)
test=directorio+archivo
fp=codecs.open(test,"r","utf-8")
cadena=fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok=analizador.token()
    if not tok :break
    print(tok)
    
