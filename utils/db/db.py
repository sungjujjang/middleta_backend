import sqlite3
import os
import datetime
import time
import utils.check_email as check_email

def start_db():
    db_path = os.path.join(os.path.dirname(__file__), 'db.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

    return conn, cursor

def check_id_duplication(id):
    con, cur = start_db()
    cur.execute(f"SELECT * FROM user where user_id='{id}'")
    user = cur.fetchone()
    if user:
        con.close()
        return True
    else:
        con.close()
        return False

def check_user(id):
    con, cur = start_db()
    cur.execute(f"SELECT * FROM user where user_id='{id}'")
    user = cur.fetchone()
    if user:
        return user
    else:
        return {
            "status" : "ERROR",
            "message" : "No User"
        }
    
# TODO : USER ADD/UPDATE/DELETE

def add_user(id, passowrd, nickname, email=None):
    if check_id_duplication(id):
        return {
            "status" : "ERROR",
            "message" : "Duplication id"
        }
    if email and check_email.check_email(email) == False:
        return {
            "status" : "ERROR",
            "message" : "Email Fuck"
        }
    now_tstamp = time.time()
    con, cur = start_db()
    if email:
        cur.execute(f"INSERT INTO user VALUES ('{id}', '{passowrd}', '{nickname}', '{now_tstamp}', '{email}')")
    else:
        cur.execute(f"INSERT INTO user VALUES ('{id}', '{passowrd}', '{nickname}', '{now_tstamp}', NULL)")
    con.commit()
    con.close()
    return {
        "status" : "SUCCESS",
        "message" : "Added User"
    }

def update_user(target_id ,id=None, passowrd=None, nickname=None, email=None):
    if not id and not passowrd and not nickname and not email:
        return {
            "status" : "SUCCESS",
            "message" : "Updated User"
        }
    
    if check_id_duplication(target_id) == False:
        return {
            "status" : "ERROR",
            "message" : "No User"
        }
    if check_id_duplication(id):
        return {
            "status" : "ERROR",
            "message" : "Duplication id"
        }
    if email and check_email.check_email(email) == False:
        return {
            "status" : "ERROR",
            "message" : "Email Fuck"
        }
    
    query = ""
    if id:
        query += f"user_id='{id}', "
    if passowrd:
        query += f"passowrd='{passowrd}', "
    if nickname:
        query += f"nickname='{nickname}', "
    if email:
        query += f"email='{email}', "
        
    query = query[:-2]
    print(query)
    
    con, cur = start_db()
    cur.execute(f"UPDATE user SET {query} WHERE user_id='{target_id}'")
    con.commit()
    con.close()
    return {
        "status" : "SUCCESS",
        "message" : "Updated User"
    }
    
def delete_user(id):
    if check_id_duplication(id) == False:
        return {
            "status" : "ERROR",
            "message" : "No User"
        }
    con, cur = start_db()
    cur.execute(f"DELETE FROM user where user_id='{id}'")
    con.commit()
    con.close()
    return {
        "status" : "SUCCESS",
        "message" : "Deleted User"
    }