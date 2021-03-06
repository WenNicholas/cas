from cas.extensions import db

class Application(db.Model):
    __tablename__ = 'application'

    domain = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    callback_url = db.Column(db.String(128), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    tgt_expire = db.Column(db.Integer, nullable=False)
    st_expire = db.Column(db.Integer, nullable=False)
    
    def existDomain(domain):
        result = Application.query.filter(Application.domain == domain).first()
        return result is not None
    
    def get(domain):
        return Application.query.filter(Application.domain == domain).first()
