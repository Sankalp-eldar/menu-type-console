import mod

def menu3(name,num):
	print('\tMenu\n')
	print('Select one of the following:')
	print('1-Enter data\n2-Display stored data\n3-Search details\n4-Delete entry\n5-Return to Main Menu')
	ch = input()
	a = fields[num]
	if ch == '1':
		mod.add(a,name)
		menu3(name,num)
	elif ch=='2':
		mod.show(a,name)
		input()
		menu3(name,num)
	elif ch == '3':
		mod.search(a,name)
		menu3(name,num)
	elif ch =='4':
		mod.delete(a,name)
		menu3(name,num)
	elif ch=='5':
		print('\n\t****** Exiting Module ******\n')
		menu1()
	else:menu3(name,num)


def menu1():
	print('\tMAIN MENU\n')
	print('Select one of the following:')
	print('1-Customer\n2-Employee\n3-Product\n4-Bill\n5-Exit')
	ch = input()
	if ch =='1':
		print('\n\t******Customer Module******\n')
		menu3(cus,1)
	elif ch =='2':
		print('\n\t******Employee Module******\n')
		menu3(emp,2)
	elif ch == '3':
		print('\n\t******Product Module******\n')
		menu3(pro,3)
	elif ch == '4':
		print('\n\t******Bill Module******\n')
		menu3(bil,4)
	elif ch== '5':
		if input('\n\t **Exiting, Save data? y/anykey**').lower() == "y":
			save()
	else:
		print('Chose carefully\n\n')
		menu1()

def data_saver(path,dit,field):
	import csv
	field_list = ["S.No."] + field
	field_data = list()
	for i in dit:
		v = [i]+ dit[i]
		field_data += [v]
	with open(path,"w",newline="") as f:
		csv_w = csv.writer(f,delimiter=",")
		csv_w.writerow(field_list)
		for i in field_data:
			csv_w.writerow(i)

def data_reader(path,dit,field):
	import csv
	with open(path,"r") as f:
		csv_r = csv.reader(f)
		for i in csv_r:
			if i[1:] != field:
				dit[i[0]] = i[1:]
def save():
	data_saver(path_name[0],cus,fields[1])
	data_saver(path_name[1],emp,fields[2])
	data_saver(path_name[2],pro,fields[3])
	data_saver(path_name[3],bil,fields[4])
def read():
	data_reader(path_name[0],cus,fields[1])
	data_reader(path_name[1],emp,fields[2])
	data_reader(path_name[2],pro,fields[3])
	data_reader(path_name[3],bil,fields[4])

def main():

	if input("Read data from existing files.  y/anykey").lower() == "y":
		try:
			read()
		except Exception as e:
			print(e)
	print('\n\t ***IceCreame***\n\n')
	menu1()

if __name__ == '__main__':
    cus,emp,pro,bil = dict(),dict(),dict(),dict()

    fields = {
        1:["Name","Item","Price","Date of purchase"],
        2:["Name","Salary","Date of Joining"],
        3:["Item Name","Quantity","Price","Batch No."],
        4:["Item name","Price","Amount"]
    }
    path_name = ["customer.csv","employee.csv","product.csv","bill.csv"]

    main()
