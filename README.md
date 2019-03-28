**Data and The Web - Final Submission - My APP - HAMZE MUUSE**

**URL for My APP** 
--> Will only work once you run app.py on the terminal

Link to my web app: http://doc.gold.ac.uk/usr/289/

**Link to all my commits** : https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/commits/master

**I have created my Flask application using the skills I have learnt throughout the Data and the Web module, both in term 1 and term 2. In addition to the module lab content and examples, I have used an online flask tutorial to build an article flask application from scratch. In order to extend on the online tutorial and the templates given to me, I have tried to implement a DRY the principle and separation of concern, by structuring my code in a modular way. I have also improved upon the tutorial by adding access control logic as well as additional security to prevent cross site forgery requests from taking place.**

**SUBMISSION:**
 
| **SUBMISSION INSTRUCTIONS** | **COMPLETE/NOT COMPLETE** |
| --- | --- |
| App run's without debug=True |  ✔ |
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
| 1 : It is a flask iapp |I have used the flask micro framework in this web application and you can see this with the use of the flask class and the use of the instance of this class with "app = Flask(__name__)”|app.py, Line 2|✔|
| 2 : There is more than one route and more than one view |I have used multiple routes in my web application some examples include @app.route(‘/’), @app.route(‘about’), @app.route(‘find’) etc.|`app.py`,[`Line 108`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L108)[`Line113`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L113)[`Line137`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L137)|✔|
| 3 : The html is rendered using jinja templates|I have rendered my html pages using jinja, you can see this with the use of ‘{%block body%} and {% if name %} in my about.html and find.html pages among other pages in my app. |`about.html`,`find.html`, `home.html` [`Line 4`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/templates/home.html#L4) [`Line 13`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/templates/find.html#L13)|✔|
| 4 : The jinja templates include some control structure|If conditional statements have been used in most of my html files an example is the home.html file which uses an if statement to check if a user is logged in or not|`home.html` [`Line8`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/templates/home.html#L8)|✔|
| 5 : It includes one or more forms|I have separated my class which creates the forms and can be found in forms.py. I have created two forms, registration form and article form. |`forms.py` [`ArticleForm`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/forms.py#L7) [`RegisterForm`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/forms.py#L12)|✔|
| 6 : The forms have some validation|I have used validation in both of my forms, in the registration form the validators set the minimum and maximum length of the input string. |`forms.py`[`Line 14`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/forms.py#L14)|✔|
| 7 : There are useful feedback messages to the user|I used several flash statements which alert the user if their login credentials do not match, inform them when they're logged out and if there is no article found. |`app.py` [`Line 190`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L190) <br/> [`Line 260`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L260) [`Line 131`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L131)|✔|
| 8 : It has a database backend that implemenets CRUD operations|For my database I am using MySQL and in order to satisfy the CRUD operations, I can create a user/article, read an article, update an article and delete an article and the changes can be seen in the database|`app.py` [`Create`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L291) [`Read`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L154) [`Update`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L319) [`Delete`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L366)|✔|
| 9 : The create and update operations take input data from a form|In my add_article and edit_article methods, you can see that title and body of the articles submitted are taken from the form data.|`app.py` [`Create`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L296) [`Update`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L332)|✔|
| 10 : There is user authentication|In the login method the user is not granted access if the password in the database and the password the user enters do not match also a user cannot edit an article which is not theirs, this can be seen in the edit_article method |`app.py` [`Line 230`]( https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L230)<br/> [`Line 335`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L335)|✔|
| 11 : The login process uses sessions|First sessesion is imported at the top of my app. Once the password in the database and the password the user enters match, a session created |`app.py` [`Line 2`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L2) [`Line 232`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L232)|✔|
| 12 : Passwords are stored as hashes|Passwords are hashed on registration using the passlib.hash library and sha256_crypt|`app.py` [`Line 12`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L12) [`Line 180`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L180)|✔|
| 13 : There is a way to logout|I have implemented a logout method which clears the session and redirects the user to the login page|`app.py` [`Line 256`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L256)|✔|
| 14 : There is a basic API. Content can be accessed as json via http methods|I have implemented the basic API which allows one to view all the articles and the authors and date and time created|`app.py` [`Line 386`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L386)|✔|
| 15 : It should be clear how to access the API|You can access the basic API by going to the home page and clicking on the api link.|`app.py` [`Line 384`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L384) `navbar.html` [`Line 28`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/templates/includes/_navbar.html#L28)|✔|


| Extensions for My APP | FILENAME/LINE| DESCRIPTION |
| --- | --- |---|
| 1 : using wtforms is not required but is recommended|`forms.py`<br/> [`Line 2`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/forms.py#L2) <br/> [`Line 8`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/forms.py#L8)|I have imported and used flask WTF for both my ArticleForm and RegisterForm and have utilised the wtf form validators.|
| 2 : use of flask-login is not required but is recommended|`supportFunction.py` [`Line 6`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/supportFunction.py#L6)|Instead of using flask login I have a method in a separate python file `supportFunction.py` which checks if a user is logged in called def`check_user_logged_in`|
| 3 : using a salt is not required but is recommended|`app.py`  [`Line 180`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L180)|With the use of sha256_crypt.encrypt() salt is generated and applied on passwords by default|
| 4 : additional credit will be given for an api that implements get,post,push and delete|`app.py`[`Line 66`]( https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L66)|I Have implemented a class called `RetrieveArticlesApi` which uses is an extesnsion to the basic api and is able to get post push and delete articles using curl|
| 5 : use of flask-restful is not required but is recommended|`app.py` <br/>[`Lines 22-25`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L22)<br/> [`Line 47`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L47)<br/>[`Line 68`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L68)|I have imported flask-restful and used it to apply the restful api|
| 6 : Access Control|`app.py`[`Lines 335-336`](https://gitlab.doc.gold.ac.uk/hmuus001/term-2-lab/blob/master/supportNewApp/app.py#L335) |One of the major changed and additions to my app is access control and making the app secure. One cannot edit or change an article/ forum post they havent written. I check if the user logged in is the one who is accessing the article if its not the access is unauthorized|
| 7 :SQL Alchemy |#|#|

