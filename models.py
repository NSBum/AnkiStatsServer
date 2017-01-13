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
    # tcount : total card count in the collection
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
    # ez_avg : average ease
    ez_avg = db.Column(db.Float)
    # ez_low : lowest ease
    ez_low = db.Column(db.Float)
    # ez_high : highest ease
    ez_high = db.Column(db.Float)
    # mtr : mature vocab card count
    mtr = db.Column(db.Integer)
    # yng: young/learn vocab card count
    yng = db.Column(db.Integer)
    # new: new vocab card count
    new = db.Column(db.Integer)
    # susp: suspended vocab card count
    susp = db.Column(db.Integer)
    # good_lrn: fraction of learning cards marked good
    good_lrn = db.Column(db.Float)
    # good_yng: fraction of young cards marked good
    good_yng = db.Column(db.Float)
    # good_mature: fraction of mature cards marked good
    good_mature = db.Column(db.Float)

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
        self.ez_avg = data['avgEase']
        self.ez_low = data['lowEase']
        self.ez_high = data['highEase']
        self.mtr = data['mtr']
        self.yng = data['yng']
        self.new = data['new']
        self.susp = data['susp']
        self.good_lrn = data['good_lrn']
        self.good_yng = data['good_yng']
        self.good_mature = data['good_mature']
