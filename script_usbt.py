import glob
data_file = []
errors_counter = 0	# общий счетчик ошибок
list_string_check_eds_508a = [									# SW Name & Location
							221, 226, 							# Turbo Ring DIP Switch
							2041, 2043,2068,					#Relay setting (Power + Turbo ring break)
							121, 128, 135, 142, 149,  			#MDIX setting
							904, 909, 913, 917, 922, 927, 		#Turbo Ring V2 Setting
							473, 477, 493,						#Time
							2261]								#LoopProtection

list_string_check_eds_408a = [									# SW Name & Location
							221, 226,							# Turbo Ring DIP Switch
							1538, 1540, 1565, 					#Relay setting (Power + Turbo ring break)
							121, 128, 135, 142, 149, 156,		#MDIX setting
							562, 567, 571, 575, 580, 585, 		#Turbo Ring V2 Setting
							428, 432, 448,						#Time
							1758]								#LoopProtection


for filename_ini in glob.glob('*.ini'):
	print('\n\n##############################################################\n')
	data_file.append('\n\n##############################################################\n\n')
	data_file.append(filename_ini[:-4])
	data_file.append('\n\n')
	errors_counter_one_ini = 0 # счетчик ошибок одного ini файла
	with open(filename_ini) as f_ini:
		list_ini = f_ini.readlines()

	if list_ini[2] == 'ModelName\t\tEDS-408A-3M-ST\n':
		filename_txt = '408.txt'
		with open(filename_txt) as f_txt:
			list_txt = f_txt.readlines()
			for i in list_string_check_eds_408a:
				if list_ini[i] in list_txt:
					print (list_ini[i] + 'OK\n')
					data_file.append(list_ini[i] + 'OK\n\n')
				else:
					print (list_ini[i] + 'CHECK FAILED!!!\n')
					data_file.append(list_ini[i] + 'CHECK FAILED!!!\n\n')
					errors_counter_one_ini += 1

	elif list_ini[2] == 'ModelName\t\tEDS-508A-MM-ST\n':
		filename_txt = '508.txt'
		with open(filename_txt) as f_txt:
			list_txt = f_txt.readlines()
			for i in list_string_check_eds_508a:
				if list_ini[i] in list_txt:
					print (list_ini[i] + 'OK\n')
					data_file.append(list_ini[i] + 'OK\n\n')
				else:
					print (list_ini[i] + 'CHECK FAILED!!!\n')
					data_file.append(list_ini[i] + 'CHECK FAILED!!!\n\n')
					errors_counter_one_ini += 1

	else:
		print ('ERROR!!! Config file not from Switch MOXA EDS-408A-3M-ST or EDS-508A-MM-ST!!!\n')
		data_file.append('ERROR!!! Config file not from Switch MOXA EDS-408A-3M-ST or EDS-508A-MM-ST\n\n')
		errors_counter_one_ini += 1

	print('Errors in .ini file: '+ str(errors_counter_one_ini) + '\n')
	data_file.append('Errors in .ini file: '+ str(errors_counter_one_ini) + '\n\n')

	errors_counter += errors_counter_one_ini
print('Errors in all checked .ini files: '+ str(errors_counter) + '\n')
data_file.append('Errors in all checked .ini files: '+ str(errors_counter) + '\n\n')

with open('result.txt', 'w') as f:
    for i in range(len(data_file)):
        f.write(data_file[i])



		


