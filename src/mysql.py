import MySQLdb


conn = MySQLdb.connect(
    host='mysql_db',
    db='sample',
    user='root',
    port=3306,
    password='password',
    charset='utf8mb4'
)

c = conn.cursor()

# テーブルを新規作成
c.execute('DROP TABLE IF EXISTS team')
c.execute('''
    CREATE TABLE team (
        name text,
        district text,
        ranking_2020 integer
    )
''')

c.executemany('INSERT INTO team VALUES (%(name)s, %(district)s, %(ranking_2020)s)', [
    {'name': 'タンパベイ・レイズ', 'district': 'ア・東地区', 'ranking_2020': 1},
    {'name': 'ニューヨーク・ヤンキース', 'district': 'ア・東地区', 'ranking_2020': 2},
    {'name': 'ミネソタ・ツインズ', 'district': 'ア・中地区', 'ranking_2020': 1},
    {'name': 'シカゴ・ホワイトソックス', 'district': 'ア・中地区', 'ranking_2020': 2},
    {'name': 'オークランド・アスレチックス', 'district': 'ア・西地区', 'ranking_2020': 1},
    {'name': 'ヒューストン・アストロズ', 'district': 'ア・西地区', 'ranking_2020': 2},
])
conn.commit()

c.execute('SELECT * FROM team')
for row in c.fetchall():
    print(row)

# コネクションを閉じる。
conn.close()
