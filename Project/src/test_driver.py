## @file test_driver.py
#  @author Mohammad Omar Zahir, zahirm1
#  @brief Test cases for the various python modules in Assignment 2
#  @date Feb 16, 2021
#  @details

import pytest
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot
import math

g = 9.81


def Fx(t):
    return 0


def Fy(t):
    return -g * 8


def Fx2(t):
    return 10


def Fy2(t):
    return -g * 16


epsilon = 0.0001


class TestCircleT:

    def setup_method(self, method):
        self.circle1 = CircleT(1, 1, 1, 1)
        self.circle2 = CircleT(-100, -10, 5, 10)

    def tear_down(self, method):
        self.circle1 = None
        self.circle2 = None

    def test_xcoord(self):
        assert self.circle1.cm_x() == 1

    def test_xcoord2(self):
        assert self.circle2.cm_x() == -100

    def test_ycoord(self):
        assert self.circle1.cm_y() == 1

    def test_ycoord2(self):
        assert self.circle2.cm_y() == -10

    def test_mass(self):
        assert self.circle1.mass() == 1

    def test_mass2(self):
        assert self.circle2.mass() == 10

    def test_m_inert(self):
        assert self.circle1.m_inert() == 0.5

    def test_m_inert2(self):
        assert self.circle2.m_inert() == 125

    # Exception Cases
    def test_ValueError(self):
        with pytest.raises(ValueError):
            CircleT(1, 1, 0, 1)

    def test_Value_Error2(self):
        with pytest.raises(ValueError):
            CircleT(1, 1, 1, 0)


class TestTriangleT:

    def setup_method(self, method):
        self.triangle1 = TriangleT(1, 1, 1, 1)
        self.triangle2 = TriangleT(1000, -2500, 7, 9)

    def tear_down(self, method):
        self.triangle1 = None
        self.triangle2 = None

    def test_xcoord(self):
        assert self.triangle1.cm_x() == 1

    def test_xcoord2(self):
        assert self.triangle2.cm_x() == 1000

    def test_ycoord(self):
        assert self.triangle1.cm_y() == 1

    def test_ycoor2(self):
        assert self.triangle2.cm_y() == -2500

    def test_mass(self):
        assert self.triangle1.mass() == 1

    def test_mass2(self):
        assert self.triangle2.mass() == 9

    def test_m_inert(self):
        assert self.triangle1.m_inert() == 1 / 12

    def test_m_inert2(self):
        assert self.triangle2.m_inert() == 147 / 4

    # Exception Cases
    def test_ValueError(self):
        with pytest.raises(ValueError):
            TriangleT(1, 1, 0, 1)

    def test_ValueError2(self):
        with pytest.raises(ValueError):
            TriangleT(1, 1, 1, 0)


class TestBodyT:

    def setup_method(self, method):
        self.body1 = BodyT([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
        self.body2 = BodyT([0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 4])

    def tear_down(self, method):
        self.body1 = None
        self.body2 = None

    def test_cmx1(self):
        assert self.body1.cm_x() == 110 / 42

    def test_cmx2(self):
        assert self.body2.cm_x() == 0

    def test_cmy1(self):
        assert self.body1.cm_y() == 278 / 42

    def test_cmy2(self):
        assert self.body2.cm_y() == 0

    def test_mass1(self):
        assert self.body1.mass() == 42

    def test_mass2(self):
        assert self.body2.mass() == 10

    def test_m_inert1(self):
        assert abs(self.body1.m_inert() - 103.809523) < epsilon

    def test_m_inert2(self):
        assert self.body2.m_inert() == 0

    # Exception Cases
    def test_ValueError(self):
        with pytest.raises(ValueError):
            BodyT([1, 2], [1, 3, 4], [1, 2])

    def test_ValueError2(self):
        with pytest.raises(ValueError):
            BodyT([1, 2], [1, 3], [0, 2])


class TestSceneT():

    def setup_method(self, method):
        self.circle1 = CircleT(1, 2, 4, 9)
        self.triangle1 = TriangleT(2, 7, 3, 4)
        self.scene1 = Scene(self.circle1, Fx, Fy, 0, 0)
        self.scene2 = Scene(self.triangle1, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.circle1 = None
        self.triangle1 = None
        self.scene1 = None
        self.scene = None

    def test_get_shape(self):
        assert self.scene1.get_shape() == self.circle1

    def test_get_shape2(self):
        assert self.scene2.get_shape() == self.triangle1

    def test_get_unbal_forces(self):
        assert self.scene1.get_unbal_forces() == (Fx, Fy)

    def test_get_init_velo(self):
        assert self.scene1.get_init_velo() == (0, 0)

    def test_set_shape(self):
        self.scene1.set_shape(self.triangle1)
        assert self.scene1.get_shape() == self.triangle1

    def test_set_unbal_forces(self):
        self.scene1.set_unbal_forces(Fx2, Fy2)
        assert self.scene1.get_unbal_forces() == (Fx2, Fy2)

    def test_set_init_velo(self):
        self.scene1.set_init_velo(2, 10)
        assert self.scene1.get_init_velo() == (2, 10)

    def test_sim(self):
        t, wsol = self.scene1.sim(5, 3)
        t_expec = [0, 2.5, 5]
        wsol_expec = [[1, 2, 0, 0], [1, -25.25, 0, -21.8], [1, -107, 0, -43.6]]

        for i in range(len(t)):
            if t_expec[i] == 0:
                assert t[i] == t_expec[i]
            else:
                assert (t[i] - t_expec[i]) / t_expec[i] < epsilon

        for j in range(len(wsol)):
            for i in range(len(wsol[j])):
                if wsol_expec[j][i] == 0:
                    assert wsol[j][i] == wsol_expec[j][i]
                else:
                    assert (wsol[j][i] - wsol_expec[j][i]) / wsol_expec[j][i] < epsilon

    def test_sim2(self):
        t, wsol = self.scene2.sim(4, 5)
        t_expec = [0.0, 1.0, 2.0, 3.0, 4.0]
        wsol_expec = [[2, 7, 0, 0], [2, -2.81, 0, -19.62], [2, -32.24, 0, -39.24],
                      [2, -81.29, 0, -58.86], [2, -149.96, 0, -78.48]]

        for i in range(len(t)):
            if t_expec[i] == 0:
                assert t[i] == t_expec[i]
            else:
                assert (t[i] - t_expec[i]) / t_expec[i] < epsilon

        for j in range(len(wsol)):
            for i in range(len(wsol[j])):
                if wsol_expec[j][i] == 0:
                    assert wsol[j][i] == wsol_expec[j][i]
                else:
                    assert (wsol[j][i] - wsol_expec[j][i]) / wsol_expec[j][i] < epsilon


class TestPlotT():

    def setup_method(self, method):
        self.circle = CircleT(2, -4, 7, 8)
        self.triangle = TriangleT(-5, -1, 6, 16)
        self.body = BodyT([0, -3, 2, -1], [4, -5, 7, 2], [2, 2, 2, 2])
        self.scene = Scene(self.circle, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.circle = None
        self.triangle = None
        self.body = None
        self.scene = None

    def test_plot(self):
        t, wsol = self.scene.sim(5, 10)
        plot(wsol, t)

        self.scene.set_shape(self.body)
        t, wsol = self.scene.sim(3, 40)
        plot(wsol, t)

        self.scene.set_init_velo(2 * math.cos(math.pi / 2), 2 * math.sin(math.pi / 2))
        self.scene.set_unbal_forces(Fx2, Fy2)
        self.scene.set_shape(self.triangle)
        t, wsol = self.scene.sim(2, 30)
        plot(wsol, t)
