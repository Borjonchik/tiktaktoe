from tiktaktoe import (
    five_mark_check,
    create_game_area,
    set_mark_position,
    check_user_position,
    win_check,
    full_check
)

import unittest


class TestGamse(unittest.TestCase):
    """
    Тесты для игры tiktaktoe
    """
    def sutUp(self):
        pass

    def test_five_mark_check(self):
        temp = "XXXXX      "
        mark = "X"
        self.assertTrue(five_mark_check(temp, mark))

        temp = "OOOOO      "
        mark = "O"
        self.assertTrue(five_mark_check(temp, mark))

        temp = "OOOO      "
        mark = "O"
        self.assertFalse(five_mark_check(temp, mark))

        temp = ""
        mark = "O"
        self.assertFalse(five_mark_check(temp, mark))

        temp = "OOOOO      "
        mark = "X"
        self.assertFalse(five_mark_check(temp, mark))

    def test_create_game_area(self):
        count_row = 10
        game_area_test = [i for i in range(count_row*count_row)]
        self.assertEqual(create_game_area(count_row), game_area_test)

        game_area_test = [i for i in range(1**2)]
        count_row = -1
        self.assertEqual(create_game_area(count_row), game_area_test)

    def test_create_game_area_negative(self):
        # count_row = "f"
        # self.assertRaises(ValueError, create_game_area(count_row))

        try:
            count_row = None
            create_game_area(count_row)
        except TypeError as err:
            self.assertIsNot(TypeError, err)

    def test_set_mark_position(self):
        game_area = [i for i in range(100)]
        mark = "X"
        pos = 0

        self.assertEqual(set_mark_position(mark, game_area, pos), True)

        game_area = []
        mark = "X"
        pos = 0

        self.assertEqual(set_mark_position(mark, game_area, pos), False)

        game_area = [i for i in range(100)]
        mark = ""
        pos = 0

        self.assertEqual(set_mark_position(mark, game_area, pos), False)

        game_area = [i for i in range(100)]
        mark = "X"
        pos = -1

        self.assertEqual(set_mark_position(mark, game_area, pos), False)

        game_area = [i for i in range(100)]
        game_area[0] = "X"
        mark = "X"
        pos = 0

        self.assertEqual(set_mark_position(mark, game_area, pos), False)

    def test_check_user_position(self):
        game_area = [i for i in range(100)]
        mark = "X"
        pos = 0

        self.assertEqual(check_user_position(pos, 10, mark, game_area), True)

        game_area = [i for i in range(100)]
        mark = "O"
        pos = 0

        self.assertEqual(check_user_position(pos, 10, mark, game_area), True)

        game_area = [i for i in range(100)]
        mark = "X"
        pos = -1

        self.assertEqual(check_user_position(pos, 10, mark, game_area), False)

        game_area = [i for i in range(100)]
        game_area[0] = "X"
        mark = "X"
        pos = 0

        self.assertEqual(check_user_position(pos, 10, mark, game_area), False)

    def test_full_check(self):
        game_area = [i for i in range(100)]

        self.assertEqual(full_check(game_area), False)

        for i in range(0, 100, 2):
            game_area[i] = "X"
            game_area[i+1] = "O"

        self.assertEqual(full_check(game_area), True)

    def test_win_check_hor(self):
        """
        тестирование проверки победной комбинации по горизонтали
        """
        game_area = [numb for numb in range(10 * 10)]

        self.assertEqual(win_check(game_area, "X", 10, 1), False)

        game_area[0] = "X"
        game_area[1] = "X"
        game_area[2] = "X"
        game_area[3] = "X"

        self.assertEqual(win_check(game_area, "X", 10, 3), False)

        game_area[4] = "X"
        self.assertEqual(win_check(game_area, "X", 10, 4), True)
        self.assertEqual(win_check(game_area, "O", 10, 4), False)

    def test_win_check_ver(self):
        """
        тестирование проверки победной комбинации по вертикали
        """
        game_area = [numb for numb in range(10 * 10)]
        game_area[0] = "X"
        game_area[10] = "X"
        game_area[20] = "X"
        game_area[30] = "X"

        self.assertEqual(win_check(game_area, "X", 10, 30), False)
        game_area[40] = "X"
        self.assertEqual(win_check(game_area, "X", 10, 40), True)

    def test_win_check_diag(self):
        """
        тестирование проверки победной комбинации по главной диагонали
        """
        game_area = [numb for numb in range(10 * 10)]
        game_area[0] = "X"
        game_area[11] = "X"
        game_area[22] = "X"
        game_area[33] = "X"

        self.assertEqual(win_check(game_area, "X", 10, 33), False)
        game_area[44] = "X"
        self.assertEqual(win_check(game_area, "X", 10, 44), True)

    def test_win_check_obr_diag(self):
        """
        тестирование проверки победной комбинации по обратной диагонали
        """
        game_area = [numb for numb in range(10 * 10)]
        game_area[9] = "O"
        game_area[18] = "O"
        game_area[27] = "O"
        game_area[36] = "O"

        self.assertEqual(win_check(game_area, "O", 10, 36), False)
        game_area[45] = "O"
        self.assertEqual(win_check(game_area, "O", 10, 45), True)


if __name__ == "__main__":
    unittest.main()
