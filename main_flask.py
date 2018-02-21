from flask import Flask
from flask import render_template
from flask import request
import create_map_with_users

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def requesr_form():
    return render_template("request_form.html")

@app.route("/", methods=["POST"])
def build_map():
    if request.form["user-name"] == "" or request.form["number"] == "":
        return render_template("failure.html")
    acct = request.form["user-name"]
    num_of_users = int(request.form["number"])
    map_dict = create_map_with_users.collect_info(acct, num_of_users)
    create_map_with_users.create_map(map_dict)
    return render_template("twitter_friends_map.html")

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=8080)

    app.run(debug=True)
