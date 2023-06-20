from models.database import db

def select(query):
    result = db.session.execute(query)
    return result.fetchall()

def select_fetchone(query, params=None):
    result = db.session.execute(query, params)
    return result.fetchone()

def insert(sql, params):
    db.session.execute(sql, params)

def update(sql, params):
    db.session.execute(sql, params)

def delete(model_instance):
    db.session.delete(model_instance)
    db.session.commit()

def begin_transaction():
    db.session.begin()

def commit_transaction():
    db.session.commit()

def rollback_transaction():
    db.session.rollback()

def close_transaction():
    db.session.close()
