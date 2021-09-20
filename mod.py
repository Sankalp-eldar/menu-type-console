"""Methods here: add(a,name), show(a,name), search(a,name), delete(a,name), update(a,name)
here 'a' is list of fields (To be used as titles),
	'name' is dictionary type object/variable"""

def add(a,name,id="S.No."):
	sno = input(f'{id}\t')
	if name.get(sno) != None:
		print(f"  Warning! Data with ID {sno} exists.\n  Entering new data will change existing data.\n")
		ch = input("\t Enter '1' to *stop* entering data:  ")
		if ch == '1':
			return None
	name[sno] = list()
	for i in range(len(a)):
		field = input(f'{a[i]}:\t')		#  change, from list of fields. Done.
		name[sno] += [field]
	print()
	ch = input('\tEnter 1 to enter data again:')
	if ch == '1':return add(a,name)
def show(a,name,id="S.No."):
	print(f'{id}', end='|\t')
	for i in a:print(i, end='|\t')    # 'a' is here, list of fields!
	key = name.keys()
	print()
	for i in key:
		print(i, end ='|\t')
		val = name[i]
		for k in val:
			print(k,end='|\t')
		print()
	print()
def search(a,name,id="Serial Number"):
	se = input(f'{id} to be serched:\t')
	try:
		print(f'{id}', end='\t')
		for i in a:print(i, end='\t')	# 'a' here too
		print()
		print(se, end='\t')
		val = name[se]
		for k in val:
			print(k, end ='\t')
		print('\n')
	except: print(f'\t{id} not found!\n')
	ch = input('\tEnter 1 to search again:')
	if ch =='1':return search(a,name)
def delete(a,name,id="S.No."):
	se = input(f'{id} to be removed:\t')
	try:del name[se]
	except:print(f'{id} not found!')
	check = input('Enter 1 to perform a search:\nEnter 2 to delete another:')
	if check == "1":return search(a,name)
	elif check =="2":return delete(a,name)
	else: print()
def update(a,name,id="S.No."):
	se = input(f'{id} to be Updated:\t')
	print("Update ",se,"to:")
	new = []
	for i in range(len(a)):
		field = input(f'{a[i]}:\t')		#  change, from list of fields. Done.
		new += [field]
	if input(f"\nChange values for {se}\n From: {name.get(se)}\nTo: {new}?\n (y/anykey)\t").lower() == "y":
		name[se] = new