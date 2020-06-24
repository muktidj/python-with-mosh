command = ""
started = False
while True:
      command = input(">  ").lower()
      if command == 'start':
          if started:
              print('Car is already started')
          else:
              started = True
              print('Car started...')
      elif command == 'stop':
          if not started:
              print('Car is already stopped')
          else:
              started = False
              print('Car stoped..')
      elif command == 'help':
        print("""
start - to started car
stop - to stopped car
quit - to quit game
        """)
      elif command == 'quit':
          break
      else:
          print("Sorry i don't understand command")