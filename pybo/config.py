import os

# 프로젝트의 루트 디렉터리
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소이다.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLALCHEMY_TRACK_MODIFICATION는 SQLAlchemy의 이벤트를 처리하는 옵션이다.
SQLALCHEMY_TRACK_MODIFICATIONS = False