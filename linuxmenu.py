import os
import getpass
from platform import system


def logo():
	if system() == 'Linux':
		os.system("clear")
		os.system("figlet -f standard -c Basic Linux | lolcat")

	elif system() == 'Windows':
		os.system("cls")


def localExecution():
	while(True):
		os.system("clear")
		logo()
		print("""
	\033[36m[1] Date Command
	\033[36m[2] Cal Command
	\033[36m[3] List contents
	\033[36m[4] Create directory
	\033[36m[5] Remove directory
	\033[36m[6] Create file
	\033[36m[7] Delete file
	\033[36m[8] Start web server
	\033[36m[9] Stop web server
	\033[36m[0] Exit
		\033[97m""")
		choice = int(input("Enter Choice : "))
		if choice == 1:
			os.system("date")
			input("Press enter to continue")
		elif choice == 2:
			os.system("cal")
			input("Press enter to continue")
		elif choice == 3:
			os.system("ls -l")
			input("Press enter to continue")
		elif choice == 4:
			dir_name = input("Enter directory name : ")
			os.system("mkdir " + dir_name)
			input("Press enter to continue")
		elif choice == 5:
			dir_name = input("Enter directory name : ")
			os.system("rmdir " + dir_name)
			input("Press enter to continue")
		elif choice == 6:
			file_name = input("Enter file name : ")
			os.system("touch " + file_name)
			input("Press enter to continue")
		elif choice == 7:
			file_name = input("Enter file name : ")
			os.system("rm " + file_name)
			input("Press enter to continue")
		elif choice == 8:
			os.system("systemctl start httpd")
			input("Press enter to continue")
		elif choice == 9:
			os.system("systemctl stop httpd")
			input("Press enter to continue")
		elif choice == 0:
			break
		else:
			print("Invalid choice")
			input("Press enter to continue")


def remoteExecution():
	ip = input("Enter remote system ip")
	uname = input("Enter username")
	password = getpass.getpass("Enter password")
	while(True):
		os.system("clear")
		logo()
		print("""
	\033[36m[1] Access remote system
	\033[36m[2] Date Command
	\033[36m[3] Cal Command
	\033[36m[4] List contents
	\033[36m[5] Create directory
	\033[36m[6] Remove directory
	\033[36m[7] Create file
	\033[36m[8] Delete file
	\033[36m[9] Start web server
	\033[36m[10] Stop web server
	\033[36m[0] Exit
		\033[97m""")
		choice = int(input("Enter Choice : "))
		if choice == 1:
			os.system("sshpass -p " + password +
			          " ssh -o StrictHostKeyChecking=no " + uname + "@" + ip)
			input("Press enter to continue")
		elif choice == 2:
			os.system("sshpass -p " + password +
			          " ssh -o StrictHostKeyChecking=no " + uname + "@" + ip + " date")
			input("Press enter to continue")
		elif choice == 3:
			os.system("sshpass -p " + password +
			          " ssh -o StrictHostKeyChecking=no " + uname + "@" + ip + " cal")
			input("Press enter to continue")
		elif choice == 4:
			os.system("sshpass -p " + password +
			          " ssh -o StrictHostKeyChecking=no " + uname + "@" + ip + " ls -l")
			input("Press enter to continue")
		elif choice == 5:
			dir_name = input("Enter directory name : ")
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " mkdir " + dir_name)
			input("Press enter to continue")
		elif choice == 6:
			dir_name = input("Enter directory name : ")
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " rmdir " + dir_name)
			input("Press enter to continue")
		elif choice == 7:
			file_name = input("Enter file name : ")
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " touch " + file_name)
			input("Press enter to continue")
		elif choice == 8:
			file_name = input("Enter file name : ")
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " rm " + file_name)
			input("Press enter to continue")
		elif choice == 9:
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " systemctl start httpd")
			input("Press enter to continue")
		elif choice == 10:
			os.system("sshpass -p " + password + " ssh -o StrictHostKeyChecking=no " +
			          uname + "@" + ip + " systemctl stop httpd")
			input("Press enter to continue")
		elif choice == 0:
			break
		else:
			print("Invalid choice")
			input("Press enter to continue")


def linuxBasics():
	while(True):
		os.system("clear")
		logo()
		print("""
	\033[36m[1] Local Execution
	\033[36m[2] Remote Execution
	\033[36m[0] Return to the Menu
	\033[91m[99] Exit From The Software
		\033[97m""")
		choice = int(input("Enter Choice : "))
		if choice == 1:
			localExecution()
			input("Press enter to continue")
		elif choice == 2:
			remoteExecution()
			input("Press enter to continue")
		elif choice == 0:
			os.system("python3 menu.py")
		elif choice == 99:
			exit()
		else:
			print("Invalid Choice")
			input("Press enter to continue")


linuxBasics()
