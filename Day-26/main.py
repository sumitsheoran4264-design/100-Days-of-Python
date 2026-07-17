with open("Day-26/file1.txt") as file1:
    file_one = file1.readlines()
    striped_file1 = [int(num.strip()) for num in file_one]
with open("Day-26/file2.txt") as file2:
    file_two = file2.readlines()
    striped_file2 = [int(num.strip()) for num in file_two]



result = [n for n in striped_file1  if n in striped_file2]

print(result)