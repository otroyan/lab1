import unittest
import simple_eratosfen as tested

class TestSimpleEratosfen(unittest.TestCase):

    def test_is_simple(self):
        print('test1')
        self.assertEqual(tested.is_simple(0), False,
                         "Zero is not a prime number")

        num_to_test = 3
        self.assertEqual(tested.is_simple(num_to_test), True,
                         "{} is prime".format(num_to_test))

        num_to_test = 4
        self.assertEqual(tested.is_simple(num_to_test), False,
                         "{} is not prime".format(num_to_test))

    def test_max_simple(self):
        func_to_test = [tested.max_simple1, tested.max_simple2,
                        tested.max_simple3]
        lst_to_test = [10, 4, 1, 7]
        expected = 7
        for func in func_to_test:
            result = func(lst_to_test)
            self.assertEqual(result, expected,
                         "{}: Max prime value is incorrect list is {}"
                         ", found value is {}, expected is "
                         "{}".format(func.__name__,lst_to_test,
                                     result, expected))

    def test_get_lst_of_simple(self):
        print('test3')
        boundary_num = 43
        expected = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        self.assertListEqual(tested.get_lst_of_simple(boundary_num), expected)

        boundary_num = 44
        self.assertListEqual(tested.get_lst_of_simple(boundary_num), expected)

        boundary_num = 1
        expected = [1]
        self.assertListEqual(tested.get_lst_of_simple(boundary_num), expected)

        boundary_num = 0
        self.assertEqual(tested.get_lst_of_simple(boundary_num), None)

    def test_get_lst_of_complicated(self):
        print('test4')
        boundary_num = 14
        expected = [4, 6, 8, 9, 10, 12, 14]
        self.assertListEqual(sorted(tested.get_lst_of_complicated(boundary_num)),
                             expected)

        expected = [4, 6, 8, 9, 10, 12, 14, 15, 16]
        boundary_num = 17
        self.assertListEqual(sorted(tested.get_lst_of_complicated(boundary_num)),
                             expected)

        boundary_num = 3
        self.assertEqual(tested.get_lst_of_complicated(boundary_num), None)


        boundary_num = 0
        self.assertEqual(tested.get_lst_of_complicated(boundary_num), None)


if __name__ == '__main__':
    unittest.main()
