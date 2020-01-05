from time import sleep
import RPi.GPIO as GPIO

led_pin = 7	# physical
time_unit = .2	# seconds

convert_dict = {'a': ' .-', 'b': ' -...', 'c': ' -.-.', 'd': ' -..', 'e': ' .', 'f': ' ..-.', 'g': ' --.', 'h': ' ....', 'i': ' ..', 'j': ' .---', 'k': ' -.-', 'l': ' .-..', 'm': ' --', 'n': ' -.', 'o': ' ---', 'p': ' .--.', 'q': ' --.-', 'r': ' .-.', 's': ' ...', 't': ' -', 'u': ' ..-', 'v': ' ..-', 'w': ' .--', 'x': ' -..-', 'y': ' -.--', 'z': ' --..', ' ': '5', '0': ' -----', '1': ' .----', '2': ' ..---', '3': ' ...--', '4': ' ....-', '5': ' .....', '6': ' -....', '7': ' --...', '8': ' ---..', '9': ' ----.', '.': ' .-.-.-', ',': ' --..--', '?': ' ..--..', '!': ' ..--.', ':': ' ---...', '"': ' .-..-.', "'": ' .----.', '=': ' -...-'}
available = convert_dict.keys()

def convertToMorse(s):
	converted = ''
	for char in s.lower():
		if char in  available:
			converted += convert_dict[char]
		else:
			print("Char '" + char + "' is not avaiable and was omitted.")
	return converted

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
def executeMorseString(s):
	print('Flashing morse string:', s, len(s))
	for char in s:
		print('Flashing', char)
		if char == '.':
			length = 1
			light = True
		elif char == '-':
			length = 3
			light = True
		elif char == ' ':
			length = 1
			light = False
		else:
			length = int(char)
			light = False
		sleep(time_unit)
		if light:
			GPIO.output(led_pin, 1)
		sleep(time_unit*length)
		GPIO.output(led_pin, 0)

s = input('Message to morse: ')
while s:
	executeMorseString(convertToMorse(s))
	s = input('Message to morse: ')