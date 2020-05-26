#!/usr/bin/python3

import sys
import getopt
import os

from shutil import copyfile

def main(argv):
    #default directory for notes
    directory = os.path.expanduser('~') + "/Documents/studyus-notes/"
    cls = ''
    fileName = ''

    #process args
    try:
        opts, args = getopt.getopt(argv, "", "")
    except getopt.GetoptError:
        print("lol u stupid")
        sys.exit(2)

    location = directory + args[0] + "/" + args[1]
    if not os.path.exists(directory + args[0]):
        os.mkdir(directory + args[0])
    else:
        print("Directory '" + args[0] + "' already exists")

    if not os.path.exists(location):
        os.mkdir(location);
    else:
        print("Directory '" + args[1] + "' already exists")

    print("Title of Lecture: ")
    title = input()

    texFileLocation = location + "/" + args[1] + ".tex"

    f = open(texFileLocation, "w")
    f.write("\input{preamble}\n")
    f.write("\\title{" + title + "}")
    f.write("\\begin{document}\n")
    f.write("\\maketitle\n\n")
    f.write("\\end{document}\n")
    f.close()
    copyfile("./preamble.tex", location + "/preamble.tex")

    os.chdir(location);
    os.system('pdflatex -output-directory '+ location + ' ' + texFileLocation)
    os.system('evince ' + location + "/" + args[1] + ".pdf" + '&')
    os.system('vim ' + texFileLocation)

if __name__ == "__main__":
    main(sys.argv[1:])

