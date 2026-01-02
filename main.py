from link import *
def work():
    print("""
    1 - see
    2 - change
    3 - add
    4 - delete""")
    choose = int(input("Choose option: "))
    if choose == 1:
        to_see()
    elif choose == 2:
        select = int(input("Select option: "))
        if select == 1:
            pass
        id = input("Enter the id: ")
        name = input("Enter the name: ")
        to_change(name,id)
work()