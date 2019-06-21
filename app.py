from flask import Flask, render_template, request
import pampo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/EntityExtraction',methods = ['GET', 'POST'])
def EntityExtraction():
    if request.method == "GET":
     return render_template('EntityExtractor.html')
    else:
     select1 = pampo.extract_entities(request.form.get('comp_select'))
     if select1=="Choose a text":
         select1=Choose a text
     select2 = pampo.extract_entities(request.form.get('area_text'))
     post_done = 1
     return render_template('EntityExtractor.html',post_done=post_done,select1=select1,select2=select2)



if __name__ == '__main__':
    app.run()
