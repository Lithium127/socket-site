from flask import Flask, render_template
from app import config

def create_app(config: config.BaseConfig):
    
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    @app.route("/")
    def index():
        return render_template('index.html')
    
    return app