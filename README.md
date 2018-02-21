# twitter_users_info 
# Please, check out web application (visualization-map):  http://lanastasia.pythonanywhere.com/
This project allows You to get information about friends of certain twitter account. You enter the user-name of account, whose friends You would like to explore and the number of friends to get information about. If You are using analyse_json.py and giving the command line input, You should also enter the key parameter of information type.

This project consists of two subprojects: <br>
first one - returnes any information You seek, if it's accessible from Twitter. The main module of the first subproject is  analyse_json.py , but it also needs additional modules for correct work (hidden.py, oauth.py, twurl.py).<br>
second one - creates an interactive map with user's friends marked on it. <br>To use this map, please check out this web application - http://lanastasia.pythonanywhere.com/ and fill in all fields of the form, then You will be redirected to the interactive map. 

