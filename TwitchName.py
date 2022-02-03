import subprocess
import time

fhand = r"new.txt"

available_lst = []
with open(fhand, "r") as words:
	for word in words:
		word = word.rstrip()
		print(word)
		cmd = 'twitch api get users -q login='+word
		result = str(subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0])
		if len(result) < 25:
			available_lst.append(word)
		print(available_lst)

print(available_lst)