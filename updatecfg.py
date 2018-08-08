# Ahmad Hamdy
# There was a critical bug in this file
# When defining arguments I put nargs = '+' in the afile argument
# Although afile was defined as str, it could now accept multiple strings, which made it an array of strings
# This gave a critical error that was very difficult to identify
import argparse
import os


# Collecting command line arguments
parser = argparse.ArgumentParser('updatecfg')
parser.add_argument('-d', '--dir', required = True, type = str, nargs = '+', metavar = '', help = 'Directories to search')
<<<<<<< HEAD
parser.add_argument('-a', '--authfile', required = False, type = str, metavar = '', help = 'authfile')


args = parser.parse_args()

def updatefile():
    # Parse dirrectories and do some validation
    for dirz in args.dir:
        if not os.path.isdir(dirz):
            print('\n' + dirz + ' is not a directory, please check\n')
            exit(1)
        # Identify openvpn configuration files and open them read-only  
        for (curdir, subdirs, filenames) in os.walk(dirz) :
            for file in filenames:
                if os.path.splitext(file)[1] == ".ovpn":
                    filepath = os.path.join(curdir,file)
                    with open (filepath,'r') as infile:
                        # Creating temp files with .txt extensions
                        tempname = (filepath + '.txt')
                        # Open tmp files for writing and modify the auth-user-pass line
                        with open(tempname,'w') as outfile :
                            for line in infile.readlines():
                                if 'auth-user-pass'.lower() in line.lower():

                                    line = 'auth-user-pass ' + args.authfile + '\n'

                                    # openvpn requires double backslash in file paths
                                    line = line.replace("\\","\\\\")
                                    type(line)

                                outfile.write(line)
                    # Do final cleanup, remove original file and rename tmp file to be same as original
                    os.remove(filepath)
                    os.rename(tempname,filepath)
                    
                    
                
                else:
                    continue    
                

def main():               
    updatefile()
    

if __name__ == '__main__':  main()
