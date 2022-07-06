import random
import re
import os
from colorama import init, Fore, Style

init()

questions = [
"Enter the command to locate bad sectors and recover readable information on a Windows system.", 
"Enter the command to display a list of currently running processes on a Windows system.",
"Enter the command to list files and directories on a Windows system.",
"Enter the command to change the working directory on a Windows system.",
"Enter the command to go back one directory on a Windows system.",
"Enter the command to wait 10 seconds then shutdown a Windows system.",
"Enter the command to wait 10 seconds then restart a Windows system.",
"Enter the command to abort a shutdown countdown on a Windows system.",
"Enter the command to open the Deployment Image Servicing and Management tool.",
"Enter the command to scan the integrity of all protected system files.",
"Enter the command to fix logical file system errors on the disk on a Windows system.",
"Enter the command to start the partition command interpreter on a Windows system.",
"Enter the command to terminate notepad.exe on a Windows system.",
"Enter the command to terminate process ID 69 and all child processes on a Windows system.",
]
answers = [
"chkdsk /r", 
"tasklist",
"dir",
"cd",
"..",
"shutdown /s /t 10",
"shutdown /s /r 10",
"shutdown /a",
"dism",
"sfc /scannow",
"chkdsk /f",
"diskpart",
"taskkill /im notepad.exe",
"taskkill /pid 69 /t",

]


def cls():
	os.system('cls')

def pwc(s, color=Fore.WHITE, **kwargs):
    print(f"{color}{s}{Style.RESET_ALL}", **kwargs)

correct_answers = 0
wrong_answers = 0

isActive = True
while isActive:
	q_number = random.choice(range(0, len(questions)))			
	question = questions[q_number]
	answer = answers[q_number]
	
	cls()		
	print(f"{Fore.GREEN}Correct: " + str(correct_answers) + f"{Fore.RED}     Wrong: " + str(wrong_answers))	
	print(f"{Fore.WHITE}Total questions remaining: " + str(len(questions)-1))
	pwc("<<Type 'q' to quit>>\n", Fore.RED)
	pwc(question, Fore.YELLOW)
	response = input("> ")
	if response == "q":
		isActive = False
	elif response == answer:
		pwc("Correct!", Fore.GREEN)
		input("Press any key...")		
		questions.remove(questions[q_number])		
		answers.remove(answers[q_number])
		correct_answers += 1
	else:
		pwc("Wrong.", Fore.RED)
		input("Press any key...")
		wrong_answers += 1

	if len(questions) == 0:
		quit()


