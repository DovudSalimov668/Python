# def reverse_string(n):
#     str(n)
#     x = []
#     x = n.split()
#     print(x)
# reverse_string("odina")
# x = ("odina")
# # list(x)


# print(type(x))
name = "odina"
def reverse_(name):
    print(name)
    if len(name) ==1:
        return name
    else:

        return name[-1]+ reverse_(name[:-1])
print(reverse_(name))