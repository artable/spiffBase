import datetime
import mysql.connector
import mysql.connector.cursor

class SpiffBaseInterface :
    """Static class, contains methods for interacting with
    SpiffBase, including insert statements and various queries.
    No delete statements included."""

    insert_xfer = """
    INSERT INTO xfers (time, goal, actual, user_id, channel_id)
    SELECT %s, %s, %s, user_id, channel_id
    FROM users join channels
    WHERE user_name = %s and channel_name = %s
    """
    query_xfers = """
    SELECT is_billable
    FROM xfers x INNER JOIN users u
    ON x.user_id = u.user_id
    INNER JOIN channels c
    ON x.channel_id = c.channel_id
    WHERE user_name = %s
    AND x.time BETWEEN %s AND %s
    """

    @staticmethod
    def record_xfer(cnx: mysql.connector, data: dict) -> int:
        """record a single xfer."""
        #TODO type hint dict should contain dictionary keys and expected values
        cursor = cnx.cursor()
        xfer = (
            data.get("time", datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")),
            data.get("goal", None),
            data.get("actual", None),
            data.get("user", None),
            data.get("channel", None))
        cursor.execute(SpiffBaseInterface.insert_xfer, xfer)
        cnx.commit()
        cursor.close()
        return 1

    @staticmethod
    def get_xfers(cnx: mysql.connector, perams: dict) -> list:
        """create a over a given period of time. if query contains a user,
        will always pull xfers for that user, even if team or channel params
        are given."""
        cursor = cnx.cursor()
        query_vals = (
            perams.get("user"),
            perams.get("start", datetime.datetime.today().strftime("%y-%m-%d")),
            perams.get("end", datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        )
        cursor.execute(SpiffBaseInterface.query_xfers, query_vals)

        result = []
        for (is_billable) in cursor:
            result.append(is_billable)
        return result
            

xfer = {
    "user": "Jonah Deal",
    "channel": "ml_team_merrol",
    "goal": 7,
    "actual": 1,
}



def tests(spiffbase) :
    SpiffBaseInterface.record_xfer(spiffbase, xfer)

    query = {
        "user": "Jonah Deal"
    }
    print(SpiffBaseInterface.get_xfers(spiffbase, query))

    spiffbase.close






spiffbase = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

tests(spiffbase)
