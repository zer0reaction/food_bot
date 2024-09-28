import sqlite3


def check_user_exists(user_id: int):
    con = sqlite3.connect("./db/users.db")
    cur = con.cursor()

    # checking if the user is in our database
    cur.execute("""

    SELECT EXISTS(
        SELECT 1 
        FROM state 
        WHERE user_id = {}
    )

    """.format(str(user_id)))

    record = cur.fetchone()

    user_exists = (record[0] == 1)

    con.close()
    return user_exists


def get_user_state(user_id: int):
    con = sqlite3.connect("./db/users.db")
    cur = con.cursor()

    # checking if the user is in our database
    user_exists = check_user_exists(user_id)
    if not user_exists: return None

    # getting user_state
    cur.execute("SELECT user_state FROM state LIMIT 1")
    user_state = cur.fetchone()

    con.close()
    return user_state


def update_user_state(user_id: int, user_state: str):
    con = sqlite3.connect("./db/users.db")
    cur = con.cursor()

    # checking if the user is in our database
    user_exists = check_user_exists(user_id)

    # updating or adding state
    if user_exists:
        cur.execute("""

        UPDATE state 
        SET user_state = '{}' 
        WHERE user_id = {}

        """.format(str(user_state), user_id))

        print("Changed user state for {} to {}".format(str(user_id), user_state))

    else:
        cur.execute("INSERT INTO state VALUES({}, '{}')".format(str(user_id), user_state))
        print("Added user {} with state {}".format(str(user_id), user_state))

    con.commit()
    con.close()
