import mariadb

#mariadb connect
mydb = mariadb.connect(
    host="127.0.0.1", # localhost
    user="your_id", #your mariadb id
    password="your_pw", #your mariadn pw 

)
#Create Database
#mycursor.execute("CREATE DATABASE db_name")



#Show Databases
#create_cursor.execute("SHOW DATABASES")
#for x in create_cursor:
#   print(x)

# Crate List
# mycursor.execute("CREATE TABLE list_name(1.Index_Id VARCHAR(100), 2.Index_Id VARCHAR(250))")   


# Crate Index
# sql = "INSERT INTO list(search_engine, url) VALUES (%s, %s)"
# val = ("index1","index2")
# mycursor.execute(sql, val)
# mydb.commit()