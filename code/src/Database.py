import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('path/to/database.db', timeout=0)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS data (
            tagText TEXT,
            machineName TEXT,
            decrypt TEXT,
            open TEXT,
            trys TEXT,
            ctx TEXT,
            pas TEXT,
            token TEXT
            );'''
        )
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS keys (
            key TEXT
            );'''
        )
        self.conn.commit()
    
    def insert_data(self, tagText, machineName, code, pas, tok):
        self.cursor.execute('''DELETE FROM data''')
        self.cursor.execute(
            '''INSERT INTO data (tagText, machineName, decrypt, open, trys, ctx, pas, token)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', (tagText, machineName, code, "false", '0', "None", pas, tok)
        )
        self.conn.commit()
    
    def update_open(self, io):
        self.cursor.execute(
            '''UPDATE data SET open = ?''', (io,)
        )
        self.conn.commit()
    
    def inc_trys(self):
        self.cursor.execute(
            '''UPDATE data SET trys = ?''', (str(int(self.get_trys())+1),)
        )
        self.conn.commit()
        
    def update_ctx(self, io):
        self.cursor.execute(
            '''UPDATE data SET ctx = ?''', (io,)
        )
        self.conn.commit()

    def res_trys(self):
        self.cursor.execute(
            '''UPDATE data SET trys = ?''', ('0',)
        )
        self.conn.commit()

    def edit_tagText(self, new_tagText):
        self.cursor.execute(
            '''UPDATE data SET tagText = ?''', (new_tagText,)
        )
        self.conn.commit()

    def insert_key(self, key):
        self.cursor.execute(
            '''INSERT INTO keys (key)
            VALUES (?);''', (key,)
        )
        self.conn.commit()
        
    def remove_key(self, key):
        self.cursor.execute(
            '''DELETE FROM keys WHERE key = ? ;''', (key,)
        )
        self.conn.commit()
    
    def remove_latest_key(self):
        keys = self.get_keys()
        if keys:
            key_index = len(keys) - 1
            self.cursor.execute(
                '''DELETE FROM keys WHERE rowid = ?''', (key_index + 1,)
            )
            self.conn.commit()
            return True
        return False

    def get_tagText(self):
        self.cursor.execute(
            '''SELECT tagText FROM data;'''
        )
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def get_trys(self):
        self.cursor.execute(
            '''SELECT trys FROM data;'''
        )
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_keys(self):
        self.cursor.execute(
            '''SELECT key FROM keys;'''
        )
        return [key[0] for key in self.cursor.fetchall()]

    def get_machineName(self):
        self.cursor.execute(
            '''SELECT machineName FROM data;'''
        )
        return self.cursor.fetchone()[0]

    def get_decrypt(self):
        self.cursor.execute(
            '''SELECT decrypt FROM data;'''
        )
        return self.cursor.fetchone()[0]

    def get_open(self):
        self.cursor.execute(
            '''SELECT open FROM data;'''
        )
        return self.cursor.fetchone()[0].strip()
    
    def get_ctx(self):
        self.cursor.execute(
            '''SELECT ctx FROM data;'''
        )
        return self.cursor.fetchone()[0].strip()
    
    def get_pass(self):
        self.cursor.execute(
            '''SELECT pas FROM data;'''
        )
        return self.cursor.fetchone()[0].strip()
    
    def get_token(self):
        self.cursor.execute(
            '''SELECT token FROM data;'''
        )
        return self.cursor.fetchone()[0].strip()