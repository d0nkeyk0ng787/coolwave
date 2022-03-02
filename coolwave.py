#! /usr/bin/env python3
# Generate a cool wave in the terminal

import time

x = "----------"

count = 0
indent = " "
indentamount = 1


while True:

	if count > 16:
		while count > 1:
			print((indent * indentamount) + x)
			indentamount = indentamount - 1
			count = count - 1
			time.sleep(0.05)
	else:
		pass

	print((indent * indentamount) + x)
	indentamount = indentamount + 1
	count = count + 1
	time.sleep(0.05)