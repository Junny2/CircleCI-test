from flask import Flask, render_template
from flask_migrate import Migrate


from models.customer import db
from routes.customer_bp import customer_bp


app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(customer_bp, url_prefix='/customer')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()