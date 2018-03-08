from flask import *
from xlrd import open_workbook
from xlutils.copy import copy
import re
from wtforms import *
from flask_wtf import CSRFProtect,FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abgiueb2389406@#%^%DFWE'
CSRFProtect(app)
fp = open('question.txt','r',encoding='utf-8')


class MyForm(FlaskForm):
    name = StringField('姓名：',[validators.Length(min=2,max=4,message='我想你的名字应该在2个字到4个字之间')])
    number = IntegerField('QQ号：',[validators.DataRequired(message='请填写你的QQ号(全数字)')])
    language = StringField('想学习使用的编程语言：')
    submit = SubmitField('提交')


@app.route('/',methods=['GET'])
def welcome():
	return render_template('welcome.html')


@app.route('/',methods=['POST'])
def welcome_button():
	return redirect(url_for('question'))


@app.route('/question/',methods=['GET'])
def question():
	fp.seek(0,0)
	question=fp.readline()
	choiceA=fp.readline()
	choiceB=fp.readline()
	choiceC=fp.readline()
	choiceD=fp.readline()
	choiceE=fp.readline()
	choiceF=fp.readline()
	filep=fp.tell()
	return render_template('question.html',question=question,choiceA=choiceA,choiceB=choiceB,choiceC=choiceC,choiceD=choiceD,choiceE=choiceE,choiceF=choiceF,filep=filep,choices='')


@app.route('/question/',methods=['POST'])
def question_button():
	choice=request.values.get('choice')
	choice=choice[0]
	filep=request.values.get('filep')
	choices=request.values.get('choices')+choice
	fp.seek(int(filep),0)
	question=fp.readline()
	if question=='END':
		oldbook=open_workbook('answer.xls')
		oldsheet=oldbook.sheet_by_index(0)
		i=int(oldsheet.cell(0,0).value)
		newbook=copy(oldbook)
		sheet1=newbook.get_sheet(0)
		sheet1.write(i,0,i)
		j=1
		for x in choices:
			sheet1.write(i,j,x)
			j=j+1
		i=i+1
		sheet1.write(0,0,i)
		newbook.save('answer.xls')
		print('No.',i-1,'has posted successfully')
		return redirect(url_for('thank'))
	choiceA=fp.readline()
	choiceB=fp.readline()
	choiceC=fp.readline()
	choiceD=fp.readline()
	choiceE=fp.readline()
	choiceF=fp.readline()
	filep=fp.tell()
	return render_template('question.html',question=question,choiceA=choiceA,choiceB=choiceB,choiceC=choiceC,choiceD=choiceD,choiceE=choiceE,choiceF=choiceF,filep=filep,choices=choices)


@app.route('/thank/',methods=['GET','POST'])
def thank():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        number = form.number.data
        language = form.language.data
        oldbook = open_workbook('number.xls')
        oldsheet = oldbook.sheet_by_index(0)
        i = int(oldsheet.cell(0, 0).value)
        newbook = copy(oldbook)
        sheet1 = newbook.get_sheet(0)
        sheet1.write(i, 0, name)
        sheet1.write(i, 1, number)
        sheet1.write(i, 2, language)
        i = i + 1
        sheet1.write(0, 0, i)
        newbook.save('number.xls')
        print('No.', i - 2, 'has uploaded his number')
        return render_template('success.html')
    return render_template('thank.html',form=form)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=14250,threaded = True)