#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as output: #letter saved as string
     prompt = (output.read())
#print(prompt)

with open("./Input/Names/invited_names.txt") as invited_names: #list of names saved as a list, removing the new line keyword
    guest_list = []#invited_names.readlines()
    for line in invited_names:
        guest_list.append(line.strip())


for i in range(len(guest_list)):
    with open(f"./Output/ReadyToSend/{guest_list[i]}.txt",mode="w+") as guests:
        #line1 = guests.readlines(1)
        #print(guest_list[i])
        guest = prompt
        guests.write(guest.replace("[name]", guest_list[i]))
