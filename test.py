def get_data():
  file = open('input_data.txt', 'r')
  lines = []
  for line in file:
    lines.append(line.rstrip())
  return lines

def line_to_lines(bash):
      res = bash.split('\n')
      res.pop(0)
      res.pop(-1)
      return res

def structure_sum(line_list):
      directory = None
      directories = {}
      for i in line_list:
            if i.split(' ')[0] == "$":
                  if i.split(' ')[1] == "ls":
                        continue
                  elif i.split(' ')[1] == "cd":
                        if i.split(' ')[2] == "..":
                              directory = directory[:-1]
                        elif i.split(' ')[2] == "/":
                              directory = ["/"]
                        else:
                              directory.append(i.split(' ')[2])
            else:
                  if i.split(' ')[0] != "dir":
                        directory_now = ""
                        for j in directory:
                              if j != "/" and directory_now != "/":
                                    directory_now += "/"
                              directory_now += j
                              directories[directory_now] = directories.get(directory_now, 0) + int(i.split(' ')[0])
      result = 0
      for i in directories.items():
            if i[1] < 100000:
                  result += i[1]
      return result

res = get_data()
res = structure_sum(res)
print(res)

