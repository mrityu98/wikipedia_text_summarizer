
from unittest import result
from flask import Flask , url_for, render_template, redirect , request
from transformers import pipeline
import wikipedia


app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def summ():
        if request.method=="POST":
              wiki_url= request.form["tex"]
              max_length= request.form["num"]
              summarizer=pipeline("summarization");
              wikiurl=wiki_url
              search_key=wiki_url.split('/')[4]
              res=wikipedia.summary(search_key)
              lenght_of_original_text=len(res.split())
              summary_text = summarizer(res, max_length, min_length=5, do_sample=False)[0]['summary_text']
              length_of_summarized_text=len(summary_text.split())
              summarized_percentage=round(((lenght_of_original_text-length_of_summarized_text)/lenght_of_original_text)*100,2)
              data = {'summarized_text':summary_text ,'len_original':lenght_of_original_text,'len_summarized':length_of_summarized_text,'per':summarized_percentage}
              return render_template('display.html',result=data)
              
        else: 
            return render_template('front.html') 

if __name__== "__main__" :
    app.run(debug=True)

