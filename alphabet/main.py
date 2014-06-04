import random
import string

def next_rnd(value):
  bit1 = (value >> 1) & 1
  bit9 = (value >> 1) & 1
  leftmostbit = bit1 ^ bit9
  return (leftmostbit) | (value >> 1)
def game():
  while(True):
    first = random.choice(string.ascii_lowercase)
    second = random.choice(string.ascii_lowercase)
    is_before = first < second
    is_after = first > second
    question = 'is '
    question += first
    question += ' before '
    question += second
    question += '?'
    answer = input(question)
    if (answer == 'yes' and is_before) or (answer == 'no' and not is_before):
      print('correct')
    else:
      print('incorrect')
def get_question():
  if()
game()
