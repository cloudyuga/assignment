from flask import Flask
from flask import render_template
from mistletoe import Document, HTMLRenderer
import os


os.getcwd()


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
                            r1 = r.replace(path,"")
                            file=file.replace('.md','.html')
                            if not os.path.exists(out_path+r1):
                                os.makedirs(out_path+r1)


                            print("*******************")
                            print(file)
                            print(out_path+r1)
                            with open(os.path.join(out_path+r1, file),"w") as out:
                                out.write(rendered)
                                out.close()


app = Flask(__name__)

@app.route('/Introduction/Chapter-One')
def Introduction_Chapter_One():
    return render_template('Introduction/Chapter-One.html')

@app.route('/Introduction/Chapter-Two')
def Introduction_Chapter_Two():
    return render_template('Introduction/Chapter-Two.html')

@app.route('/Setup/Configuration/Chapter-One')
def SetupConfigurationChapter_One():
    return render_template('Setup/Configuration/Chapter-One.html')

@app.route('/Setup/Installation/Chapter-One')
def SetupInstallationChapter_One():
    return render_template('Setup/Installation/Chapter-One.html')

@app.route('/')
def hello_world():
    convert_md_to_html()
    url = "http://127.0.0.1:5000"
    str1 = ''
    url_path = ''
    for r, d, f in os.walk(path):
        for file in f:
            if '.md' in file:
                if 'README.md' not in file:
                    r1 = r.replace("/Users/chaitalee/Desktop/cloudyuga_assignment/assignment", "")
                    url_path = url+r1+"/"+file.replace('.md', '')
                    file_name = r1+"/" + file.replace('.md', '')
                    str1 += '<a href =' + str(url_path) + '>' + file_name + '</a><br>'
                    print(str1)
    return str1


if __name__ == '__main__':

    app.run(debug=True)
