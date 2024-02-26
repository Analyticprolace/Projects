list = [1,2,3,4,5,6,7,8,9,10]
condition = True
original_List = list

def printBoard(list):
  print(f"{list[0]}|{list[1]}|{list[2]}")
  print(f"{list[3]}|{list[4]}|{list[5]}")
  print(f"{list[6]}|{list[7]}|{list[8]}")

def change(sign1,sign2,index,turn):
  global list
  if turn == 0 and int(list[index]):
   list[index] = sign1
  elif turn == 1 and int(list[index]):
   list[index] = sign2
  else:
   print("You are tricky but not as tricky as me\nEnter a number where box is empty")
   count -= 1

def check():
    global list
    global condition
    global original_List
    X = ["X","X","X"]
    O = ["O","O","O"]
    if list[0:3] == X or list[0:3] == O:
        print(f"{list[0]} won")
        condition = False
        list = original_List
    elif list[3:6] == X or list[3:6] == O:
        print(f"{list[3]} won")
        condition = False
        list = original_List
    elif list[6:9] == X or list[6:9] == O:
        print(f"{list[6]} won")
        condition = False
        list = original_List
    elif list[0:9:3] == X or list[0:9:3] == O:
        print(f"{list[0]} won")
        condition = False
        list = original_List
    elif list[1:9:3] == X or list[1:9:3] == O:
        print(f"{list[1]} won")
        condition = False
        list = original_List
    elif list[2:9:3] == X or list[2:9:3] == O:
        print(f"{list[2]} won")
        condition = False
        list = original_List
        list = original_List
    elif list[0:9:4] == X or list[0:9:3] == O:
        print(f"{list[0]} won")
        condition = False
        list = original_List
    elif list[1:9:4] == X or list[1:9:3] == O:
        print(f"{list[1]} won")
        condition = False
        list = original_List
    elif list[2:9:4] == X or list[2:9:3] == O:
        print(f"{list[2]} won")
        condition = False

if __name__ == "__main__":
  p1 = input("Enter the name of player 1 or press enter to continue as default name: ").strip() or "Player1"
  p2 = input("Enter the name of player 2 or press enter to continue as default name: ").strip() or "Player2"
  numChoice = int(input(f"Enter 1 for X or 2 for O({p1} turn of selection, The remaining value will automatically be chosen for {p2}): "))
  if numChoice == 1:
    sign1 = "X"
    sign2 = "O"
  elif numChoice == 2:
    sign1 = "O"
    sign2 = "X"
  else:
    print("Enter 1 or 2")
  condition = True
  turn = 0
  count = 0
  while (condition):
    printBoard(list)
    if turn == 0:
      turnWords = p1
    else:
      turnWords = p2
    count += 1
    print(f"Turn: {turnWords}")
    user_input = (int(input("Enter the index of the square you want to change: ")) - 1)
    change(sign1,sign2,user_input,turn)
    check()
    if not(count % 2 == 0):
      turn = 1
    else:
      turn = 0