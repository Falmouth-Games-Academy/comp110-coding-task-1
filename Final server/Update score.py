def update_score():
    first_name = str(form.getvalue('first_name'))
    last_name = str(form.getvalue('last_name'))
    score = str(form.getvalue('score'))

    get_id = c.execute("SELECT id FROM players "
    "WHERE first_name=%s",
    (first_name))

    get_number = ([(r[0]) for r in c.fetchall()])
    id = get_number[0]
    player_id = str(json.dumps(id))

    update_score = c.execute("UPDATE scores "
    "SET score=%s WHERE player_id=%s",
    (score, player_id))

    conn.commit()
    print("Score updated")