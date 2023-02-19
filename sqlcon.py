import mysql.connector

conn = mysql.connector.connect(host = "localhost",user= "root",password ="",database="blog")
cursor = conn.cursor()

def registration(rollno,name,email,password):
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES ('{}','{}','{}','{}')""".format(rollno,name,email,password))
    conn.commit()

def email_auth(email):
    done = 1
    cursor.execute("""SELECT * FROM `email` WHERE `email` LIKE '{}' """.format(email))
    popular = cursor.fetchall()
    if len(popular)>0:
        return done
    else:
        cursor.execute("""INSERT INTO `email` (`email`) VALUES('{}')""".format(email))
        conn.commit()
        done = 0
        return done
        
    
def authentication(email,password):
    cursor.execute("""SELECT * FROM `blog` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    return users

def blog_data():
    category = ['popular','latest','feature']
    
    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[0]))
    popular = cursor.fetchall()
    
    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[1]))
    latest = cursor.fetchall()

    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[2]))
    feature = cursor.fetchall()

    return popular,latest,feature
def blog_detail(id):
    cursor.execute("""SELECT * FROM `blog` WHERE `id` LIKE '{}'""".format(id))
    blog_details = cursor.fetchall()
    return blog_details