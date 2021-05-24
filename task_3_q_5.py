def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)


the_list = [2, 3, 4, 5, 6, ]
other_list = [2, 4, 5, 6, 7, ]

is_consecutive(the_list)
is_consecutive(other_list)