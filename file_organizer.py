import os
 
dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
        try:
            if file.endswith('.jpg'):
                jpgs()
            elif file.endswith('.png'):
                pngs()
        except FileNotFoundError:
             quit()

def jpgs():
   destination = f'D:\\Downloadpics\\jpgs\\{str(file)}'
   source = f'D:\\{str(file)}'
   os.replace(source, destination)

def pngs():
  destination = f'D:\\Downloadpics\\pngs\\{str(file)}'
  source = f'D:\\{str(file)}'
  os.replace(source, destination)

def quit():
  print("Complete run")
  exit()
