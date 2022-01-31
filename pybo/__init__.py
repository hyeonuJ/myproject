from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    #config.py 파일에 작성한 항목을 app.config 환경 변수로 부르기 위한 코드
    app.config.from_object(config)
    
    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    # migrate 객체가 models.py 파일 참조하게 함
    from . import models

    #블루프린트
    from .views import main_views,question_views,answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app