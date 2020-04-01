import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from app.player.models import Player
from app import api, db

player = Blueprint('player', __name__)

parser = reqparse.RequestParser()
parser.add_argument('playerName', type=str)
parser.add_argument('nickName', type=str)
parser.add_argument('teamName', type=str)
parser.add_argument('role', type=str)
parser.add_argument('totalKills', type=int)
parser.add_argument('totalAssists', type=int)
parser.add_argument('totalDeaths', type=int)
parser.add_argument('totalMatchs', type=int)
parser.add_argument('totalVictories', type=int)
parser.add_argument('kda', type=float)
parser.add_argument('winningRate', type=float)

@player.route("/")
@player.route("/home")

def home():
    return "Catálogo de players de eSports"

class PlayerAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            players = Player.query.paginate(page, 10).items
        else:
            players = [Player.query.get(id)]
        if not players:
            abort(404)

        res = {}
        for plr in players:
            res[plr.id] = {
                'playerName'     :  plr.playerName,
                'nickName'       :  plr.nickName,
                'teamName'       :  plr.teamName,
                'role'           :  plr.role,
                'totalKills'     :  plr.totalKills,
                'totalAssists'   :  plr.totalAssists,
                'totalDeaths'    :  plr.totalDeaths,
                'totalMatchs'    :  plr.totalMatchs,
                'totalVictories' :  plr.totalVictories,
                'kda'            :  str(plr.kda),
                'winningRate'    :  str(plr.winningRate)
            }

        return json.dumps(res)

    def post(self):
        args = parser.parse_args()

        playerName     = args['playerName']
        nickName       = args['nickName']
        teamName       = args['teamName']
        role           = args['role']
        totalKills     = args['totalKills']
        totalAssists   = args['totalAssists']
        totalDeaths    = args['totalDeaths']
        totalMatchs    = args['totalMatchs']
        totalVictories = args['totalVictories']
        kda            = (totaKills + totalAssists) if totalDeaths == 0 else (totalKills + totalAssists / totalDeaths)
        winningRate    = ((totalVictories / totalMatchs) * 100)

        plr = Player(playerName, nickName, teamName, role, totalKills, totalAssists, totalDeaths, totalMatchs, totalVictories, kda, winningRate)
        db.session.add(plr)
        db.session.commit()

        res = {}
        res[plr.id] = {
                'playerName'     :  plr.playerName,
                'nickName'       :  plr.nickName,
                'teamName'       :  plr.teamName,
                'role'           :  plr.role,
                'totalKills'     :  plr.totalKills,
                'totalAssists'   :  plr.totalAssists,
                'totalDeaths'    :  plr.totalDeaths,
                'totalMatchs'    :  plr.totalMatchs,
                'totalVictories' :  plr.totalVictories,
                'kda'            :  str(plr.kda),
                'winningRate'    :  str(plr.winningRate)
            }

        return json.dumps(res)

    def delete(self, id):
        con = Player.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {'id' : id}
        return json.dumps(res)

    def put(self, id):
        con = Player.query.get(id)
        args = parser.parse_args()

        playerName     = args['playerName']
        nickName       = args['nickName']
        teamName       = args['teamName']
        role           = args['role']
        totalKills     = args['totalKills']
        totalAssists   = args['totalAssists']
        totalDeaths    = args['totalDeaths']
        totalMatchs    = args['totalMatchs']
        totalVictories = args['totalVictories']
        kda            = (totaKills + totalAssists) if totalDeaths == 0 else (totalKills + totalAssists / totalDeaths)
        winningRate    = ((totalVictories / totalMatchs) * 100)

        con.playerName     = playerName
        con.nickName       = nickName
        con.teamName       = teamName
        con.role           = role
        con.totalKills     = totalKills
        con.totalAssists   = totalAssists
        con.totalDeaths    = totalDeaths
        con.totalMatchs    = totalMatchs
        con.totalVictories = totalVictories
        con.kda            = kda
        con.winningRate    = winningRate

        db.session.commit()

        res = {}
        res[con.id] = {
                'playerName'     :  con.playerName,
                'nickName'       :  con.nickName,
                'teamName'       :  con.teamName,
                'role'           :  con.role,
                'totalKills'     :  con.totalKills,
                'totalAssists'   :  con.totalAssists,
                'totalDeaths'    :  con.totalDeaths,
                'totalMatchs'    :  con.totalMatchs,
                'totalVictories' :  con.totalVictories,
                'kda'            :  str(con.kda),
                'winningRate'    :  str(con.winningRate)
            }

        return json.dumps(res)

api.add_resource(
    PlayerAPI,
    '/api/player',
    '/api/player/<int:id>',
    '/api/player/<int:id>/<int:page>'
)