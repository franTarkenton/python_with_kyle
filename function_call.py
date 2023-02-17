from start_python import myfunc
import datetime
import os


def myfunc2(first_arg, second_arg=2):
    print("this si my function")
    print(f"args are: {first_arg}, second arg {second_arg}")
    mystring = f"{first_arg}-{second_arg}"
    return mystring


def demo_date():
    # https://strftime.org/
    # pendulum module... makes working with datetime easier
    # https://pleac.sourceforge.net/pleac_python/datesandtimes.html
    now = datetime.datetime.now()
    strNow = now.strftime('%Y%m%d')

    print(strNow)
    return strNow

def get_file():
    print(__file__)
    just_dir = os.path.dirname(__file__)


def readFile():
    fh = open('path to file', 'r')
    for line in fh:
        print(line)
    fh.close()

    fh = open('path to file', 'w')
    fh.write('string\n')
    fh.close()

    with open('pathto file', 'r') as fh:
        for i in fh:
            print(i)
        

if __name__ == '__main__':

    myfunc()
    newvar = myfunc2(first_arg=10, second_arg=22)
    print(newvar)
    get_file()
    demo_date()


