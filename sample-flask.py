from flask import Flask, request, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def hello_world():
    name = request.args.get("name", default="", type=str)
    return render_template("hello.html", name=name)

app.run()
