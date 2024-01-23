import pandas as pd 

data =  [["Alex", 20, "Male", 3.5],
        ["Maria", 21, "Female", 3.6],
        ["John", 22, "Male", 3.7],
        ["Sophia", 21, "Female", 3.8],
        ["Michael", 23, "Male", 3.9],
        ["Emma", 22, "Female", 4.0],
        ["Daniel", 20, "Male", 3.4],
        ["Olivia", 21, "Female", 3.3],
        ["David", 24, "Male", 3.2],
        ["Isabella", 20, "Female", 3.1]]

columns = ['name', 'age', 'gender', 'gpa']

df = pd.DataFrame(data, columns = columns)

'''
#print(f'{df}') #1 задание
print('')
print('-' * 20)

#2 задание
names = df["name"]
print(f'Имена {names}') 
print('-' * 20)

girls = df[df["gender"] == 'Female' ]
print(f'Девочки {girls}') 
print('-' * 20)

max_gpa = df['gpa'].max()
studMaxGpa = df[df['gpa'] == max_gpa]
print(studMaxGpa)
print('-' * 20)

#3 задание
agePlus = df['age'] + 1
print(agePlus)
print('-' * 20)

min_gpa = df['gpa'].min()
update_gpa = min_gpa + 1
print(update_gpa)
print('-' * 20)


#4 задание
new_student = pd.Series(['Anton',  20, "Male", 3.9], index=df.columns)
df = df._append(new_student, ignore_index = True)
print(df)


#5 задание
increase_gpa = df['gpa'] + 0.5
print(increase_gpa)


#6 задание
sort_age = df.sort_values(by='age', ascending=False)
print(sort_age)
print('-' * 20)

sort_gpa = df.sort_values(by='gpa', ascending= True)
print(sort_gpa)

#7 задание
df.to_csv('dataframe.csv', index=False)
'''