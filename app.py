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
     post1=0
     select1=""
     original1 = request.form.get('comp_select')
     original2 = request.form.get('area_text')
     if original1 != "Choose a text":
      select1 = pampo.extract_entities(original1)
      post1=1
     if original2 != "Write your text here":
      select2 = pampo.extract_entities(original2)
     else:
      select2 ="No text given"
     post_done = 1
     return render_template('EntityExtractor.html',post1=post1,post_done=post_done,select1=select1,select2=select2,original2=original2,original1=original1)



if __name__ == '__main__':
    app.run()
