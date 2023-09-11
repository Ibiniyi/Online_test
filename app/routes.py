from app import app,db
from app.models import Student, Question
from flask import render_template, request,flash,redirect
@app.route('/')
def index():
    return render_template('index.html')

@app.post('/exam')
def exam():
    student = Student.query.filter_by(matric_no=request.form['matric_no']).first()
    firstname,lastname,matric_no = student.firstname,student.lastname,student.matric_no
    if not student:
        flash('Invalid Matric Number')
        return redirect('/')
    if bool(student.written):
        flash('Already Taken Exam!')
        return redirect('/')
    questions = Question.query.all()
    return render_template("exam.html",questions=questions,matric_no=matric_no,firstname=firstname,lastname=lastname)