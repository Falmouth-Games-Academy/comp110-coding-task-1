def print_highscore():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player$
    print ("<b>Top score</b><br />")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))
