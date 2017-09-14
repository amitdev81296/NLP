title = 'Days of the Week\n'
read_file_path = 'resources/days.txt'
read_days = open(read_file_path, 'r')
days = read_days.read()

write_file_path = 'resources/new_days.txt'
write_days = open(write_file_path, 'w')

write_days.write(title+days)

read_days.close()
write_days.close()
