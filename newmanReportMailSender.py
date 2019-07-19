# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported
import os
import zipfile
import datetime
#import pathlib

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders



#############################################################################
# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths


def zipDirectory():
    # Assign the name of the directory to zip
    #dir_name = 'mydir'
    dir_name = 'newman'
    current_date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print("current_date_time >>> "+current_date_time )

    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(dir_name)

    # printing the list of all files to be zipped
    print('The following list of files will be zipped:')
    for fileName in filePaths:
        print(fileName)

    # writing files to a zipfile
    zip_name = dir_name + '_'+current_date_time +'.zip'
    zip_file = zipfile.ZipFile(zip_name, 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)
    # print(zip_name + ' file is created successfully!')
    return zip_name


def removeFile(dirName):
    # setup file paths variable
    filePaths = []
    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        print(root)
        for filename in files:
            os.remove(root+'/'+filename)
            print('report file is deleted successfully!')

#########################################################################
fromaddr = "asaraporn@addtechhub.com"
toaddr = "hadsai.g@gmail.com"
#filename = "newman-run-report-2019-07-05-05-35-08-237-0.html"
Password = "Hadsai.1"
Subject = "Subject of the Mail"
body = "Body_of_the_mail"



# instance of MIMEMultipart
msg = MIMEMultipart()
# storing the senders email address 
msg['From'] = fromaddr
# storing the receivers email address 
msg['To'] = toaddr
# storing the subject 
msg['Subject'] = "Subject of the Mail"
# string to store the body of the mail
body = "Body_of_the_mail"

###########################################################################
#Zip Folder
newmanReport = zipDirectory()
############################################################################
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain'))
# open the file to be sent 
# filename = "./newman/newman-run-report-2019-07-05-05-35-08-237-0.html"
filename = newmanReport
attachment = open(filename, "rb")
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form 
p.set_payload((attachment).read())
# encode into base64 
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

##############################################################################
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security 
s.starttls()
# Authentication 
s.login(fromaddr, "Hadsai.1")
# Converts the Multipart msg into a string 
text = msg.as_string()
# sending the mail 
s.sendmail(fromaddr, toaddr, text)
# terminating the session 
s.quit()

#################################################################################
#delete newman report file
dir_name = 'newman'
removeFile(dir_name)

print("==== End =====")
################################################################################

