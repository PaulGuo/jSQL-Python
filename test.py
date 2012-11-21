#!/usr/bin/env python
# coding=utf-8

import re

class Db(object):
    def __init__(self):
        self.get = self._get
        self.query = self._query
        self.execute = self._execute 

    def _get(self, s):
        print('GET: %s' % s)

    def _query(self, s):
        print('QUERY: %s' % s)

    def _execute(self, s):
        print('EXECUTE: %s' % s)

if __name__ == '__main__':
    q = Query('test_table')
    print('''Query wrapper for tornado's test case''')

    print q.find(cheat = True)
    print q.select(cheat = True)
    print q.count(cheat = True)
    print q.delete(cheat = True)
    print q.save(cheat = True)
    print q.add(cheat = True)
    print q.grasp('SELECT * FROM lab WHERE name === "Hi"').find(cheat = True)
    print q.limit(10).query('SELECT * FROM lab WHERE name === "Hi" LIMIT 15, 25')
    print q.table('selected_table') \
            .field('name, age, id') \
            .where('name = "tom"') \
            .limit(33, 44) \
            .group('name') \
            .having('age > 13') \
            .join('LEFT JOIN account.id = id') \
            .select(cheat = True)

    print q.table('selected_table').data({'a': 1, 'b': 2}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2, 'c': "'中文' 123 Abc"}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2, 'c': "'中文'"}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2, 'c': "He's tom."}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2, 'c': "He's '%s'." % 'tom'}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2, 'c': "He's %s." % 'tom'}).add(cheat = True)
    print q.table('selected_table').data({'a': 1, 'b': 2}).where('name = "tom"').save(cheat = True)
    print q.table('selected_table').where('name = "tom"').delete(cheat = True)
    print q.table('selected_table').where('name LIKE "%tom%"').find(cheat = True)
    print q.table('selected_table').where("name = '%s'" % "tom's cat.").find(cheat = True)
    print q.table('selected_table').where('name = "tom"').prepend('where', 'value').prepend('where', 'A = B').find(cheat = True)
    print q.field('name, age').where('name LIKE "%tom%"').find(cheat = True)
    # print dir(q)
    print q._Query__valuefix('He\'s tom.')

