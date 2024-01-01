from time import time

print('Press Enter to start typing or break a new line.')
print('Press Enter twice to finish typing')
input('------------------------------------------------')

# Record timestamp when user is typing
start = time()

text = []
while True:
    line = input()
    if not line:
        break
    text.append(line)

# Record timestamp when user finishes typing
end = time()
print('------------------------------------------------')

elapsedTime = (end-start) / 60
charsCount = sum(len(item) for item in text)
wordsCount = charsCount / 5

wpm = round(wordsCount / elapsedTime)

print(f'Your average WPM is {wpm}')
if wpm < 50:
    print('You have Average Speed')
elif wpm < 60:
    print('You have Above Average Speed')
elif wpm < 70:
    print('You have Productive Speed')
elif wpm < 120:
    print('You have High Speed')
elif wpm > 120:
    print('You have a Competitive speed')