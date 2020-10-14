#!/usr/bin/python3

import sys
import getopt
import os

from shutil import copyfile

def main(argv):
    #default directory for notes
    directory = os.environ.get('STUDYUS') or os.path.expanduser('~') + "/studyus-notes"
    viewer = os.environ.get('STUDYUS_VIEWER') or "sumatraPDF"
    cls = ''
    fileName = ''

    directory = directory + "/"

    #process args
    try:
        opts, args = getopt.getopt(argv, "e", ['edit'])
    except getopt.GetoptError:
        print("lol u stupid")
        sys.exit(2)

    location = directory + args[0] + "/" + args[1]
    if not os.path.exists(directory + args[0]):
        print("Course '" + args[0] + "' does not exist yet. Create it? [Y/n]")
        create = input()
        if not (create == "n" or create == "N"):
            os.mkdir(directory + args[0])
        else:
            sys.exit(0)

    if not os.path.exists(location):
        print ("Lecture '" +  args[1]  + "' does not exist yet. Create it? [Y/n]")
        create = input()
        if not (create == "n" or create == "N"):
            os.mkdir(location);
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
            os.system(viewer + " " + location + "/" + args[1] + ".pdf" + '&')
            os.system('vim ' + texFileLocation)
        else:
            sys.exit(0);
    else:
        texFileLocation = location + "/" + args[1] + ".tex"
        os.chdir(location);
        os.system(viewer + " " + location + "/" + args[1] + ".pdf" + '&')
        if opts and opts[0] != "-e" and opts[0] != "--edit":
            os.system('vim ' + texFileLocation)

if __name__ == "__main__":
    main(sys.argv[1:])

