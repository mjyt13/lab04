""" test_quantity_same_elem: В этой функции мы добавили несколько тестов:
Тест 1 проверяет функцию на списках с повторяющимися элементами.
Тест 2 проверяет, что функция возвращает пустой список, если нет повторяющихся элементов.
Тест 3 проверяет случай, когда все элементы одинаковы.
Тест 4 проверяет поведение функции на пустом входе."""

import unittest
def quantity_same_elem(lists):
    same_elems = {}
    same_quan = []
    for list in lists:
        for elem in list:
            if elem not in same_elems:
                same_elems[elem] = 0
            else:
                same_elems[elem] += 1
    for elem in same_elems:
        if same_elems[elem] > 1:
            str_elem = str(elem)
            str_quan = str(same_elems[elem] + 1)
            same_quan.append((str_elem + ' : ' + (str_quan) + ' times '))
    return same_quan

class TestQuantitySameElem(unittest.TestCase):
    def test_quantity_same_elem(self):
        first_list = [8, 8, 90, 1]
        second_list = [90, 1, 11, 8, 43, 1]
        third_list = [124, 77, 1, 8, 90]
        lists = [first_list, second_list, third_list]

        expected_output = ['8 : 4 times ', '90 : 3 times ', '1 : 4 times ']
        self.assertEqual(quantity_same_elem(lists), expected_output)

    def test_empty_lists(self):
        lists = [[], [], []]
        expected_output = []
        self.assertEqual(quantity_same_elem(lists), expected_output)

    def test_no_common_elements(self):
        lists = [[1, 2], [3, 4], [5, 6]]
        expected_output = []
        self.assertEqual(quantity_same_elem(lists), expected_output)

    def test_all_same_elements(self):
        lists = [[1, 1, 1], [1, 1], [1]]
        expected_output = ['1 : 6 times ']
        self.assertEqual(quantity_same_elem(lists), expected_output)

if __name__ == '__main__':
    unittest.main()

