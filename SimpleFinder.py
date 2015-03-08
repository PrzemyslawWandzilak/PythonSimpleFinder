from optparse import OptionParser
import optparse
import os
import re

def debug1(options, args):
    print("sample use: " + '''python SimpleFinder.py -f klj  -d "/c/OPENSW/" args1 args2''')
    # http://stackoverflow.com/questions/6666856
    # in python 2, all of your classes should inherit from object. 
    # If you don't, you end up with "old style classes", which are 
    # always of type classobj, and whose instances are always of type instance
    print("type(options)\t\tis " + str(type(options)))                     # <type 'instance'>
    print("options.__class__\tis " + str(options.__class__))               # optparse.values
    print("type(optparse.Values)\tis " + str(type(optparse.Values)))       # <type 'classobj'>
    print("options:\t" + str(options))
    print("vars(options):\t" + str(vars(options)))
    print("args:\t\t" + str(args))
    print("")
    print("options.filename:\t" + str(options.filename  ))
    print("options.number +1:\t" + str(options.number + 1))
    #print("options['filename']\t" + str(options['filename'])) #options is not a dic type

def parseOptions():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="Find pattern in FILE", metavar="FILE")
    parser.add_option("-d", "--dir", dest="directory",
                      help="Find pattern in all files in DIR", metavar="DIR")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")
    parser.add_option("-n", "--num",
                      action="store", dest="number", type="int", default=1,
                      help="number lucky")
                      
    # Program will return after next line if run with: <yourscript> [-h|--help] 
    (options, args) = parser.parse_args()
    return (options, args)
    
def main():
    #Parse input arguments
    (options, args) = parseOptions();

    #Print debug data
    if options.verbose == True:
        debug1(options, args)
 
    pattern = re.compile(r'(.*doc)\s+.*')
    

    #Attempt1 - walk through files in folder
    #for filename in os.listdir (folder):
    
    #Attempt2 - walk through files in folder
    for root, dirs, filenames in os.walk(options.directory):
        for f in filenames:
            log = open(os.path.join(root, f),'r')
            for lines in log:
                output = pattern.findall(lines)
                if output:
                    print(os.path.join(root, f) + " : " + output[0])    



if __name__ == '__main__':
  main()

#End of script