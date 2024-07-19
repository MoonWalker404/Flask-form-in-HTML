from flask import Flask

# Создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'you will never guess'

from app import routes