#step 2
PLACEHOLDER = "[name]"



#step 1 
with open("/Users/Sumit/OneDrive/Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("/Users/Sumit/OneDrive/Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contants = letter_file.read()
    for name in names:
        stripped_name = name.strip() #strip() method use for remove extra spaces
        new_letter = letter_contants.replace(PLACEHOLDER, stripped_name) # change Placeholder with name in letter
        print(new_letter)
        
        #step 3
        with open(f"/Users/Sumit/OneDrive/Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/output/ReadyToSend/letter_for_{stripped_name}.txt",mode= "w") as completed_letter:
            completed_letter.write(new_letter)



    

 