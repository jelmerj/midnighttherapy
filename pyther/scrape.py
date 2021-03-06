#!/usr/bin/env python
import datetime
import json
import re
import subprocess
import requests

import pathery

TYPE_MAP = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    's': 's',
    'S': 's',
    'f': 't',
    'r': 'X',
    't': '1',
    'u': '!',
    'm': '2',
    'n': '@',
    'g': '3',
    'h': '#',
    'i': '4',
    'j': '$',
    'k': '5',
    'l': '%',
}

def call(command):
  print 'Calling "%s"' % (command,)
  return subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read()[:-1]

def get_problems(days_before=0):
  return [(board['data'], int(board['walls'])) for board in get_boards(days_before)]

def get_graphs(days_before=0):
  return [pathery.Graph(board['data']) for board in get_boards(days_before)]

def get_boards(days_before=0):
  if days_before:
    date = datetime.datetime.today() + datetime.timedelta(hours=3) - datetime.timedelta(days=days_before)
    url = 'www.pathery.com/leaderboard?date=%s' % (date.isoformat()[:10],)
  else:
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    url = 'http://www.pathery.com/a/mapsbydate/' + date_str + '.js'
    r = requests.get(url).text
    board_nums = json.loads(r)
    boards = []
    for board_num in board_nums:
      url = 'http://www.pathery.com/a/map/' + str(board_num) + '.js'
      r = requests.get(url).text
      boards.append(parse_board(json.loads(r)))
    return boards

def parse_board(board):
  code = board.pop('code')
  code = board['code'] = code
  (head, body) = code.split(':')

  head = head.split('.')
  width = int(board['width'])
  height = int(board['height'])
  assert(head[1][0] == 'c'), 'head[1][0] was %s, expected c' % (head[1][0],)
  targets = int(head[1][1:])
  assert(head[2][0] == 'r'), 'head[2][0] was %s, expected r' % (head[2][0],)
  targets = int(head[2][1:])
  assert(head[3][0] == 'w'), 'head[3][0] was %s, expected w' % (head[3][0],)
  assert(int(board['walls']) == int(head[3][1:])), 'board.walls is different from walls in header, %d instead of %d' % (int(board['walls']), int(head[3][1:]))
  assert(head[4][0] == 't'), 'head[4][0] was %s, expected t' % (head[4][0],)
  teleports = int(head[4][1:])

  data = [[' ' for j in range(width)] for i in range(height)]
  i = -1
  j = width - 1
  for item in body.split('.')[:-1]:
    for _ in range(int(item[:-1]) + 1):
      j += 1
      if j >= width:
        j = 0
        i += 1
    type = item[-1]
    assert(type in TYPE_MAP), 'Unexpected type %s' % (type,)
    data[i][j] = TYPE_MAP[type]
  board['data'] = [''.join(row) for row in data]
  return board

if __name__ == '__main__':
  pass
