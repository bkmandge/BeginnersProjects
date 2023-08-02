"#Acronym Creator" 

text = str(input('Enter the text: ')).split()

acronym = ""

for ch in text:
    acronym = acronym + str(ch[0]).upper()
print(acronym)
