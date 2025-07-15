import os
import shutil
import re

def move_jpg():
    src_folder=input("Enter folder name:").strip()
    if os.path.exists(src_folder):
       src_path=os.path.abspath(src_folder)
       src_parent=os.path.dirname(src_path)
       dest_folder=input("Enter destination folder name:")
       
       if not os.path.exists(dest_folder):
         try:
            dest_path=os.path.join(src_parent,dest_folder)
            os.mkdir(dest_path)
         except Exception as e:
            print(f"Failed to create destination folder :{e}")
            return
       else:
         dest_path=os.path.abspath(dest_folder)
       
       try:
          for filename in os.listdir(src_path):
            if filename.lower().endswith(".jpg"):
               src_file=os.path.join(src_path,filename)
               dest_file=os.path.join(dest_path,filename)
               shutil.move(src_file,dest_file)
          print(f"Jpg files from {src_folder} moved to {dest_folder}")
       except Exception as e:
          print(f"Error occurred during moving files :{e}")
          return
    else:
      print("Input folder does not exist")
      return
 
def emails():
   src_file=input("Enter txt file name").strip()
   src_file+=".txt"
   if os.path.exists(src_file):
       with open(os.path.abspath(src_file),'r') as f:
          content=f.read()
       email_pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+')
       emails=email_pattern.findall(content)
       unique_emails=list(set(emails))
       with open("email.txt","w") as f:
           for email in unique_emails:
               f.write(email+"\n")
       print("E-mails saved to \"email.txt\"")
   else:
       print("Input file does not exist")


if __name__=="__main__":
  print("Functions to handle data")
  print("1.Move Jpg files")
  print("2.Extract email addresses")
  print("3.Save title of webpage")
  choice=int(input("Enter your choice(1-3)"))
  
  if choice==1:
      move_jpg()
  elif choice==2:
      emails()
  elif choice==3:
      pass
  else:
      print("Bad choice by user")