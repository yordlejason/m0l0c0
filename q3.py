

''' Q3-3 -- didn't work on it
For each site, compute the unique number of users whose last visit (found in the original data set) was to that site. For instance, user "LC3561"'s last visit is to "N0OTG" based on timestamp data. Based on this measure, what are top three sites? (hint: site "3POLC" is ranked at 5th with 28 users whose last visit in the data set was to 3POLC; simply provide three pairs in the form (site_id, number of users).)
'''



import pandas as pd
from sqlalchemy import create_engine

class Solution:
    def __init__(self, filename='sample2.csv'):
        self._df = pd.read_csv('sample2.csv')
        self._df['ts'] = self._df['ts'].astype('datetime64[ns]')
        self._engine = create_engine('sqlite://', echo=False)
        self._df.to_sql('db', con=self._engine)

    def query(self, cmd):
        return self._engine.execute(cmd).fetchall()

    ''' Q3-1
    Consider only the rows with country_id = "BDV" (there are 844 such rows). For each site_id, we can compute the number of unique user_id's found in these 844 rows. Which site_id has the largest number of unique users? And what's the number?
    '''
    def getMaxUniqueUser(self, cid='BDV'):
        cmd = '''SELECT site_id, COUNT(user_id)
        FROM db
        WHERE country_id = "{0}"
        GROUP BY site_id
        ORDER BY COUNT(user_id) DESC
        LIMIT 1
        '''.format(cid)
        return self._engine.execute(cmd).fetchall()

    ''' Q3-2
    Between 2019-02-03 00:00:00 and 2019-02-04 23:59:59, there are four users who visited a certain site more than 10 times. Find these four users & which sites they (each) visited more than 10 times. (Simply provides four triples in the form (user_id, site_id, number of visits) in the box below.)
    '''
    def getNvisitedUsers(self, start='2019-02-03 00:00:00', end='2019-02-04 23:59:59', least_number_of_visits=10):
        cmd = '''SELECT site_id, user_id, COUNT(user_id)
        FROM db
        WHERE ts >= '{0}' AND '{1}' <= ts
        GROUP BY site_id, user_id
        HAVING COUNT(user_id) > {2}
        '''.format(start, end, least_number_of_visits)
        return self._engine.execute(cmd).fetchall()

    ''' Q3-4
    For each user, determine the first site he/she visited and the last site he/she visited based on the timestamp data. Compute the number of users whose first/last visits are to the same website. What is the number?
    '''
    def countSameEndToEndVisits(self):
        cmd = '''
        WITH sdb AS (
            SELECT user_id, site_id, MIN(ts) ts
            FROM db
            GROUP BY user_id
        ) INNER JOIN ON user_id = db.user_id AND ts = db.ts,
        WITH edb AS (
            SELECT user_id, site_id, MAX(ts) ts
            FROM db
            GROUP BY user_id
        ) INNER JOIN ON user_id = db.user_id AND ts = db.ts
        SELECT sdb.user_id, sdb.site_id
        FROM sdb INNER JOIN edb ON sdb.user_id = edb.user_id AND sdb.site_id = edb.site_id
        '''
        return self._engine.execute(cmd).fetchall()
