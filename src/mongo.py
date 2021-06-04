from pymongo import MongoClient


client = MongoClient('mongo_db', 27017)
sample_db = client.sample
team_collection = sample_db.team_collection

post = [
    {'name': 'アトランタ・ブレーブス', 'district': 'ナ・東地区', 'ranking_2020': 1},
    {'name': 'フロリダ・マーリンズ', 'district': 'ナ・東地区', 'ranking_2020': 2},
    {'name': 'シカゴ・カブス', 'district': 'ナ・中地区', 'ranking_2020': 1},
    {'name': 'セントルイス・カージナルス', 'district': 'ナ・中地区', 'ranking_2020': 2},
    {'name': 'ロサンゼルス・ドジャース', 'district': 'ナ・西地区', 'ranking_2020': 1},
    {'name': 'サンディエゴ・パドレス', 'district': 'ナ・西地区', 'ranking_2020': 2},
]
# データの挿入
team_collection.insert_many(post)

for team in team_collection.find():
    print(team)
