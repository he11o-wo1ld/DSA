# input = "profile 1 - { id: 1, email: 'knowkanhai@gmail.com', first_name: ‘Kanhai’, last_name: ‘Shah’, class_year: None, date_of_birth: None}"

inp1 = "profile 1 - { id: 1, email: 'knowkanhai@gmail.com', first_name: ‘Kanhai’, last_name: ‘Shah’, class_year: None, date_of_birth: None}"
inp2 = "profile 2 - { id: 2, email: 'knowkanhai+donotcompare@gmail.com', first_name: ‘Kanhai1’, last_name: ‘Shah’, class_year: 2012, date_of_birth: ’1990-10-11’}"


def extract_profile(profile):
	inp_arr = profile.split('-')

	inp_data = inp_arr[1].split(':' and ',')
	inp_dict = {}

	# prin(inp_dict)
	return inp_dict


def check_duplicate_profile(inp):
	data = extract_profile(inp)
	print(data)
	for i in range(len(data)):
		print(data[i])


data1 = check_duplicate_profile(inp1)
# data2 = check_duplicate_profile(inp2)

print(data1)
