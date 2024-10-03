import words,guessable,random,string

def clear() -> None:
  print('\x1b[2J;H')

def drawletters(letterinfo) -> None:
  print("\x1b[20G[",end='')
  for i in letterinfo.keys():
    print(f'\x1b[{str(letterinfo[i])}m{i}\x1b[0m',end='')
  print('\x1b[0m]\x1b[0G',end='')
  
guessable.words.extend(words.words)
while 1:
  try:
    word = random.choice(words.words)
    letterinfo = {}
    for i in string.ascii_lowercase:
      letterinfo[i] = 90
    for i in range(6):
      correct=False
      attempt = ''
      while not attempt in guessable.words:
        drawletters(letterinfo)
        attempt = input(f"{i+1} > ")
        if attempt not in guessable.words:
          print('\x1b[1F\x1b[2K',end='')
      if attempt == word:
        print(f"\x1b[1F\x1b[2K\x1b[4C\x1b[32m{attempt}\x1b[0m")
        print(f"Correct! Took {i+1} tries!")
        correct = True
        break
      else:
        print("\x1b[1F\x1b[4C",end='')
        for index,i in enumerate(attempt):
          if i == word[index]:
            print(f"\x1b[32m{i}\x1b[0m",end="")
            letterinfo[i] = 32
          elif i in word:
            print(f"\x1b[33m{i}\x1b[0m",end="")
            if letterinfo[i] != 32:
              letterinfo[i] = 33
          else:
            print(f"\x1b[31m{i}\x1b[0m",end="")
            letterinfo[i] = 31
        print("")
    if not correct:
      print(f"Wrong! Word was: {word}")
  except KeyboardInterrupt:
    print("quitting...")
    exit(0)
  except Exception as e:
    print(e)
    exit()
