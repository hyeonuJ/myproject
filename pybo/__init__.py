from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix" : "ix_%(column_0_label)s",
    "uq" : "uq_%(table_name)s_%(column_0_name)s",
    "ck" : "ck_%(table_name)s_%(column_0_name)s",
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk" : "pk_%(table_name)s"
}

db=SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    #config.py 파일에 작성한 항목을 app.config 환경 변수로 부르기 위한 코드
    app.config.from_object(config)
    
    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app,db,render_as_batch=True)
    else:
        migrate.init_app(app,db)
    migrate.init_app(app,db)
    # migrate 객체가 models.py 파일 참조하게 함
    from . import models

    #블루프린트
    from .views import main_views,question_views,answer_views,auth_views,comment_views,vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    
    return app