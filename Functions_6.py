def subject(name, sub):
    print(name, " likes to read:")
    for i in range(0, len(sub)):
        print(sub[i])


name = input("Enter name:")
n = int(input("Enter the no. of subjects u like:"))
sub = []
for i in range(0, n):
    sub_name = input("Enter subject:")
    sub.append(sub_name)

subject(name, sub)