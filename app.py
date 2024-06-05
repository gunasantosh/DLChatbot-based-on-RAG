from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "gt"


from views import views

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run()
