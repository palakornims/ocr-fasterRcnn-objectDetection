from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from six.moves import range
import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import string_int_label_map_pb2


def show_string(label_map,
                max_num_classes,
                use_display_name=True):
  categories = []
  list_of_ids_already_added = []

  for item in label_map.item:
    if not 0 < item.id <= max_num_classes:
      logging.info(
        'Ignore item %d since it falls outside of requested '
        'label range.', item.id)
      continue
    if use_display_name and item.HasField('display_name'):
      name = item.display_name
    else:
      name = item.name
    if item.id not in list_of_ids_already_added:
      list_of_ids_already_added.append(item.id)
      categories.append({'id': item.id})
  return categories

def class_string(categories):

  category_index = {}
  for cat in categories:
    category_index[cat['id']] = cat
  return category_index

def compare_string(category_index):
  string_index = []
  for i in category_index:
        if i == {'id': 1}:
          string_index.append('A')
        if i == {'id': 2}:
          string_index.append('B')
        if i == {'id': 3}:
          string_index.append('C')
        if i == {'id': 4}:
          string_index.append('D')
        if i == {'id': 5}:
          string_index.append('E')
        if i == {'id': 6}:
          string_index.append('F')
        if i == {'id': 7}:
          string_index.append('G')
        if i == {'id': 8}:
          string_index.append('H')
        if i == {'id': 9}:
          string_index.append('I')
        if i == {'id': 10}:
          string_index.append('J')
        if i == {'id': 11}:
          string_index.append('K')
        if i == {'id': 12}:
          string_index.append('L')
        if i == {'id': 13}:
          string_index.append('M')
        if i == {'id': 14}:
          string_index.append('N')
        if i == {'id': 15}:
          string_index.append('O')
        if i == {'id': 16}:
          string_index.append('P')
        if i == {'id': 17}:
          string_index.append('Q')
        if i == {'id': 18}:
          string_index.append('R')
        if i == {'id': 19}:
          string_index.append('S')
        if i == {'id': 20}:
          string_index.append('T')
        if i == {'id': 21}:
          string_index.append('U')
        if i == {'id': 22}:
          string_index.append('V')
        if i == {'id': 23}:
          string_index.append('W')
        if i == {'id': 24}:
          string_index.append('X')
        if i == {'id': 25}:
          string_index.append('Y')
        if i == {'id': 26}:
          string_index.append('Z')
        if i == {'id': 27}:
          string_index.append('1')
        if i == {'id': 28}:
          string_index.append('2')
        if i == {'id': 29}:
          string_index.append('3')
        if i == {'id': 30}:
          string_index.append('4')
        if i == {'id': 31}:
          string_index.append('5')
        if i == {'id': 32}:
          string_index.append('6')
        if i == {'id': 33}:
          string_index.append('7')
        if i == {'id': 34}:
          string_index.append('8')
        if i == {'id': 35}:
          string_index.append('9')
        if i == {'id': 36}:
          string_index.append('0')

  return string_index



