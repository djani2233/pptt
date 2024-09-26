# file = open("python.txt", "r")
# while True:
# 	content=file.readline()
# 	if not content:
# 		break
# 	print(content)
# file.close()

# file = open("large_file.csv", "r")
# content=file.readlines()
# print(content)
# file.close()

# file = open("test.txt", "w")
# sample_list = ["one", "two", "three"]
# for item in sample_list:
#     file.write(item)
#     file.write('\n')
# file.close()

# file = open("test.txt", "w")
# sample_list = ["one", "two", "three"]
# file.writelines(sample_list)
# file.close()
output_list = []
file = open("people.csv", mode = "r",encoding = "utf-8")
while True:
	line = file.readline()
	if not line:
		break
	token_list = line.split(',')
	name = token_list[0]
	family_name = token_list[1]
	age = int(token_list[2])
	city = token_list[3]
	if age > 38 or city.lower() == 'железаре':
		continue
	if  not family_name == 'Писаров':
		age = age + 1
		output_list.append(line)
	if not name == 'Август' and family_name == 'Попов':
		token_list[2] = str(35)
		output_list.append(','.join(token_list))

file.close()


file = open("people_ouput.csv", "w", encoding='utf-8')
file.writelines(output_list)
file.close()
