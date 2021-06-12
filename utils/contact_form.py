from re import search as check
from sqlite3 import IntegrityError
from time import time

from aiosqlite import connect

db_path = './db/contacts.sqlite3'
email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


async def add_contact(data):
    async with connect(db_path) as db:
        email = data.get('email')
        name = data.get('name')
        message = data.get('message')

        if await form_validate(email, name):
            name = name.strip().lower()
            if message:
                message = message.strip().lower()
            email = email.strip().lower()

            try:
                await db.execute('''INSERT INTO contacts VALUES(?, ?, ?, ?, ?)''',
                                 (email, name, str([message]), time(), 1))
                await db.commit()
            except IntegrityError:
                await db.execute('''UPDATE contacts SET tried_times = tried_times + 1 WHERE email=?''', (email,))
                await db.commit()
                data = await db.execute('''SELECT tried_times FROM contacts WHERE email=?''', (email,))
                return (await data.fetchall())[0][0]

            return True
        else:
            return False


async def form_validate(email: str, name: str):
    if check(email_regex, email):
        if name:
            for word in name.split():
                if not word.isalpha():
                    return False
            return True
    return False
