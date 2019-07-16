# -*- coding: utf-8 -*-
import sys


def cal_sdkp(array):
    array_now = [[0 for _ in range(9)] for _ in range(9)]
    cel_cons = input_numbers(array)
    for i in range(9):
        for j in range(9):
            array_now[i][j] = cel_cons[i][j].number
    print("01", array_now[0][1])
    is_not_complete = True
    loop_count = 0
    loop_more_count = 0
    while is_not_complete:
        print(array_now)
        print(loop_count)
        for i in range(9):
            for j in range(9):
                cel_cons[i][j].check_s_area(array_now)
                cel_cons[i][j].check_row(array_now)
                cel_cons[i][j].check_column(array_now)
                cel_cons[i][j].check_complete()
        complete_count = 0

        if loop_more_count == 100:
            pass

        for i in range(9):
            for j in range(9):
                array_now[i][j] = cel_cons[i][j].number
                if not cel_cons[i][j].array_possibility[0]:
                    complete_count += 1

        if complete_count == 0:
            is_not_complete = False
        loop_count += 1
        loop_more_count += 1
    print("COMPLETE")
    return array_now


def input_numbers(array):
    cel_cons = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if array[i][j] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                cel_cons[i][j] = CellSd(i, j, array[i][j])
            else:
                print("Error")
                sys.exit()
    return cel_cons


def re_to_ab(re_l, re_s):
    ab_x = rel_to_ab_x(re_l) * 3 + rel_to_ab_x(re_s)
    ab_y = rel_to_ab_y(re_l) * 3 + rel_to_ab_y(re_s)
    return ab_x, ab_y


def rel_to_ab_x(number):
    x = number // 3
    return x


def rel_to_ab_y(number):
    y = number % 3
    return y


class CellSd:

    def __init__(self, re_l, re_s, number):
        self.number = number
        self.re_position_l = re_l
        self.re_position_s = re_s
        ab_xy = re_to_ab(re_l, re_s)
        self.ab_position_x = ab_xy[0]
        self.ab_position_y = ab_xy[1]
        self.array_possibility = [True for _ in range(10)]
        if number != 0:
            self.array_possibility[0] = True
        else:
            self.array_possibility[0] = False

    def turn_false(self, number):
        if number != 0:
            self.array_possibility[number] = False

    def check_complete(self):
        count = 0
        number = 0
        for i in range(10):
            if self.array_possibility[i]:
                count += 1
                number = i
        if count == 1 and number != 0:
            self.array_possibility[0] = True
            self.number = number
            print("fil", self.re_position_l, self.re_position_s, "=", self.number)
        elif count == 0:
            print(self.re_position_l, self.re_position_s, "has not any possibility :", self.array_possibility)
            sys.exit()

    def check_s_area(self, array):
        number_s_area = 0
        for i in range(9):
            if i == self.re_position_s:
                pass
            else:
                number_s_area = array[self.re_position_l][i]
            if number_s_area != 0:
                if number_s_area == self.number:
                    pass
                else:
                    self.turn_false(number_s_area)

    def check_row(self, array):
        for i in range(3):
            for j in range(3):
                x = rel_to_ab_x(self.re_position_l) * 3 + i
                y = rel_to_ab_x(self.re_position_s) * 3 + j
                if x == self.re_position_l and y == self.re_position_s:
                    pass
                else:
                    number_s_area = array[x][y]
                    if number_s_area != 0:
                        if number_s_area == self.number:
                            pass
                        else:
                            self.turn_false(number_s_area)

    def check_column(self, array):
        for i in range(3):
            for j in range(3):
                x = rel_to_ab_y(self.re_position_l) + i * 3
                y = rel_to_ab_y(self.re_position_s) + j * 3
                if x == self.re_position_l and y == self.re_position_s:
                    pass
                else:
                    number_s_area = array[x][y]

                    if number_s_area != 0:
                        if number_s_area == self.number:
                            pass
                        else:
                            self.turn_false(number_s_area)
