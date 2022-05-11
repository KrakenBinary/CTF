#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Testing framework
'''
import unittest
import decode_ocean


class TestStringMethods(unittest.TestCase):
    '''Testing class'''
    str_test = 'flagCTF{kr4k3n_B1n4Ry_t3St}'
    str_contains = 'flagCTF{'
    look_for_flag = False

    def test_md5(self):
        '''docstr'''
        result = decode_ocean.md5(self.str_test)
        self.assertEqual(
            result,
            '7ccbc0cdc219e16bc2ad8dfd8b1c2a0d')
        if self.look_for_flag:
            self.assertIn(self.str_contains, result)

    def test_sh1(self):
        '''docstr'''
        result = decode_ocean.sh1(self.str_test)
        self.assertEqual(
            result,
            '9851e7d6527dc1f15675fc06373dfda0730fe3f8')
        if self.look_for_flag:
            self.assertIn(self.str_contains, result)

    def test_str_to_b64(self):
        '''docstr'''
        result = decode_ocean.string_to_b64(self.str_test)
        self.assertEqual(
            result,
            'ZmxhZ0NURntrcjRrM25fQjFuNFJ5X3QzU3R9')
        if self.look_for_flag:
            self.assertIn(self.str_contains, result)

    def test_b64_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_b64(self.str_test)
        result = decode_ocean.b64_to_string(new_str_test)
        self.assertEqual(result, self.str_test)
        if self.look_for_flag:
            self.assertIn(self.str_contains, result)


if __name__ == '__main__':
    unittest.main()
