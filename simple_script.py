import sys

if __name__ == '__main__':
    rez = {}
    for x in sys.argv[1:]:
        rez[x] = rez.get(x,0)+1
    print (rez)