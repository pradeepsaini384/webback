from flask import Flask,render_template ,Response,redirect,request,flash,url_for
from sqlcon import authentication,registration,blog_data , blog_detail,email_auth

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#for home page
@app.route('/')
def home():
    popular,latest,feature = blog_data()
    print(popular,latest,feature)
    return render_template('index.html',popular=popular,latest=latest,feature=feature)


#for education blog page
@app.route('/eduBlog')
def eduBlog():
    return render_template('eduBlog.html')


#for businessBlog page
@app.route('/businessBlog')
def businessBlog():
    return render_template('businessBlog.html')


#for entertainmentBlog page
@app.route('/entertainmentBlog')
def entertainmentBlog():
    return render_template('entertainmentBlog.html')


#for about page
@app.route('/about')
def about():
    return render_template('about.html')


#for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


#for blogDetails page
@app.route('/blogDetails/<id>')
def blogDetails(id):
    blog_details = blog_detail(id)
    print(blog_details)
    return render_template('blogDetails.html',blog_details=blog_details)


#for login page
@app.route('/login')
def login():
    return render_template('login.html')

#for userdashboard 
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

#for email subscribe
@app.route('/email',methods = ['GET','POST'])
def email():
    email = request.form.get('email')
    e = email_auth(email)
   
    if e==0:
        flash("Email Insert successfully!")
        return render_template('index.html')
    else:
        flash('Email Aready Added Or Something Went Wrong!')
        return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)