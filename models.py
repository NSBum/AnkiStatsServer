from app import db

class Stats(db.Model):
    """An Anki statistics object
    """
    __tablename__ = 'stats'

    # s_id : unique row id
    s_id = db.Column(db.Integer, primary_key=True)

    # timestamp : UNIX Epoch
    timestamp = db.Column(db.Integer)
    # vocab : number of vocabulary notes
    vocab = db.Column(db.Integer)
    # tcount : total card cound in the collection
    tcount = db.Column(db.Integer)
    # review : number reviewed
    review = db.Column(db.Integer)
    # due : number that were due
    due = db.Column(db.Integer)
    # filt : number of filtered cards reviewed
    filt = db.Column(db.Integer)
    # msum : total mature cards presented
    msum = db.Column(db.Integer)
    # mcnt : mature cards marked correctly
    mcnt = db.Column(db.Integer)
    # relearn : cards relearned
    relearn = db.Column(db.Integer)
    # learn : cards learned
    learn = db.Column(db.Integer)
    # duration : total duration of study
    duration = db.Column(db.Integer)
    # total : cards studied today
    total = db.Column(db.Integer)
    # tomorrow : cards due tomorrow
    tomorrow = db.Column(db.Integer)
    # tretent : true retention rate
    tretent = db.Column(db.Float)


    def __init__(self,data):
        self.timestamp = data['time']
        self.vocab = data['vocab']
        self.tcount = data['tcount']
        self.review = data['review']
        self.due = data['review']
        self.filt = data['filter']
        self.msum = data['msum']
        if( self.msum == None ):
            self.msum = 0;
        self.mcnt = data['mcnt']
        self.relearn = data['relearn']
        self.learn = data['learn']
        self.duration = data['duration']
        self.total = data['total']
        self.tomorrow = data['tomorrow']
        self.tretent = data['trueRetention']
