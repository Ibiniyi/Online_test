from app import app,db
from json import dumps
from app.models import Student, Question
from flask import render_template, request,flash,redirect,session,jsonify
@app.route('/')
def index():
    return render_template('index.html')

@app.post('/exam')
def exam():
    student = Student.query.filter_by(matric_no=request.form['matric_no']).first()
    if not student:
        flash('Invalid Matric Number')
        return redirect('/')
    firstname,lastname,matric_no = student.firstname,student.lastname,student.matric_no
    if bool(student.written):
        flash('Already Taken Exam!')
        return redirect('/')
    questions = Question.query.all()
    session['student'] = student.to_dict()
    return render_template("exam.html",questions=questions,matric_no=matric_no,firstname=firstname,lastname=lastname)


@app.post('/submit')
def submit():
    student = Student.query.filter_by(matric_no=session.pop('student')['matric_no']).first()
    student.written = True
    score = 0
    for i,j in enumerate(request.form):
        if request.form[j] == Question.query.get(i+1).answer:
            score += 1
    student.score = score
    db.session.add(student)
    db.session.commit()
    return f"Exam submitted successfully"