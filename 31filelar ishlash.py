
# file = open('matn.txt')
# file.close()
# print(file.read())
# print(file)
# print(type(file))



# with open('matn.txt') as file :
#     name = file.read()
# print(name)
# print(file)


# with open('matn.txt') as file :
#     info = file.read()
# print(info)
#
# info = info.rstrip()
# info = info.replace('\n', '')
# print(info)
# print(type(info))


# file_name = 'data/matn.txt'
# with open(file_name) as file :
#     matn = file.read()
# print(matn)


# file_name = 'data/matn.txt'
# with open(file_name) as file :
#     for line in file :
#         print(line)
# print(file)


# file_name = 'data/students'
# with open(file_name) as students :
#     for student in students :
#         print(student)



# file_name = 'data/students'
# with open(file_name) as students :
#     line = students.readlines()
#
# students = [student.strip() for student in line]
# print(students)
# print(line)



# new_file = 'data/new_file'
# firstname = 'Abdulloh'
# lastname = 'Hamidov'
# age = 24
# with open(new_file, 'w') as file :
#     file.write(firstname + '\n')
#     file.write(lastname + '\n')
#     file.write(str(age) + '\n')
#
# with open(new_file) as file :
#     print(file.read())



# file_name = 'data/new_file'
# with open(file_name, 'a') as file :
#     file.write('Akmal' + '\n')
#     file.write('Sobirov' + '\n')
#     file.write('21' + '\n')
#
# with open(file_name) as result :
#     print(result.read())



import pickle

# student1 = {'firstname': 'Abdulloh', 'lastname' : 'Komilov', 'age' : 23, 'course' : 3}
# student2 = {'firstname': 'Anvar', 'lastname' : 'Sobirov', 'age' : 25, 'course' : 4}
#
#
# pickle_file = 'data/info'
# with open(pickle_file, 'wb') as file :
#     pickle.dump(student1, file)
#     pickle.dump(student2, file)
# print(file)

#
# pickle_file = 'data/info'
#
# with open(pickle_file, 'rb') as file :
#     student1 = pickle.load(file)
#     student2 = pickle.load(file)
#     print(student1)


person1 = {'firstname' : 'alisher', 'lastname': 'davlatov', 'age': 24}
person2 = {'firstname' : 'sardor', 'lastname': 'akmalov', 'age': 24}
person3 = {'firstname' : 'komil', 'lastname': 'sobirov', 'age': 24}

new_pickle = 'data/new_pickle'

with open(new_pickle, 'wb') as new_file :
    pickle.dump(person1, new_file)
    pickle.dump(person2, new_file)
    pickle.dump(person3, new_file)


with open('data/new_pickle', 'rb') as file :
    person1 = pickle.load(file)
    person2 = pickle.load(file)
    person3 = pickle.load(file)
print(person1)
print(person2)
print(person3)































