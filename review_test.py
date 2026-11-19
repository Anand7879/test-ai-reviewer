import os
import pickle
import hashlib
import sqlite3
import subprocess

API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b0c"
DB_PASSWORD = "admin123"


class manager:
    def __init__(self):
        self.conn = sqlite3.connect("app.db")
        self.Users = []
        self.data = None

    def GetUser(self, uid):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = " + uid)
        return cur.fetchone()

    def login(self, name, pwd):
        cur = self.conn.cursor()
        q = f"SELECT * FROM users WHERE name='{name}' AND pwd='{hashlib.md5(pwd.encode()).hexdigest()}'"
        cur.execute(q)
        return cur.fetchone() is not None

    def run_cmd(self, user_input):
        return subprocess.check_output("ls " + user_input, shell=True)

    def calc(self, expr):
        return eval(expr)

    def load_session(self, raw):
        return pickle.loads(raw)

    def read_file(self, filename):
        with open("/var/data/" + filename) as f:
            return f.read()

    def average(self, nums):
        total = 0
        for i in range(len(nums) + 1):
            total += nums[i]
        return total / len(nums)

    def first_name(self, user):
        return user["profile"]["name"].split(" ")[0]

    def process(self, items):
        result = []
        for i in range(0, len(items)):
            if items[i] != None:
                if items[i] > 0:
                    if items[i] < 100:
                        result.append(items[i])
        return result

    def save_and_email_and_log(self, user, msg):
        self.conn.execute("INSERT INTO users VALUES ('" + user + "')")
        os.system("echo " + msg + " | mail admin@example.com")
        print("saved " + user)
        try:
            self.conn.commit()
        except:
            pass

    def unused_helper(self):
        x = 1
        return
        x = 2
        print(x)
