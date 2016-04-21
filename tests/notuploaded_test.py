import glob
import os

photopath = "../samplepics/backupcheck/"

missedfile_appendix = "-FILENOTUPLOADED"

make_tests = 1 # toggle if you want to make the test files first


def upload_single_missingfile():
    checkstr = photopath + "*" + missedfile_appendix + "*"
    #print "Checking with string :" + checkstr
    filesnotuploaded = glob.glob(photopath + "*" + missedfile_appendix + "*")
    print "found following files : "
    print filesnotuploaded
    if len(filesnotuploaded) > 0:
        target_name = os.path.basename(filesnotuploaded[0])
        print "current file :" + target_name
        name_split = str.split(target_name, missedfile_appendix)
        filetoupload = name_split[0]
        if os.path.exists(photopath + filetoupload + ".gif"):
            print "uploading with file " + filetoupload
            print "backing up too"
            print "now i can delete it too"
            os.remove(photopath + target_name)
        else:
            print "couldnt find gif deleting backupflag"
            os.remove(photopath + target_name)
    else:
        print "no missing uploads found"

# make file notuploaded
if make_tests:
    for fname in ["test", "hedgehog", "hedgehog2", "not_exist"]:
        file = open(photopath + fname + missedfile_appendix, 'w')  # Trying to create a new file or open one
        file.close()


upload_single_missingfile()
