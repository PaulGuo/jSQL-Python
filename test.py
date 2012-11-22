#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 Guokai (benben.cc)
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from Query import *

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
    db = Db()
    q = Query('test_table', db)

    print('''Query wrapper for tornado's test case''')

    print q.find(cheat = True)
    print q.select(cheat = True)
    print q.count(cheat = True)
    print q.delete(cheat = True)
    print q.save(cheat = True)
    print q.add(cheat = True)
    print q.grasp('SELECT * FROM lab WHERE name === "Hi"').find(cheat = True)
    print q.limit(10).query('SELECT * FROM lab WHERE name === "Hi" LIMIT 15, 25')
    print q.limit(10).query('SELECT * FROM lab WHERE name === "Hi"')
    print q.limit(10).order('ID DESC').query('SELECT * FROM lab WHERE name === "Hi" ORDER BY AGE ASC')
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
    print q.grasp('SELECT ArticleTitle, Copyright, ab.AuthID \
        FROM Articles AS b, AuthorArticle AS ab \
        WHERE b.ArticleID=ab.ArticleID AND Copyright<1980 \
        ORDER BY ArticleTitle;').find(cheat = True)
    print q.table('table_a, table_b AS b').field('name, age, sex').where('table_a.name = b.name').find(cheat = True)
    print q.table('table_a AS a, table_b AS b').field('name, age, sex, id AS user_id').where('a.name = b.name').find(cheat = True)
    print q.grasp('SELECT name, age, sex, id AS user_id FROM table_a AS a, table_b AS b WHERE a.name = b.name').find(cheat = True)

