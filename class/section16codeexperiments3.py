import shutil
# shell utilities
# can copy files, create zip files, extract from zip files.

# expects output of archive user wants to create a zip file consisting of files in the "file" directory/folder
# three parameters: 1) file name 2)format type "zip", 3) declare directory where files are located
shutil.make_archive("output", "zip", "")
