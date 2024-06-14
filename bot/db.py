import sqlite3
import datetime

class DBInterface:
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.con.cursor()


DB = DBInterface('database')


def exist_user(user_id: int) -> bool:
    return DB.cur.execute(f"""
        SELECT 1 from users WHERE id = {user_id}
    """).fetchone() is not None


def add_user(user_id: int, inviter=None) -> None:
    DB.cur.execute(f"""
        INSERT INTO users(id, refcode, inviter)
        VALUES(
            "{user_id}",
            "{user_id}",
            "{inviter}"
        )
    """)
    DB.con.commit()


def change_trade_link(user_id: int, trade_link: str) -> None:
    DB.cur.execute(f"""
        UPDATE users
        SET tradelink = "{trade_link}"
        WHERE id = "{user_id}"
    """)
    DB.con.commit()


def get_trade_link(user_id: int) -> str:
    return DB.cur.execute(f"""
        SELECT tradelink FROM users WHERE id = {user_id}
    """).fetchone()


def get_show_info(user_id: int) -> list[str]:
    return DB.cur.execute(f"""
        SELECT tradelink, balance, invited FROM users WHERE id = {user_id}
    """).fetchone()


def increase_balance(user_id: int) -> None:
    balance, invited = DB.cur.execute(f"""
    SELECT balance, invited FROM users 
    WHERE id = {user_id}""").fetchone()

    balance += 1
    invited += 1

    DB.cur.execute(f"""
        UPDATE users
        SET balance = "{balance}" , invited = "{invited}" 
        WHERE id = "{user_id}"
    """)
    DB.con.commit()


def get_users() -> list[int]:
    return list(map(lambda x: x[0], DB.cur.execute("""
    SELECT id FROM users
    """).fetchall()))


def create_ticket(user_id: int, username: str = "") -> None:
    trade_link, amount = DB.cur.execute(f"""
    SELECT tradelink, balance FROM users WHERE id = {user_id}
    """).fetchone()

    DB.cur.execute(f"""
    INSERT INTO tickets(user_id, tradelink, amount, date, username)
    VALUES(
        "{user_id}",
        "{trade_link}",
        "{amount}",
        "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}",
        "{username}"
    )
    """)

    DB.cur.execute(f"""
        UPDATE users
        SET balance = "0"
        WHERE id = "{user_id}"
    """)

    DB.con.commit()


def get_all_tickets() -> list[list]:
    return DB.cur.execute("""
    SELECT * from tickets
    """).fetchall()


def get_one_ticket() -> list:
    return DB.cur.execute("""
        SELECT * from tickets
        """).fetchone()


def delete_ticket(ticket_id: int):
    DB.cur.execute(f"""
        DELETE FROM tickets WHERE id = {ticket_id}
        """)
    DB.con.commit()


def reject_ticket(ticket_id):
    user_id, amount = DB.cur.execute(f"""
    SELECT user_id, amount from tickets WHERE id = {ticket_id}
    """).fetchone()

    balance = DB.cur.execute(f"""
    SELECT balance from users WHERE id = {user_id}
    """).fetchone()[0]

    DB.cur.execute(f"""
        UPDATE users
        SET balance = "{amount + balance}"
        WHERE id = "{user_id}"
    """)
    delete_ticket(ticket_id)
    DB.con.commit()



