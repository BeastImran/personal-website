from aiosqlite import connect, IntegrityError
from shortuuid import ShortUUID

short_url_db = '../db/url_short.sqlite3'
uid = ShortUUID()


async def validate_format(data):
    if isinstance(data, dict):
        if 'real_url' in data:
            return data['real_url'].startswith('http')
    return False


async def short_url(data):
    if await validate_format(data):
        async with connect(short_url_db) as db:
            random_id = uid.random(length=8)

            try:
                await db.execute('''INSERT INTO short_urls VALUES(?, ?, ?, ?, ?, ?)''',
                                 (random_id, data['real_url'], 'http://beastimran.com/url/' + random_id, False, 0, 0))

            except IntegrityError:
                random_id = uid.random(length=8)
                await db.execute('''INSERT INTO short_urls VALUES(?, ?, ?, ?, ?, ?)''',
                                 (random_id, data['real_url'], 'http://beastimran.com/url/' + random_id, False, 0, 0))
            await db.commit()
        return uid
    else:
        return False


async def get_real_url(url):
    if '/' in url:
        url = url.rpartition('/')[1]

    async with connect(short_url_db) as db:
        data = await db.execute('''SELECT * FROM short_urls WHERE random_id=?''', url)
        data = await data.fetchall()
        print(data)

        if data[0]:
            return data[0]
    return False
