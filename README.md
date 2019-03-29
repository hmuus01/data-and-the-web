**Data and The Web - Final Submission - My APP - HAMZE MUUSE**

**URL for My APP** 
--> Will only work once you run app.py on the terminal

**Link to my web app**: http://doc.gold.ac.uk/usr/289/

**Link to all my commits** : https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/commits/master

**This is a link to watch my y website working incase you cannot run it due to access** : http://doc.gold.ac.uk/~hmuus001/dw/hmuus001myApp.mp4

Login Credentials<br/>
**username** : admin <br/>
**password** : password

Backup Credentials<br/>
**username** : hmuus001
**password** : 12345
____________________________________
**I have created my term 2 Final Flask application using the techniques I have gained over the course of the Data and the Web module, both in term 1 and term 2. With the Knowledge aquired from the lab content and the documentations, I have searched and found resources online one of which is a flask tutorial which is used to build an article flask app (see reference below). In order to extend on the online tutorial and the templates given to me, I have tried to implement the DRY (Don't Repeat Yourself) principle and separation of concern. I have done this by seperating my html files, my forms for registrations and to fill an article which will be explained more below and the logic to check if a user is logged in which will also be explained more below. Privacy is key, therefore i have ensured users of my web applications are protected against Cross Site Request Forgery.**

**Please Note** `All the lines in the tables below are links and can be clicked. Once clicked it will take you to the specific line mentioned and the file it is in.`  

**SUBMISSION:**
 
| **SUBMISSION INSTRUCTIONS** | **COMPLETE/NOT COMPLETE** |
| --- | --- |
| App run's without debug=True |[`debug=false`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L410)  ✔ |
| Your app process should run in the background: use 'python3 YOUR-APP-NAME &' | ✔ |
| The url for your app should be in a README.txt | ✔ |
| Any login credentials should be in the README | ✔ |
| You should include a clear statement in the README submitted that describes what you have done | ✔ |
| Your app should be in the top level of your repo in "my app" subdirectory | ✔ |
| All the rest of your code for the term should be in subdirectories (lab-12, lab-13, ...) | ✔ |
| You should give master access to your repo to the following gitlab accounts: @ehoma001 and TAs (I will announce their gitlab accounts later) | ✔ |
| Check this page before submission not missing any updates on this page |  ✔  |

_______


| APP CRITERIA | DESCRIPTION | FILENAME & LINES | COMPLETE/NOT COMPLETE |
| --- | --- | ---- |-|
| 1 : It is a flask iapp |I have used the flask micro framework in this web application and you can see this with the use of the flask class and the use of the instance of this class with "app = Flask(__name__)”|`app.py`,<br/> [`Line 2`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L2) <br/> [`Line 27`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L27)|✔|
| 2 : There is more than one route and more than one view |I have used multiple routes in my web application some examples include @app.route(‘/’), @app.route(‘about’), @app.route(‘find’) etc.|`app.py`, <br/> [`Line 115`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L115) <br/> [`Line 120`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L120) <br/> [`Line 145`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L145)|✔|
| 3 : The html is rendered using jinja templates|I have rendered my html pages using jinja, you can see this with the use of ‘{%block body%} and {% if name %} in my about.html and find.html pages among other pages in my app. |`about.html`,<br/>`find.html`,<br/> `home.html` [`Line 4`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/home.html#L4) [`Line 13`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/find.html#L13)|✔|
| 4 : The jinja templates include some control structure|If conditional statements have been used in most of my html files an example is the home.html file which uses an if statement to check if a user is logged in or not|`home.html` [`Line 8`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/home.html#L8)|✔|
| 5 : It includes one or more forms|I have separated my class which creates the forms and can be found in forms.py. I have created two forms, registration form and article form. |`forms.py` [`ArticleForm`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/forms.py#L7) [`RegisterForm`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/forms.py#L12)|✔|
| 6 : The forms have some validation|I have used validation in both of my forms, in the registration form the validators set the minimum and maximum length of the input string. |`forms.py`<br/>[`Line 14`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/forms.py#L14)|✔|
| 7 : There are useful feedback messages to the user|I used several flash statements which alert the user if their login credentials do not match, inform them when they're logged out and if there is no article found. |`app.py`<br/> [`Line 197`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L197) <br/> [`Line 242`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L242) <br/>[`Line 138`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L138)|✔|
| 8 : It has a database backend that implemenets CRUD operations|For my database I am using MySQL and in order to satisfy the CRUD operations, I can create a user/article, read an article, update an article and delete an article and the changes can be seen in the database|`app.py`, <br/> `CREATE`[`Line298`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L298)<br/> `READ`[`Line161`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L161)<br/> `UPDATE`[`Line326`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L319)<br/> `DELETE`[`Line373`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L373)|✔|
| 9 : The create and update operations take input data from a form|In my add_article and edit_article methods, you can see that title and body of the articles submitted are taken from the form data.|`app.py`<br/>`CREATE`[`Lines303-304`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L303)<br/>`UPDATE`[`Lines339-340`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L339)|✔|
| 10 : There is user authentication|In the login method the user is not granted access if the password in the database and the password the user enters do not match also a user cannot edit an article which is not theirs, this can be seen in the edit_article method |`app.py`<br/> [`Line237`]( https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L237)<br/> [`Line342`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L342)|✔|
| 11 : The login process uses sessions|First sessesion is imported at the top of my app. Once the password in the database and the password the user enters match, a session is created |`app.py`<br/> [`Line 2`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L2) [`Lines239-240`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L239)|✔|
| 12 : Passwords are stored as hashes|Passwords are hashed on registration using the passlib.hash library and sha256_crypt|`app.py`<br/> [`Line 12`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L12)<br/> [`Line 187`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L187)|✔|
| 13 : There is a way to logout|I have implemented a logout method which clears the session and redirects the user to the login page|`app.py`<br/> [`Line 263-269`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L263)|✔|
| 14 : There is a basic API. Content can be accessed as json via http methods|I have implemented the basic API which allows one to view all the articles and the authors and date and time created|`app.py`<br/> [`Line 391-405`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L391)|✔|
| 15 : It should be clear how to access the API|You can access the basic API by going to the home page and clicking on the api link.|`app.py` <br/> [`Line 391`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L391) `_navbar.html`<br/> [`Line 28`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/includes/_navbar.html#L28)|✔|

______________________________________________________________________________________________________________________________________________________________________________________________________

| Extensions for My APP | FILENAME/LINE| DESCRIPTION |
| --- | --- |---|
| 1 : using wtforms is not required but is recommended|`forms.py`<br/> [`Line 2`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/forms.py#L2) <br/> [`Line 8`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/forms.py#L8)|I have imported and used flask WTF for both my ArticleForm and RegisterForm and have utilised the wtf form validators.|
| 2 : use of flask-login is not required but is recommended|`supportFunction.py` [`Line 6`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/supportFunction.py#L6)|Instead of using flask login I have a method in a separate python file `supportFunction.py` which checks if a user is logged in called def`check_user_logged_in`|
| 3 : using a salt is not required but is recommended|`app.py`<br/>[`Line 187`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L187)|With the use of sha256_crypt.encrypt() salt is generated and applied on passwords by default|
| 4 : additional credit will be given for an api that implements get,put and delete|`app.py`<br/>[`Line 66-110`]( https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L66)|I Have implemented a class called `RetrieveArticlesApi` which is an extesnsion to the basic api and is able to get put and delete articles using curl request|
| 5 : use of flask-restful is not required but is recommended|`app.py` <br/>[`Lines 22-24`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L22)<br/> [`Line 47`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L47)<br/>[`Line 68`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L68)|I have imported flask-restful and used it to apply the restful api|
| 6 : Access Control|`app.py`<br/>[`Lines 342-343`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L342) |One of the major changes and additions to my app is access control and making the app secure. One cannot edit or change an article/ forum post they havent written. I check if the user logged in is the one who is accessing the article if its not the access is unauthorized|
| 7 :CSRF |`app.py` <br/> [`Line 30`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/app.py#L30)<br/> `add_article`<br/>[`Line 7`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/add_article.html#L7)<br/>`edit_article`<br/>[`Line 7`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/myApp/templates/edit_article.html#L7)|I have ensured users of my web applications are protected against Cross-Site Request Forgery therefore to run and use the app a token is required.|

______________________________________________________________________________________________________

**References** <br/>
Below you can find the links i've used to build my flask application. <br/>
http://flask.pocoo.org/docs/1.0/quickstart/ <br/>
https://www.youtube.com/watch?v=zRwy8gtgJ1A - This is a video i got the idea from, i have adapted and changed most of the content. Examples of how i changed it is i've applied the dry principle by seperating some of the logic in the python files such as supportFunction.py and also have added both the basic Api and the restful Api as well. To protect against request forgery i have wrapped the whole app with **csrf**. <br/>
https://flask-mysqldb.readthedocs.io/en/latest/ <br/>
http://flask.pocoo.org/docs/1.0/patterns/wtforms/ <br/>
https://flask-wtf.readthedocs.io/en/stable/csrf.html <br/>

**'Please Note'** : I have used CSRF throught my whole app as mentioned above in order to ensure security and privacy of my users therefore to use the **DELETE** and **PUT** curl requests please comment out line 30 as advised by Dr Vala.  

 

**DELETE** CURL REQUEST
`curl http://doc.gold.ac.uk/usr/289/apirestful/<ENTER ID TO DELETE> -X DELETE`

**GET** CURL REQUEST
`curl http://doc.gold.ac.uk/usr/289/apirestful/<ENTER ID TO GET> -X GET`

**PUT** CURL REQUEST
`curl -d “body=<ENTER TEXT HERE>”http://doc.gold.ac.uk/usr/289/apirestful/<ENTER ID OF ARTICLE TO EDIT> -X PUT -v`

