

def myfunc():
    num_var = 1
    bool_var = True
    string_var = 'string'

    print(num_var, bool_var, string_var)
    print(f"num_var is {num_var}, bool_var is: {bool_var}")

    if num_var > 1:
        print("yep its greater than 1")
    elif bool_var:
        print("yep its true")
    else:
        print("nope")

    tuple = (3,4,2,3,4)
    myList = list(tuple)
    myList.append(88)
    print(myList)
    print(myList[1:3])

    mylist = [[34, 34, 22], [66,55]]
    print(mylist[0][1])

    my_dict = {}
    my_dict = {'key': 'value',
            "key2": 'value2'}

    print(my_dict['key2'])

    for key in my_dict:
        print(f'key is {key}')


if __name__ == '__main__':
    myfunc()

