import time

# Change if needed
pause=0.01
fromD='C:/1/one_file.xml'
toD='C:/2/another_file.xml'

#
print('Copying file ...')
with open(fromD, 'rb') as inFile:
	with open(toD, 'wb') as outFile:
		while True:
			time.sleep(pause)
			byte = inFile.read(1)
			if byte:
				outFile.write(byte)
			else: break
print('Finished')