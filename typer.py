from adafruit_hid.keycode import Keycode as K
import time

class typer:
    def __init__(self,ke):
        self.keyboard = ke
        
    def type(self, words):
        time.sleep(0.1)
        for letter in words:
            time.sleep(0.05)
            if letter == 'a' :
                self.keyboard.send(K.A)
                continue
            if letter == 'b' :
                self.keyboard.send(K.B)
                continue
            if letter == 'c' :
                self.keyboard.send(K.C)
                continue
            if letter == 'd' :
                self.keyboard.send(K.D)
                continue
            if letter == 'e' :
                self.keyboard.send(K.E)
                continue
            if letter == 'f' :
                self.keyboard.send(K.F)
                continue
            if letter == 'g' :
                self.keyboard.send(K.G)
                continue
            if letter == 'h' :
                self.keyboard.send(K.H)
                continue
            if letter == 'i' :
                self.keyboard.send(K.I)
                continue
            if letter == 'j' :
                self.keyboard.send(K.J)
                continue
            if letter == 'k' :
                self.keyboard.send(K.K)
                continue
            if letter == 'l' :
                self.keyboard.send(K.L)
                continue
            if letter == 'm' :
                self.keyboard.send(K.M)
                continue
            if letter == 'n' :
                self.keyboard.send(K.N)
                continue
            if letter == 'o' :
                self.keyboard.send(K.O)
                continue
            if letter == 'p' :
                self.keyboard.send(K.P)
                continue
            if letter == 'q' :
                self.keyboard.send(K.Q)
                continue
            if letter == 'r' :
                self.keyboard.send(K.R)
                continue
            if letter == 's' :
                self.keyboard.send(K.S)
                continue
            if letter == 't' :
                self.keyboard.send(K.T)
                continue
            if letter == 'u' :
                self.keyboard.send(K.U)
                continue
            if letter == 'v' :
                self.keyboard.send(K.V)
                continue
            if letter == 'w' :
                self.keyboard.send(K.W)
                continue
            if letter == 'x' :
                self.keyboard.send(K.X)
                continue
            if letter == 'y' :
                self.keyboard.send(K.Y)
                continue
            if letter == 'z' :
                self.keyboard.send(K.Z)
                continue
            if letter == 'A' :
                self.keyboard.send(K.SHIFT ,K.A)
                continue
            if letter == 'B' :
                self.keyboard.send(K.SHIFT ,K.B)
                continue
            if letter == 'C' :
                self.keyboard.send(K.SHIFT ,K.C)
                continue
            if letter == 'D' :
                self.keyboard.send(K.SHIFT ,K.D)
                continue
            if letter == 'E' :
                self.keyboard.send(K.SHIFT ,K.E)
                continue
            if letter == 'F' :
                self.keyboard.send(K.SHIFT ,K.F)
                continue
            if letter == 'G' :
                self.keyboard.send(K.SHIFT ,K.G)
                continue
            if letter == 'H' :
                self.keyboard.send(K.SHIFT ,K.H)
                continue
            if letter == 'I' :
                self.keyboard.send(K.SHIFT ,K.I)
                continue
            if letter == 'J' :
                self.keyboard.send(K.SHIFT ,K.J)
                continue
            if letter == 'K' :
                self.keyboard.send(K.SHIFT ,K.K)
                continue
            if letter == 'L' :
                self.keyboard.send(K.SHIFT ,K.L)
                continue
            if letter == 'M' :
                self.keyboard.send(K.SHIFT ,K.M)
                continue
            if letter == 'N' :
                self.keyboard.send(K.SHIFT ,K.N)
                continue
            if letter == 'O' :
                self.keyboard.send(K.SHIFT ,K.O)
                continue
            if letter == 'P' :
                self.keyboard.send(K.SHIFT ,K.P)
                continue
            if letter == 'Q' :
                self.keyboard.send(K.SHIFT ,K.Q)
                continue
            if letter == 'R' :
                self.keyboard.send(K.SHIFT ,K.R)
                continue
            if letter == 'S' :
                self.keyboard.send(K.SHIFT ,K.S)
                continue
            if letter == 'T' :
                self.keyboard.send(K.SHIFT ,K.T)
                continue
            if letter == 'U' :
                self.keyboard.send(K.SHIFT ,K.U)
                continue
            if letter == 'V' :
                self.keyboard.send(K.SHIFT ,K.V)
                continue
            if letter == 'W' :
                self.keyboard.send(K.SHIFT ,K.W)
                continue
            if letter == 'X' :
                self.keyboard.send(K.SHIFT ,K.X)
                continue
            if letter == 'Y' :
                self.keyboard.send(K.SHIFT ,K.Y)
                continue
            if letter == 'Z' :
                self.keyboard.send(K.SHIFT ,K.Z)
                continue
            if letter.upper() == '1' :
                self.keyboard.send(K.ONE)
                continue
            if letter.upper() == '2' :
                self.keyboard.send(K.TWO)
                continue
            if letter.upper() == '3' :
                self.keyboard.send(K.THREE)
                continue
            if letter.upper() == '4' :
                self.keyboard.send(K.FOUR)
                continue
            if letter.upper() == '5' :
                self.keyboard.send(K.FIVE)
                continue
            if letter.upper() == '6' :
                self.keyboard.send(K.SIX)
                continue
            if letter.upper() == '7' :
                self.keyboard.send(K.SEVEN)
                continue
            if letter.upper() == '8' :
                self.keyboard.send(K.EIGHT)
                continue
            if letter.upper() == '9' :
                self.keyboard.send(K.NINE)
                continue
            if letter.upper() == '0' :
                self.keyboard.send(K.ZERO)
                continue
            if letter.upper() == ' ' :
                self.keyboard.send(K.SPACE)
                continue
            if letter.upper() == '-' :
                self.keyboard.send(K.MINUS)
                continue
            if letter.upper() == '_' :
                self.keyboard.send(K.SHIFT, K.MINUS)
                continue
            if letter.upper() == '=' :
                self.keyboard.send(K.EQUALS)
                continue
            if letter.upper() == '_' :
                self.keyboard.send(K.SHIFT, K.EQUALS)
                continue
            if letter.upper() == '[' :
                self.keyboard.send(K.LEFT_BRACKET)
                continue
            if letter.upper() == '{' :
                self.keyboard.send(K.SHIFT, K.LEFT_BRACKET)
                continue
            if letter.upper() == ']' :
                self.keyboard.send(K.RIGHT_BRACKET)
                continue
            if letter.upper() == '}' :
                self.keyboard.send(K.SHIFT, K.RIGHT_BRACKET)
                continue
            if letter.upper() == '\\' :
                self.keyboard.send(K.BACKSLASH)
                continue
            if letter.upper() == '|' :
                self.keyboard.send(K.SHIFT, K.BACKSLASH)
                continue
            if letter.upper() == '#' :
                self.keyboard.send(K.POUND)
                continue
            if letter.upper() == '|' :
                self.keyboard.send(K.SHIFT, K.POUND)
                continue
            if letter.upper() == ';' :
                self.keyboard.send(K.SEMICOLON)
                continue
            if letter.upper() == ':' :
                self.keyboard.send(K.SHIFT, K.SEMICOLON)
                continue
            if letter.upper() == "'" :
                self.keyboard.send(K.QUOTE)
                continue
            if letter.upper() == '"' :
                self.keyboard.send(K.SHIFT, K.QUOTE)
                continue
            if letter.upper() == '~' :
                self.keyboard.send(K.SHIFT, K.GRAVE_ACCE)
                continue
            if letter.upper() == "," :
                self.keyboard.send(K.COMMA)
                continue
            if letter.upper() == '<' :
                self.keyboard.send(K.SHIFT, K.COMMA)
                continue
            if letter.upper() == "." :
                self.keyboard.send(K.PERIOD)
                continue
            if letter.upper() == '>' :
                self.keyboard.send(K.SHIFT, K.PERIOD)
                continue
            if letter.upper() == "/" :
                self.keyboard.send(K.FORWARD_SLASH)
                continue
            if letter.upper() == '?' :
                self.keyboard.send(K.SHIFT, K.FORWARD_SLASH )
                continue
            if letter.upper() == '!' :
                self.keyboard.send(K.SHIFT, K.ONE)
                continue
            if letter.upper() == '@' :
                self.keyboard.send(K.SHIFT, K.TWO)
                continue
            if letter.upper() == '#' :
                self.keyboard.send(K.SHIFT, K.THREE)
                continue
            if letter.upper() == '$' :
                self.keyboard.send(K.SHIFT, K.FOUR)
                continue
            if letter.upper() == '%' :
                self.keyboard.send(K.SHIFT, K.FIVE)
                continue
            if letter.upper() == '^' :
                self.keyboard.send(K.SHIFT, K.SIX)
                continue
            if letter.upper() == '&' :
                self.keyboard.send(K.SHIFT, K.SEVEN)
                continue
            if letter.upper() == '*' :
                self.keyboard.send(K.SHIFT, K.EIGHT)
                continue
            if letter.upper() == '(' :
                self.keyboard.send(K.SHIFT, K.NINE)
                continue
            if letter.upper() == ')' :
                self.keyboard.send(K.SHIFT, K.ZERO)
                
        time.sleep(0.1)

    def admin(self):
        time.sleep(0.05)
        self.keyboard.send(K.SHIFT, K.CONTROL, K.ENTER)
        time.sleep(1)
        self.keyboard.send(K.LEFT_ARROW)
        time.sleep(0.09)
        self.keyboard.send(K.ENTER)
        time.sleep(0.08)
        
        
    def run(self,command, admin=False):
        time.sleep(0.08)
        self.keyboard.send(K.WINDOWS, K.R)
        time.sleep(0.08)
        self.type(command)
        time.sleep(0.5)
        if admin:
            self.admin()
        else:
            self.keyboard.send(K.ENTER)
            time.sleep(0.08)
        
    def cmd(self, command, admin=False):
        time.sleep(0.08)
        if admin:
            self.run("cmd",True)
        else:
            self.run("cmd")
         
        time.sleep(0.08)
        self.type(command)
        time.sleep(0.08)
        self.keyboard.send(K.ENTER)
        time.sleep(0.08)
        
    def powershell(self, command, admin=False):
        if admin:
            self.run("powershell", True)
        else:
            self.run("powershell")
        time.sleep(0.9)
        self.type(command)
        time.sleep(1)
        self.keyboard.send(K.ENTER)
        time.sleep(0.08)
        
    def enter(self):
        time.sleep(0.05)
        self.keyboard.send(K.ENTER)
        time.sleep(0.05)
        
            
            

