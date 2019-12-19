# Problem Statement - Parse all MD files from a GitHub repository and render the result in HTML format in a web server

## Instructions
* Fork this repository
* Write a web server of your choice (Flask, for example) which will recursively parse all MD files from the forked repository
* The index page of your server needs to list all file paths as hyperlinks
* Clicking on any of them, server routes to a different page where the parsed MD file is displayed in HTML format

### Example
We have the directory structure as
* Introduction/Chapter-One.md
* Introduction/Chapter-Two.md
* Setup/Installation/Chapter-One.md
* Setup/Configuration/Chapter-One.md
* images/  
* README.md
  
Let's assume your server runs on port 5000.  
The index page of your server needs to be accessible in your web browser as mentioned below -  

http://localhost:5000/
* [Introduction/Chapter-One]()
* [Introduction/Chapter-Two]()
* [Setup/Installation/Chapter-One]()
* [Setup/Configuration/Chapter-One]()  

Note: The hyperlinks used here are for demo purpose only; they are not functional. Also, omit README.md file. images directory needs to be omitted as well since they do not contain any MD files
  
Let's say we click on [Introduction/Chapter-One]()  
Server needs to route to http://localhost:5000/Introduction/Chapter-One, where the result on your webpage is HTML equivalent of the parsed MD file

This is the MD file  
![](images/md.png?raw=true)  
  
This is parsed HTML, which needs to be shown in web browser  
![](images/html.png?raw=true)  
