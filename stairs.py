all_solutions = []

def find_stairs_recursive(target, ind, single_solution = None):
  if single_solution == None:
    single_solution = ""

  if target == 0:
    all_solutions.append(single_solution)
    return
  
  if target >= ind:
    for i in range(ind, target+1):
      find_stairs_recursive(target-i, i+1, single_solution + " " + str(i))
  else:
    single_solution = ""
    return

def find_stairs(target):
  find_stairs_recursive(target, 1)


num = int(input("Give me a positive integer: "))
type = input("Enter 0 to see the number of solutions, 1 to list of all solutions: ")

find_stairs(num)

if type == '0':
	print(len(all_solutions))
elif type == '1':
	for i in range(len(all_solutions)):
		print(str(i+1) + ". " + all_solutions[i])
