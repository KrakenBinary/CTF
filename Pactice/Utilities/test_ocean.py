#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Testing framework
'''
import unittest
import decode_ocean


class TestStringMethods(unittest.TestCase):
    '''Testing class'''
    str_test = 'flagCTF{kr4k3n_B1n4Ry_t3St}'  # do not change!
    str_contains = 'flagCTF{'  # in case you want to check for a flag
    look_for_flag = False

    def looper(self, str_in, str_compare, str_des):
        '''loop for any of the tests'''
        if self.look_for_flag:
            self.assertIn(self.str_contains, str_in)
            print('\n{} pass: {}'.format(str_des, str_in))
        else:
            self.assertEqual(
                str_in,
                str_compare,
                '{}: fail'.format(str_des))
            return str_in

    def test_md5(self):
        '''md5'''
        self.looper(
            decode_ocean.md5(self.str_test),
            '7ccbc0cdc219e16bc2ad8dfd8b1c2a0d',
            'string to md5')

    def test_sh1(self):
        '''docstr'''
        self.looper(
            decode_ocean.sh1(self.str_test),
            '9851e7d6527dc1f15675fc06373dfda0730fe3f8',
            'string to sh1')

    def test_str_to_b64(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_b64(self.str_test),
            'ZmxhZ0NURntrcjRrM25fQjFuNFJ5X3QzU3R9',
            'string to base64')

    def test_b64_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_b64(self.str_test)
        self.looper(
            decode_ocean.b64_to_string(new_str_test),
            self.str_test,
            'base64 to string')

    def test_string_to_b32(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_b32(self.str_test),
            'MZWGCZ2DKRDHW23SGRVTG3S7IIYW4NCSPFPXIM2TOR6Q====',
            'string to base32')

    def test_b32_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_b32(self.str_test)
        self.looper(
            decode_ocean.b32_to_string(new_str_test),
            self.str_test,
            'base32 to string')

    def test_string_to_b16(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_b16(self.str_test),
            '666C61674354467B6B72346B336E5F42316E3452795F743353747D',
            'string to base16')

    def test_b16_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_b16(self.str_test)
        self.looper(
            decode_ocean.b16_to_string(new_str_test),
            self.str_test,
            'base16 to string')

    def test_string_to_a85(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_a85(self.str_test),
            'Ao(mg6W?O%CN;7I1N$Pd0lAgGH!bYL;fmE',
            'string to a85')

    def test_a85_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_a85(self.str_test)
        self.looper(
            decode_ocean.a85_to_string(new_str_test),
            self.str_test,
            'a85 to string')

    def test_string_to_b85(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_b85(self.str_test),
            'W^7?+LsUk4YjQMeGj3l(F>W+cd0%uhQ*?a',
            'string to b85')

    def test_b85_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_b85(self.str_test)
        self.looper(
            decode_ocean.b85_to_string(new_str_test),
            self.str_test,
            'b85 to string')

    def test_string_to_base36(self):
        '''docstr'''
        # new_str_test = decode_ocean.base36_to_string(self.str_test)
        self.looper(
            decode_ocean.string_to_base36('krakenBinary'),
            '2732223524352615502',
            'string to b36')

    def test_string_to_base36(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_base36('krakenbinary')
        self.looper(
            decode_ocean.base36_to_string(new_str_test),
            'krakenbinary',
            'b36 to string')

    def test_string_to_base58(self):
        '''docstr'''
        self.looper(
            decode_ocean.string_to_base58(self.str_test),
            'EqtsFqmtxqPYUx1RH9yHzPoz8cEvWJY7tu2v8',
            'string to b85')

    def test_base58_to_str(self):
        '''docstr'''
        new_str_test = decode_ocean.string_to_base58(self.str_test)
        self.looper(
            decode_ocean.base58_to_string(new_str_test),
            self.str_test,
            'b85 to string')


if __name__ == '__main__':
    unittest.main(verbosity=0)
