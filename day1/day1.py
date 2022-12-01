elf_list = []
current_elf_total_calories = 0

with open('day1_input.txt') as f:
    for line in f:
    	if line.strip() == "":
    		print("Empty line")
    		print("Current elf total calories: ", current_elf_total_calories)
    		elf_list.append(current_elf_total_calories)
    		current_elf_total_calories = 0

    	elif line[-1] == "\n":
    		print(line[:-1])
    		current_elf_total_calories += int(line[:-1])
    	else:
    		print(line)
    		current_elf_total_calories += int(line)

    print(elf_list)
    print("------")
    print("Number of elfs:", len(elf_list))

    print("Elf", elf_list.index(max(elf_list)), "with highest calories:", max(elf_list))
  
