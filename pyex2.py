



import requests
import mysql.connector
from mysql.connector import Error
keyword=input('enter the keyword')#here user enter the keywoard 

   conn = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='admin',
                             password='')
   sql_Query = " ""SELECT * FROM image WHERE key LIKE '%{$%s}%'"""(%keyword)   #image is here table_name and having key as a column .I here matched the substring from the database table strings and then retuns the links for that image  

   cursor = conn.cursor(buffered=True)
   cursor.execute(sql_Query)
   record = cursor.fetchone()
   
   cursor.close()

        conn.close()
       


print('Beginning file download with requests')

url = 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-540x360/06/74/aa/fc.jpg'  #this url is the obtained from record as record stores 
r = requests.get(url)

with open('/Users/Prabhat Jha/Desktop/eifeltower.jpg', 'wb') as f: #here the download path is given where user want to donload this 
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)  
print(r.headers['content-type'])  
print(r.encoding)
#in the above function i have a database in which all urls of images are stored when user enter the keyword that keyword get matched as a substrinh of key columns in image name table after getting that substring to be matched then after that a record having the url of that link is retieved from database and get downloaded at the path where user seted its downloaded path  
