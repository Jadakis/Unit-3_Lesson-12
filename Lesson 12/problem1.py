import time
import random

print('-' * 65)
print(' I am a Magic Eight Ball! ')
print()
question = input(' What is your question? ')
time.sleep(1)
print(' . . Shacking . .')
time.sleep(1)
print(' . . . Thinking . . .')
time.sleep(1)

choice = random.randint(1,4)

if choice == 1:
	print('Mortal Kombat!!!')
elif choice == 2:
	print('Yes!')
elif choice == 3:
	print(' One, Two, Freddy\'s coming for you. Three, Four, better lock your doors. Five, Six, Grab your Crucifx. Seven, Eight, Gonna stay up late. Nine, Ten, Never sleep again! ')
elif choice == 4:
	print('Run!')	