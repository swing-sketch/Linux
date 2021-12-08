
DIGITS="0123456789"

TT_INT="INT"
TT_FLOAT="FLOAT"
TT_PLUS="PLUS"
TT_MINUS="MINUS"
TT_MUL="MUL"
TT_DIV="DIV"
TT_LPAREN="LPAREN"
TT_RPAREN="RPAREN"

class error(object):
    def __init__(self,pos_start,pos_end,error_name,details):
        self.pos_start=pos_start
        self.pos_end=pos_end
        self.error_name=error_name
        self.details=details
    def as_string(self):
        res=f'{self.error_name}:{self.details}'
        res+=f'File{self.pos_start.fn},line {self.pos_end.ln+1}'
        return res

class IllegalCharError(error):
    def __init__(self,pos_start,pos_end,details):
        super().__init__(pos_start,pos_end,"Illegal Character",details)

class Token(object):
    def __init__(self,type_,value):
        self.type=type_
        self.value=value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'


class Position(object):
    def __init__(self,idx,ln,col,fn,ftxt):
        self.idx=idx
        self.ln=ln
        self.col=col
        self.fn=fn
        self.ftxt=ftxt

    def advance(self,current_char):
        self.idx+=1;
        self.col+=1

        if current_char == '\n':
            self.col=0
            self.ln+=1

    def copy(self):
        return Position(self.idx,self.ln,self.col,self.fn,self.ftxt)

class Lexer(object):
    def __init__(self,fn,text):
        self.fn=fn
        self.text=text
        self.pos=Position(-1,0,-1,fn,text)
        self.current_char=None #dang qian de zi fu
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        if self.pos.idx < len(self.text):
            self.current_char = self.text[self.pos.idx]
        else:
            self.current_char=None
    def make_tokens(self):
        tokens=[]
        while self.current_char != None:
            if self.current_char in (' ','\t'):
                self.advance()
            elif self.current_char in DIGITS:#shuzi
                tokens.oppend(self.make_number())
            elif self.current_char=='+':
                tokens.oppend(Token(TT_PLUS))
                self.advance()
            elif self.current_char=='-':
                tokens.oppend(Token(TT_MINUS))
                self.advance()
            elif self.current_char=='*':
                tokens.oppend(Token(TT_MUL))
                self.advance()
            elif self.current_char=='/':
                tokens.oppend(Token(TT_DIV))
                self.advance()
            elif self.current_char=='(':
                tokens.oppend(Token(TT_LPAREN))
                self.advance()
            elif self.current_char==')':
                tokens.oppend(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start=self.pos.copy()
                char = self.current_char
                self.advance()
                return [],IllegalCharError(pos_start,self.pos,f"'{char}")
        return tokens,None

    def make_number(self):
        num_str=''
        dot_coumt=0

        while self.current_char != None and self.current_char in DIGITS +'.':
            if self.current_char=='.':
                if dot_coumt ==1:
                    break
                dot_coumt+=1
                num_str+='.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_coumt==0:
            return Token(TT_INT,int(num_str))
        else:
            return Token(TT_FLOAT,float(num_str))
