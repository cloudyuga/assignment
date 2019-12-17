from flask import Flask
from flask import render_template
from mistletoe import Document, HTMLRenderer
import os

path = '/Users/chaitalee/Desktop/cloudyuga_assignment/assignment/'
out_path = '/Users/chaitalee/Desktop/cloudyuga_assignment/assignment/templates/'


def convert_md_to_html():
    print("testing")
    for r, d, f in os.walk(path):
        for file in f:
            if '.md' in file:
                if 'README.md' not in file:
                    with open(os.path.join(r, file), 'r') as fin:
                        with HTMLRenderer() as renderer:
                            rendered = renderer.render(Document(fin))
                            r1 = r.replace(path,"").replace("/","")
                            file=r1+file.replace('.md','.html')
                            with open(os.path.join(out_path, file),"w") as out:
                                out.write(rendered)
                                out.close()


app = Flask(__name__)

@app.route('/IntroductionChapter-One')
def Introduction_Chapter_One():
    return render_template('IntroductionChapter-One.html')

@app.route('/IntroductionChapter-Two')
def Introduction_Chapter_Two():
    return render_template('IntroductionChapter-Two.html')

@app.route('/SetupConfigurationChapter-One')
def SetupConfigurationChapter_One():
    return render_template('SetupConfigurationChapter-One.html')

@app.route('/SetupInstallationChapter-One')
def SetupInstallationChapter_One():
    return render_template('SetupInstallationChapter-One.html')

@app.route('/')
def hello_world():
    convert_md_to_html()
    url = "http://127.0.0.1:5000/"
    str1 = ''
    url_path = ''
    for r, d, f in os.walk(path):
        for file in f:
            if '.md' in file:
                if 'README.md' not in file:
                    r1 = r.replace("/Users/chaitalee/Desktop/cloudyuga_assignment/assignment", "")\
                        .replace("/", "").replace("/", "")
                    url_path = url+r1+file.replace('.md', '')
                    file_name = r1 + file.replace('.md', '')
                    str1 += '<a href =' + str(url_path) + '>' + file_name + '</a><br>'
    return str1


if __name__ == '__main__':

    app.run(debug=True)
