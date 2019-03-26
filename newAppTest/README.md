| APP CRITERIA | DESCRIPTION | LINES |
| --- | --- | --- |
| 1 : It is a flask app |I have used the flask micro framework in this web application and you can see this with the use of the flask class and the use of the instance of this class with "app = Flask(__name__)”|#|
| 2 : There is more than one route and more than one view |I have used multiple routes in my web application some examples include @app.route(‘/’), @app.route(‘about’), @app.route(‘find’) etc.|#|
| 3 : The html is rendered using jinja templates|I have rendered my html pages using jinja, you can see this with the use of ‘{%block body%} and {% if name %} in my about.html and find.html pages among other pages in my app. |#|
| 4 : The jinja templates include some control structure|#|#|
| 5 : It includes one or more forms|I have separated my class which creates the forms and can be found in forms.py. I have created two forms, registration form and article form. |#|
| 6 : The forms have some validation|I have used validation in both of my forms, in the registration form the validators set the minimum and maximum length of the input string. |#|
| 7 : There are useful feedback messages to the user|I used several flash statements which alert the user if their login credentials do not match, if no article is found and if the username they pick on registration is taken. |#|
| 8 : It has a database backend that implemenets CRUD operations|For my database I am using MySQL and in order to satisfy the CRUD operations, I can create a user/article, read an article, update an article and delete an article and the changes can be seen in the database|#|
| 9 : The create and update operations take input data from a form|In my add_article and edit_article methods, you can see that title and body of the articles submitted are taken from the form data.|#|
| 10 : There is user authentication|In the login method the user is not granted access if the password in the database and the password the user enters do not match also a user cannot edit an article which is not theirs, this can be seen in the edit_article method |#|
| 11 : The login process uses sessions|| Once the password in the database and the password the user enters match, a session created |#|
| 12 : Passwords are stored as hashes|Passwords are hashed on registration using the passlib.hash library and sha256_crypt|#|
| 13 : There is a way to logout|I have implemented a logout method which clears the session and redirects the user to the login page|#|
| 14 : There is a basic API. Content can be accessed as json via http methods|I have implemented the basic API which allows one to view all the articles and the authors and date and time created|#|
| 15 : It should be clear how to access the API|You can access the basic API by going to the home page and clicking on the api link.|#|


| Extensions for My APP | DESCRIPTION |
| --- | --- |
| 1 : using wtforms is not required but is recommended|#|
| 2 : use of flask-login is not required but is recommended|#|
| 3 : using a salt is not required but is recommended|#|
| 4 : additional credit will be given for an api that implements get,post,push and delete|#|
| 5 : use of flask-restful is not required but is recommended|#|
| 6 : using sqlalchemy is not required but will attract credit|#|

