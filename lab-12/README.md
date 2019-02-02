Short Description of all the files in Lab 12. 


decorator_1.py – 
In decorator_1.py there are three functions defined which explain the order of operations in a sense, because there are print statements before and after a function is called. 

random_headline.py – 
This displays a random news article each time one runs the file, with the use of randint. 

decorator_timer.py – 
In decorator_timer.py, there are two functions defined. The function wrapper returns the time it took to run the function, while the function ‘my_function’ prints the sum of all numbers. 

random_letters.py - 
In the random_letters.py we see two functions defined both containing @app.route which redirects the user to a different webpage by changing the url input. After running the python file and going to the URL http://www.doc.gold.ac.uk/usr/289/ The user is greeted with a Hello, World! Which is what the first function returns. And after running the  http://www.doc.gold.ac.uk/usr/289/word with word at the end it returns 31 random characters, which is what the second function does.

headline.py – 
In headline.py one news article is displayed to the user when the python file is run, which is the one in the first index. 

show_time.py - 
After running the python file show_time.py, Hello World is printed to the user and after putting “time” in the URL like this http://doc.gold.ac.uk/usr/289/time the current date and time is displayed to the user. 

headlines_if.py  
After running the “headlines_if” python file we can see that it allows a user to find articles with words they pass in the URL. And all the articles that are displayed all contain the word the user entered.  

show_time_with_filter.py –
After running this file I see that Hello World is printed and if you add time at the end of the URL the date and time is displayed in large. This happens with the use of html as show_time_with_filter.html extends base.html which uses bootstrap. 

headlines.py –
This displays all the BBC articles by looping over them using jinja in the headlines.html file in templates. There 
hello_world.py  - 
All this file does is displays Hello World! to the user.


url_for.py –
After running url_for.py this displays “This route is a root” to the user but after adding login to the end of the url this redirects the user to doc.gold university website. 

hello_world_with_templates.py – 
This webpage displays hello world to the user in bold and centered. It does this in the hello_world.html file by extending base.html which uses bootstrap. 

url_for_using_vs_url_for.py – 
After running url_for_using_vs_url_for.py it first displays to the user “this route is a root” similar to url_for but the difference with this is it doesn’t not redirect the user to the goldsmith’s website like the url_for.py when entering login in the URL.

home.html – 
This Html file extends base.html which uses bootstrap. It has three div statements wrapped in a block with a header “greeting”

username.py – 
This file contains to app.route’s and what the second app.route does is whatever the user enters in the URL will be displayed after “hello,”

if_name_test.py - 
After trying to run this file I have realized there is a syntax error therefore not being able to run the file. 

vs_url_for.py - 
This file imports url_for from flask and has one function defined. After trying to run this file I found it to be not executable. 

macros.py – 
This file has three functions defined which all have app.route’s which display whatever the user enters in the URL e.g. home, about and contact. They’re all displayed in a block as it is rendering a template macros_page.html which extends base.html which uses bootstrap to wrap whatever’s displayed in the header.
                      
whats_my_name.py – 
After trying to run this while we see that its not possible to run this file as all it prints is “whats_my_name = {}'.format(__name__)” which is invalid syntax.

templates
base.html is used in most of the python files as files such as macros, home, hello_world_with_template etc. extend it. 
headlines_if.html – store the html which is displayed in headlines_if.py 

headlines.html – stores the html which is used in headlines.py

show_time_with_filter.html – stores the html which is used in show_time_with_filter.py

