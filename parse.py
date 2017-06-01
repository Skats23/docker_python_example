#!/usr/bin/env python2

import requests
import yaml
import json

def fetch_from_url(url):
  '''
  Fetch content from a url and return the text

  >>> r = fetch_from_url('https://raw.githubusercontent.com/necrolyte2/docker_python_example/master/inputs/example.json')
  >>> 'findme' in r
  True
  '''
  return ""

def fetch_from_path(path):
  '''
  Open a file from a filepath and return the text

  >>> r = fetch_from_path('inputs/example.json')
  >>> 'findme' in r
  True
  '''
  return ""

def parse_text(text, text_type):
  '''
  Parse the given text as the text_type which is json or yaml
  Should also validate that text_type is only 'json' or 'yaml'

  >>> parse_text('{"key": "value"}', 'json')
  {u'key': u'value'}
  >>> parse_text('key: value', 'yaml')
  {'key': 'value'}
  >>> parse_text('', 'invalid')
  'invalid text_type given'
  '''
  return ""
