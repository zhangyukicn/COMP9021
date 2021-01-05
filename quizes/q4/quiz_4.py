# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys

symble =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             '_',]

def check_word(words):
    words =words.strip()
    for x in words:
        if x not in symble:
            #print('world not value')
            return False
    #print('world value')
    return True



def is_valid(word, arity):

    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

    #word = word.replace(' ','')
    number_a_z =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number_A_Z =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    charactor=('_')
    if arity == 0:
        for x in word:
            if x not in number_A_Z and x not in number_a_z and x not in charactor:
                #print('1')
                return False

    charactor1=('_',' ')
    if arity > 0:
        if word.count('(')!=word.count(')'):
            #print('11')
            return False

        stack = []
        word_temp =''
        for i in range(len(word)):
            #print('word[i]=',word[i])
            if word[i] == '(':
                if len(word_temp):
                    if not check_word(word_temp):
                        #print('word no')
                        return False
                    word_temp = word_temp.strip()
                    if word_temp != '':
                        stack.append(word_temp)
                    #print('stack(=',stack)
                    word_temp = ''
                    stack.append('(')

            elif word[i] == ',':
                if len(word_temp):
                    if not check_word(word_temp):
                        #print('word ,no')
                        return False
                    word_temp = word_temp.strip()
                    if word_temp != '':
                        stack.append(word_temp)
                    word_temp =''

            elif word[i] == ')':
                if len(word_temp):
                    if not check_word(word_temp):
                        #print('word( no')
                        return False
                    word_temp = word_temp.strip()
                    if word_temp != '':
                        stack.append(word_temp)
                    word_temp=''

                count = -1
                str =''
                while str!='(':
                    str = stack.pop()
                    count = count + 1
                    #print('count',count)
                    #print('stack',stack)
                    #print(str)
                #if count == arity:
                    #continue
                #else:
                if count != arity:
                    #print('234234')
                    return False
                #elif len(stack) == 1:
                     #return True
                #elif len(stack) != 1:
                    #continue

            elif word[i].isalpha() or word[i]in charactor1:
                    #word[i] != '' and (word[i].isalpha() or word[i]in charactor):
                word_temp = word_temp + word[i]
                #print('word_temp=',word_temp)
            #else:
                #eturn False
                #print(word_temp)
                #F(g(a,a), f(a,b))
        if len(stack) == 1:
            return True
        else:
            print('32343242')
            return False
    return True




try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print(''
          'Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')





