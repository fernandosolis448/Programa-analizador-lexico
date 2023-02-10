import ply.lex as lex 

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVICION',
    'ID',
)

reserved = {
    'if':'CONDICIONAL',
    'else':'SI_NO',
    'then':'ENTONCES',
    'while':'CICLO_MIENTRAS',
    'for':'CICLO_PARA',
    'Continue':'CONTINUE',
    'false':'FALSO',
    'or':'O',
    'and':'Y',
    'from':'DE',
    'break':'ROMPER',
    'global':'GLOBALES',
    'assert':'AFIRMAR',
    'import':'IMPORTAR',
    'class':'CLASE',
    'finally':'FINALIZAR',
    'del':'DEL',
    'elif':'ELIF',
    'exec':'EXEC',
    'in':'EN',
    'new':'NUEVO',
    'typedef':'DECLARACION',
	'sizeof' : 'OPERADOR',
	'Operator':'OPERADOR',
	'assert' : 'DEFINIR',
	'Boolean':'SI_NO',
	'Break':'PARA',
 	'catch': 'INTENTAR',
	'class':'CLASE',
	'const':'COSNTANTE',
	'continue':'CONTINUAR',
	'default':'DEFECTO',
	'do':'HACER',
	'double':'DECIMAL',
	'else':'SI_NO',
	'enum' : 'REPRESENTAR',
	'extends':'EXTENCION',
	'false': 'FALSO',
	'final':'FINAL',
	'finally':'FINALMENTE',
	'Goto' : 'TRANSFERIR',
	'implements':'IMPLEMENTOS',
	'import':'IMPOTAR',
	'Inner' : 'SELECCIONAR',
	'Instanceof' : 'VERIFICAR',
                     
    }

tokens = list(tokens) + list(reserved.values())

# Expresiones regulares de conocimiento

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVICION = r'/'




# Caracteres Ignorados
t_ignore = ' \t' '\n'


#Manejo de errores
def t_error(t):
    print("Token desconocido: '%s'" % t.value[0] )
    t.lexer.skip(1)
    
lexer = lex.lex()

#empieza
with open('data.txt', 'r') as archivo:
# archivo = open('data.txt', 'r')
    data = archivo.read()
    lexer.input(data) 

     
    
# archivo.close()
#termina

#data = '3234123 + 4 * -abc if else then'


while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)