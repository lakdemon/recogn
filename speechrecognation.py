import speech_recognition as sr
from subprocess import Popen, PIPE

r = sr.Recognizer()

result = " "

print("Скажите что-нибудь")

while result != "выход":

	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		result = r.recognize_google(audio, language="ru-RU")
     		
		print(result)
		
		#if result == "Джарвис":
			#print("Да, сэр!?")
		if result == "Открой браузер":
			Popen("firefox", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
		if result == "Открой гугл":
			Popen("firefox google.com", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
		if result == "Открой контакт":			
			Popen("firefox vk.com", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
		if result == "Открой проводник":
			Popen("pcmanfm", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
	except sr.UnknownValueError:
		print("Робот не расслышал фразу")
	except sr.RequestError as e:
		print("Ошибка сервиса; {0}".format(e))