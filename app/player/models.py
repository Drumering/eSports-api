from app import db

class Player(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    playerName     = db.Column(db.String(100))
    nickName       = db.Column(db.String(100))
    teamName       = db.Column(db.String(100))
    role           = db.Column(db.String(100))
    totalKills     = db.Column(db.Integer)
    totalAssists   = db.Column(db.Integer)
    totalDeaths    = db.Column(db.Integer)
    totalMatchs    = db.Column(db.Integer)
    totalVictories = db.Column(db.Integer)
    kda            = db.Column(db.Float(asdecimal=True))
    winningRate    = db.Column(db.Float(asdecimal=True))

    def __init__(self,playerName,nickName,teamName,role,totalKills,totalAssists,totalDeaths,totalMatchs, totalVictories,kda,winningRate):
        self.playerName     = playerName
        self.nickName       = nickName
        self.teamName       = teamName
        self.role           = role
        self.totalKills     = totalKills
        self.totalAssists   = totalAssists
        self.totalDeaths    = totalDeaths
        self.totalMatchs    = totalMatchs
        self.totalVictories = totalVictories
        self.kda            = kda
        self.winningRate    = winningRate

    def __repr__():
        return 'Player {0}'.format(self.id)