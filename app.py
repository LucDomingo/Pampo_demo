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
    active="nav-link active"
    nactive="nav-link"
    ncontent="tab-pane fade"
    content="tab-pane fade show active"
    state1=active
    state2=nactive
    content1=content
    content2=ncontent
    if request.method == "GET":
     return render_template('EntityExtractor.html',state1=state1,state2=state2,content1=content1,content2=content2)
    else:
     post1=0
     select1=""
     original1 = request.form.get('comp_select')
     original2 = request.form.get('area_text')
     if original1 != "Choose a text":
      select1 = pampo.extract_entities(original1)
      state1=active
      state2=nactive
      content1=content
      content2=ncontent
      post1=1
      original2 = "Write your text here"
     if original2 != "Write your text here":
      state1=nactive
      state2=active
      content1=ncontent
      content2=content
      select2 = pampo.extract_entities(original2)
     else:
      select2 ="No text given"
     post_done = 1
     return render_template('EntityExtractor.html',post1=post1,post_done=post_done,select1=select1,select2=select2,original2=original2,original1=original1,state1=state1,state2=state2,content1=content1,content2=content2)



if __name__ == '__main__':
    app.run()
