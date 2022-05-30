def GetInt(msg):
 while(True):
  try:
     k = int(input(msg))
     return k
  except ValueError as e:
    print("Input Integer Only...")

def GetFloat(msg):
 while(True):
  try:
     k = float(input(msg))
     return k
  except ValueError as e:
    print("Input Real Number Only...")
