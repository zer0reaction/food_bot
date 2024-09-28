import sqlite3

def update_user_state(user_id: int, user_state: str):
    con = sqlite3.connect("./db/users.db")
    cur = con.cursor()

    cur.execute("SELECT EXISTS(SELECT 1 FROM state WHERE user_id={})".format(user_id))
    record = cur.fetchone()

    user_exists = (record[0] == 1)

    if user_exists:
        cur.execute("UPDATE state SET user_state = '{}' WHERE user_id = {}".format(user_state, user_id))
        print("Changed user state for {} to {}".format(str(user_id), user_state))

    else:
        cur.execute("INSERT INTO state VALUES({}, '{}')".format(user_id, user_state))
        print("Added user {} with state {}".format(str(user_id), user_state))

    con.commit()
    con.close()
