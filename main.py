import os, time
todos = []
f = open("todoslist.txt","a")
f = open("todoslist.txt", "r")
todos = eval(f.read())
f.close()


def add():
  time.sleep(2)
  os.system("clear")
  item = input("item to add? ")
  date = input("due date? ")
  priority = input("High, Medium, Low ? ")
  row = [item,date,priority]
  todos.append(row)
  print("Added!")

def view():
  time.sleep(2)
  os.system("clear")
  options = input("1. All \n 2. View by priority")
  if options == "1":
    for row in todos:
      for item in row:
        print(item, end = "|")
    print()
  else:
    priority = input("Which priority?")
    for row in todos:
      if priority in row:
        for item in row:
          print(item, end = "|")
        print()
    print()
  print()
  time.sleep(2)

def edit():
  time.sleep(2)
  os.system("clear")
  check = input("item to edit? ")
  checked = False
  for row in todos:
    if check in row:
      checked = True
    if not checked :
      print("could not find it!")
      return
    for row in todos:
      if check in row:
        #todos.remove(row)
        todos.remove(row)
    item = input("item?")
    date = input("date?")
    priority = input("priority?")
    row = [item,date,priority]
    todos.append(row)

def remove():
  time.sleep(2)
  os.system("clear")
  check = input("item to remove? ")
  for row in todos:
    if check in row:
      todos.remove(row)

while True:
  menu = input("1. Add \n 2. View \n 3. Edit \n 4. Remove > ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  elif menu == "4":
    remove()


  time.sleep(2)
  os.system("clear")
  f = open("todoslist.txt", "w")
  f.write(str(todos))
  f.close()





  





































































































#import os, time
#todos = []
#f = open("todoslist.txt", "r")
#todos = eval(f.read())
#f.close()

#def add():
  #time.sleep(2)
  #os.system("clear")
  #item = input("item to add? ")
  #date = input("due date? ")
  #priority = input("High, Medium, Low ? ")
  #row = [item,date,priority]
  #todos.append(row)
  #print("Added!")

#def view():
  #time.sleep(2)
  #os.system("clear")
  #options = input("1. All \n 2. #View by priority")
  #if options == "1":
    #for row in todos:
      #for item in row:
        #print(item, end = "|")
    #print()
  #else:
    #priority = input("Which priority?")
    #for row in todos:
      #if priority in row:
        #for item in row:
          #print(item, end = "|")
        #print()
    #print()
  #print()
  #time.sleep(2)

#def edit():
  #time.sleep(2)
  #os.system("clear")
  #check = input("item to edit? ")
  #checked = False
  #for row in todos:
    #if check in row:
      #checked = True
    #if not checked :
      #print("could not find it!")
      #return
    #for row in todos:
      #if check in row:
        #todos.remove(row)
        #todos.remove(row)
    #item = input("item?")
    #date = input("date?")
    #priority = input("priority?")
    #row = [item,date,priority]
    #todos.append(row)

#def remove():
  #time.sleep(2)
  #os.system("clear")
  #check = input("item to remove? ")
  #for row in todos:
    #if check in row:
      #todos.remove(row)

#while True:
  #menu = input("1. Add \n 2. View \n 3. Edit \n 4. Remove > ")
  #if menu == "1":
    #add()
  #elif menu == "2":
    #view()
  #elif menu == "3":
    #edit()
  #elif menu == "4":
    #remove()
  

  #time.sleep(2)
  #os.system("clear")
  #f = open("todoslist.txt", "w")
  #f.write(str(todos))
  #f.close()

