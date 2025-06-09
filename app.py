from flask import Flask
from config import Config
from extensions import db, login_manager

# Создаем и настраиваем приложение
app = Flask(__name__)
app.config.from_object(Config)

# Инициализируем расширения
db.init_app(app)
login_manager.init_app(app)

# Регистрация callback для загрузки пользователя
@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Регистрируем Blueprints
from routes.auth import auth_bp
from routes.courses import courses_bp
from routes.lessons import lessons_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(lessons_bp)
app.register_blueprint(dashboard_bp)

# Создаем таблицы и запускаем сервер
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
