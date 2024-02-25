#!/usr/bin/python3
''' test file of base.py script
Unitests of class Base:
TestBaseIntialization
'''
from unittest import TestCase, main
from models.base import Base


class TestBaseIntialization(TestCase):
	'''Unit tests for intialization objects from Base'''

	def test_no_arg(self):
		b1 = Base()
		b2 = Base()
		self.assertEqual(b1.id, b2.id - 1)

	def test_three_objects(self):
		b1 = Base()
		b2 = Base()
		b3 = Base()
		self.assertEqual(b1.id, b3.id - 2)

	def test_pass_None_id(self):
		b1 = Base(None)
		b2 = Base(None)
		self.assertEqual(b1.id, b2.id - 1)

	def test_pass_unique_id(self):
		unique_id = Base(12).id
		self.assertEqual(unique_id, 12)

	def test_nb_instances_after_unique_id(self):
		b1 = Base()
		b2 = Base(12)
		b3 = Base()
		self.assertEqual(b1.id, b3.id - 1)

	def test_change_id_public(self):
		b = Base(12)
		b.id = 15
		self.assertEqual(15, b.id)

	def test_nb_instances_private(self):
		with self.assertRaises(AttributeError):
			print(Base(12).__nb_instances)

	def test_pass_str_id(self):
		self.assertEqual("hello", Base("hello").id)

	def test_pass_float_id(self):
		self.assertEqual(5.5, Base(5.5).id)

	def test_pass_complex_id(self):
		self.assertEqual(complex(5), Base(complex(5)).id)

	def test_pass_dict_id(self):
		self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

	def test_pass_bool_id(self):
		self.assertEqual(True, Base(True).id)

	def test_pass_list_id(self):
		self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

	def test_pass_tuple_id(self):
		self.assertEqual((1, 2), Base((1, 2)).id)

	def test_pass_set_id(self):
		self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

	def test_pass_frozenset_id(self):
		self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

	def test_pass_range_id(self):
		self.assertEqual(range(5), Base(range(5)).id)

	def test_pass_bytes_id(self):
		self.assertEqual(b'Python', Base(b'Python').id)

	def test_pass_bytearray_id(self):
		self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

	def test_pass_memoryview_id(self):
		self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

	def test_pass_inf_id(self):
		self.assertEqual(float('inf'), Base(float('inf')).id)

	def test_pass_NaN_id(self):
		self.assertNotEqual(float('nan'), Base(float('nan')).id)

	def test_pass_two_args(self):
		with self.assertRaises(TypeError):
			Base(1, 2)


if __name__ == '__main__':
	main()
