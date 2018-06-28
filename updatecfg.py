import argparse
import os
from test.test_decimal import file

# Collecting command line arguments
parser = argparse.ArgumentParser('updatecfg')
parser.add_argument('-d', '--dir', required = True, type = str, nargs = '+', metavar = '', help = 'Directories to search')
parser.add_argument('-a', '--authfile', required = False, type = str, nargs = '+', metavar = '', help = 'authfile')

args = parser.parse_args()

def updatefile():
    for dirz in args.dir:
        if not os.path.isdir(dirz):
            print('\n' + dirz + ' is not a directory, please check\n')
            exit(1)
        for (curdir, subdirs, filenames) in os.walk(dirz) :
            for file in filenames:
                if os.path.splitext(file)[1] == ".ovpn":
                    filepath = os.path.join(curdir,file)
                    with open (filepath,'r') as infile:
                        tempname = (filepath + '.txt')
                        with open(tempname,'w') as outfile :
                            for line in infile.readlines():
                                if 'auth-user-pass'.lower() in line.lower():
                                    line = 'auth-user-pass readme1.txt\n'
                                outfile.write(line)
                    os.remove(filepath)
                    os.rename(tempname,filepath)
                    
                    
                    
                else:
                    continue    
                

def main():               
    updatefile()
    

if __name__ == '__main__':  main()
