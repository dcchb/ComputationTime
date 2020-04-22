#Generate a windows exe file for Computation Time Reporter 
#(requires "Computation_time_reporter.py")
#
#After running the exe file should be located in "./Computation_time_reporter/Computation_time_reporter.exe"
#
#Created by David Harris-Birtill on 22/04/2020
"""
Note to generate the windows executable
Following instructions from helpful video: https://www.youtube.com/watch?time_continue=27&v=lOIJIk_maO4&feature=emb_logo, accessed 21/04/2020.

Used the command (in cmd):

pyinstaller -w -F -i "PythonIcon.ico" Computation_time_reporter.py

pyinstaller -w -F -i "<location of icon file with name of icon file>" <script name>
where:
-w stops the command window appearing
-F compiles all generated files into one executable file (rather than a whole directory of files)
-i means that the executable can have an icon (the icon must be a .ico file)


Before this is run pyinstaller needs to be installed use command (in cmd): pip install pyinstaller
"""

import os #needed to check status of files and remove directories
from PIL import Image # needed to convert png to ico
import shutil #needed to move files around

#The timer image used as an icon is from: https://pixabay.com/illustrations/just-in-time-jit-clock-icon-3750378/
#which is under a free pixabay license
#if you run the code you need to download this file and either change the filename below (or change the name of the file to icon.png)

#check png or ico file exists (if png file exists then create ico)
#if no icon exists at all then it will create the exe without an icon.

#convert png file to ico (icon) file
if os.path.isfile('icon.png'):
  filename = r'icon.png'
  img = Image.open(filename)
  img.save('ComputationTimeIcon.ico')

if os.path.isfile('ComputationTimeIcon.ico'):
  pyinstall_command = 'pyinstaller -w -F -i "ComputationTimeIcon.ico" Computation_time_reporter.py'
  icon_exists=1;
else:
  pyinstall_command = 'pyinstaller -w -F Computation_time_reporter.py'
  icon_exists=0;


#Generate the exe:
os.system(pyinstall_command);

#Delete the unneccesary files (which pyinstaller created):
#deleting directories and files code adapted from https://linuxize.com/post/python-delete-files-and-directories/#deleting-directories-folders accessed 22/04/2020
def delete_dir_and_its_contents(dir_path):
  try:
      shutil.rmtree(dir_path)
  except OSError as e:
      print("Error: %s : %s" % (dir_path, e.strerror))

def delete_file(file_path):
  try:
      os.remove(file_path)
  except OSError as e:
      print("Error: %s : %s" % (file_path, e.strerror)) 

#create directory code adapted from: https://stackabuse.com/creating-and-deleting-directories-with-python/ accessed 22/04/2020
def create_directory(dir_to_create_path):
  try:
      os.mkdir(dir_to_create_path)
  except OSError:
      print ("Creation of the directory %s failed" % dir_to_create_path)
  else:
      print ("Successfully created the directory %s " % dir_to_create_path)
      
#to delete:
#file: "Computation_time_reporter.spec"
delete_file('./Computation_time_reporter.spec');
#directory: "__pycache__"
delete_dir_and_its_contents('./__pycache__');
#directory:  "build"
delete_dir_and_its_contents('./build');

#move file "Computation_time_reporter.exe" from directory "dist" to current directory and then delete the "dist directory"
shutil.move('./dist/Computation_time_reporter.exe', './Computation_time_reporter.exe')

#if the icon file exists then delete it
if icon_exists == 1:
  delete_file("./ComputationTimeIcon.ico")
#delete: ComputationTimeIcon.ico

#delete directory "dist" (first check that the file we want exists)
if os.path.isfile('./Computation_time_reporter.exe'):
    delete_dir_and_its_contents('./dist');
else:
    print("Directory 'Dist' not deleted as the Computation_time_reporter.exe does not exist in the new directory");

