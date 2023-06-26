def palidrome():
    slovo = input('введите фразу или слово без пробелов:')
    a = slovo[::-1]
    print(a)
    if slovo == a:
      print(True)
    else:
      print(False)
palidrome()
