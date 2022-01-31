from pybo import db

class Question(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    # db.ForeignKey 에 지정한 첫 번째 값은 연결할 모델의 속성명, 두번째 ondelete에 지정한 값은 삭제 연동 설정이다.
    # ondelete='CASCADE' 에 의해 데이터베이스에서 쿼리를 이용해 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다.
    question_id=db.Column(db.Integer, db.ForeignKey('question.id',ondelete='CASCADE'))
    # db.relationship에 지정한 첫 번째 값은 참조할 모델이고, 두 번째 backref에 지정한 값은 역참조 설정이다.
    # 역참조란 쉽게 말해 질문에서 답변을 참조하는 것을 의미한다. 한 질문에는 여러 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변을 참조할 수 있게 한다.
    # 예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변을 참조할 수 있다.
    question=db.relationship('Question', backref=db.backref('answer_set',))
    content=db.Column(db.Text(),nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)