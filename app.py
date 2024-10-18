from flask import Flask, render_template,request
import pymysql as sql

app = Flask(__name__)

my_connection = sql.connect(
    host='localhost',
    user='root',
    password='8267',
    database='final2'
)
my_cursor = my_connection.cursor()

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/admission',methods=['GET'])
def admission():
    return render_template('admission.html')


@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register-form',methods=['POST'])
def register_form():
    _id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    percentage = request.form['percentage']
    rank = request.form['rank']
    course = request.form['course']
    address = request.form['address']

    query = '''
        insert into student(id,`name`,email,phone,percentage,`rank`,course,address)
        values(%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    values = (_id,name,email,phone,percentage,rank,course,address)
    my_cursor.execute(query,values)
    my_connection.commit()
    return 'register data recieved'

@app.route('/view',methods=['GET'])
def view():
    query='''
        select * from student;
    '''
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    return render_template('view.html',details=data)

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html')

@app.route('/update-form',methods=['POST'])
def update_form():
    _id = request.form['id']
    field = request.form['field']
    new_value = request.form['new_value']

    query = f'''
        update student
        set {field} = '{new_value}'
        where id={_id};
    '''
    my_cursor.execute(query)
    my_connection.commit
    return 'updated'



@app.route('/delete',methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route('/delete-form',methods=['POST'])
def delete_form():
    _id = request.form['id']
    query = f'''
        delete from student
        where id = {_id};
    '''
    my_cursor.execute(query)
    my_connection.commit()
    return f'user {_id} has been deleted'

@app.route('/query-submit',methods=['POST'])
def query_submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    
    query = '''
        insert into query(`name`,email,phone,course)
        values(%s,%s,%s,%s);
    '''
    values = (name,email,phone,course)
    my_cursor.execute(query,values)
    my_connection.commit()
    return 'We will reach out to you soon'

#nikhil made a change
#nikhil added another
app.run()