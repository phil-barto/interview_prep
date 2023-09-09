
from binary_search.binary_search_rotated import find_min_rotated


class TestFindMinRotated:
    def test_find_min_rotated_mid(self):
        ex_list = [5, 6, 1, 2, 3, 4]
        assert find_min_rotated(ex_list) == 2

    def test_find_min_rotated_not_rotated(self):
        ex_list = [1, 2, 3, 4]
        assert find_min_rotated(ex_list) == 0
    
    def test_find_min_rotated__empty_list(self):
        ex_list = [0]
        assert find_min_rotated(ex_list) == 0

    def test_find_min_rotated__last_value_rotated(self):
        ex_list = [1, 2, 3, 5, 8, 0]
        assert find_min_rotated(ex_list) == 5
