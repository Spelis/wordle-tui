import string

with open('words.txt') as f:
  newwords = []
  f = f.read()
  f = f.split('\n')
  for word in f:
    if word.isalpha():
      if len(word) == 5:
        newwords.append(word.lower())
  with open('guessable.py','w') as r:
    r.write(f'words = {str(newwords)}')
  print(f"dictionary size: {len(newwords)}")
