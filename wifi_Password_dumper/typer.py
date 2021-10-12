from adafruit_hid.keycode import Keycode as K
import time

def type(keyboard, words):
	#TODO add support for case  
	for letter in words:
		time.sleep(0.05)
		if letter.upper() == 'A' :
			keyboard.send(K.A)
			continue
		if letter.upper() == 'B' :
			keyboard.send(K.B)
			continue
		if letter.upper() == 'C' :
			keyboard.send(K.C)
			continue
		if letter.upper() == 'D' :
			keyboard.send(K.D)
			continue
		if letter.upper() == 'E' :
			keyboard.send(K.E)
			continue
		if letter.upper() == 'F' :
			keyboard.send(K.F)
			continue
		if letter.upper() == 'G' :
			keyboard.send(K.G)
			continue
		if letter.upper() == 'H' :
			keyboard.send(K.H)
			continue
		if letter.upper() == 'I' :
			keyboard.send(K.I)
			continue
		if letter.upper() == 'J' :
			keyboard.send(K.J)
			continue
		if letter.upper() == 'K' :
			keyboard.send(K.K)
			continue
		if letter.upper() == 'L' :
			keyboard.send(K.L)
			continue
		if letter.upper() == 'M' :
			keyboard.send(K.M)
			continue
		if letter.upper() == 'N' :
			keyboard.send(K.N)
			continue
		if letter.upper() == 'O' :
			keyboard.send(K.O)
			continue
		if letter.upper() == 'P' :
			keyboard.send(K.P)
			continue
		if letter.upper() == 'Q' :
			keyboard.send(K.Q)
			continue
		if letter.upper() == 'R' :
			keyboard.send(K.R)
			continue
		if letter.upper() == 'S' :
			keyboard.send(K.S)
			continue
		if letter.upper() == 'T' :
			keyboard.send(K.T)
			continue
		if letter.upper() == 'U' :
			keyboard.send(K.U)
			continue
		if letter.upper() == 'V' :
			keyboard.send(K.V)
			continue
		if letter.upper() == 'W' :
			keyboard.send(K.W)
			continue
		if letter.upper() == 'X' :
			keyboard.send(K.X)
			continue
		if letter.upper() == 'Y' :
			keyboard.send(K.Y)
			continue
		if letter.upper() == 'Z' :
			keyboard.send(K.Z)
			continue
		if letter.upper() == '1' :
			keyboard.send(K.ONE)
			continue
		if letter.upper() == '2' :
			keyboard.send(K.TWO)
			continue
		if letter.upper() == '3' :
			keyboard.send(K.THREE)
			continue
		if letter.upper() == '4' :
			keyboard.send(K.FOUR)
			continue
		if letter.upper() == '5' :
			keyboard.send(K.FIVE)
			continue
		if letter.upper() == '6' :
			keyboard.send(K.SIX)
			continue
		if letter.upper() == '7' :
			keyboard.send(K.SEVEN)
			continue
		if letter.upper() == '8' :
			keyboard.send(K.EIGHT)
			continue
		if letter.upper() == '9' :
			keyboard.send(K.NINE)
			continue
		if letter.upper() == '0' :
			keyboard.send(K.ZERO)
			continue
		if letter.upper() == ' ' :
			keyboard.send(K.SPACE)
			continue
		if letter.upper() == '-' :
			keyboard.send(K.MINUS)
			continue
		if letter.upper() == '_' :
			keyboard.send(K.SHIFT, K.MINUS)
			continue
		if letter.upper() == '=' :
			keyboard.send(K.EQUALS)
			continue
		if letter.upper() == '_' :
			keyboard.send(K.SHIFT, K.EQUALS)
			continue
		if letter.upper() == '[' :
			keyboard.send(K.LEFT_BRACKET)
			continue
		if letter.upper() == '{' :
			keyboard.send(K.SHIFT, K.LEFT_BRACKET)
			continue
		if letter.upper() == ']' :
			keyboard.send(K.RIGHT_BRACKET)
			continue
		if letter.upper() == '}' :
			keyboard.send(K.SHIFT, K.RIGHT_BRACKET)
			continue
		if letter.upper() == '\\' :
			keyboard.send(K.BACKSLASH)
			continue
		if letter.upper() == '|' :
			keyboard.send(K.SHIFT, K.BACKSLASH)
			continue
		if letter.upper() == '#' :
			keyboard.send(K.POUND)
			continue
		if letter.upper() == '|' :
			keyboard.send(K.SHIFT, K.POUND)
			continue
		if letter.upper() == ';' :
			keyboard.send(K.SEMICOLON)
			continue
		if letter.upper() == ':' :
			keyboard.send(K.SHIFT, K.SEMICOLON)
			continue
		if letter.upper() == "'" :
			keyboard.send(K.QUOTE)
			continue
		if letter.upper() == '"' :
			keyboard.send(K.SHIFT, K.QUOTE)
			continue
		if letter.upper() == '~' :
			keyboard.send(K.SHIFT, K.GRAVE_ACCE)
			continue
		if letter.upper() == "," :
			keyboard.send(K.COMMA)
			continue
		if letter.upper() == '<' :
			keyboard.send(K.SHIFT, K.COMMA)
			continue
		if letter.upper() == "." :
			keyboard.send(K.PERIOD)
			continue
		if letter.upper() == '>' :
			keyboard.send(K.SHIFT, K.PERIOD)
			continue
		if letter.upper() == "/" :
			keyboard.send(K.FORWARD_SLASH)
			continue
		if letter.upper() == '?' :
			keyboard.send(K.SHIFT, K.FORWARD_SLASH )
			continue
		if letter.upper() == '!' :
			keyboard.send(K.SHIFT, K.ONE)
			continue
		if letter.upper() == '@' :
			keyboard.send(K.SHIFT, K.TWO)
			continue
		if letter.upper() == '#' :
			keyboard.send(K.SHIFT, K.THREE)
			continue
		if letter.upper() == '$' :
			keyboard.send(K.SHIFT, K.FOUR)
			continue
		if letter.upper() == '%' :
			keyboard.send(K.SHIFT, K.FIVE)
			continue
		if letter.upper() == '^' :
			keyboard.send(K.SHIFT, K.SIX)
			continue
		if letter.upper() == '&' :
			keyboard.send(K.SHIFT, K.SEVEN)
			continue
		if letter.upper() == '*' :
			keyboard.send(K.SHIFT, K.EIGHT)
			continue
		if letter.upper() == '(' :
			keyboard.send(K.SHIFT, K.NINE)
			continue
		if letter.upper() == ')' :
			keyboard.send(K.SHIFT, K.ZERO)
