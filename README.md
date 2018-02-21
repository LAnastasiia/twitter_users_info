# twitter_users_info 
# Please, check out web application (visualization-map):  http://lanastasia.pythonanywhere.com/
This project allows You to get information about friends of certain twitter account. You enter the user-name of account, whose friends You would like to explore. Also a number of frienfs and the key parameter of information type are demanded.

This project consists of two subprojects: <br>
first one - <b>analyse_json.py</b> - returnes any information You seek, if it's accessible from Twitter. analyse_json.py is the main module of the first subproject, but it also needs additional modules for correct work (hidden.py, oauth.py, twurl.py).<br>
second one - <b>create_map_with_users.py + main_flask.py</b> - creates an interactive map with user's friends marked on it. <br>To use this map, please check out this web application - http://lanastasia.pythonanywhere.com/ and fill in all fields of the form, then You will be redirected to the interactive map. 

