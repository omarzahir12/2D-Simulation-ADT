from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot


g = 9.81  # accel due to gravity (m/s^2)
m = 1  # mass (kg)


def Fx(t):
    return 5 if t < 5 else 0


def Fy(t):
    return -g * m if t < 3 else g * m


c = CircleT(1.0, 10.0, 0.5, 1.0)
print(c.cm_x(), c.cm_y(), c.mass(), c.m_inert())

t = TriangleT(1.0, -10.0, 5, 17.5)
print(t.cm_x(), t.cm_y(), t.mass(), t.m_inert())

b = BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, 10])
print(b.cm_x(), b.cm_y(), b.mass(), b.m_inert())
# cm should be (0, 0)

b2 = BodyT([11, 9, 9, 11], [11, 11, 9, 9], [10, 10, 10, 10])
print(b2.cm_x(), b2.cm_y(), b2.mass(), b2.m_inert())
# cm for b2 should be shifted to 10, 10; b.m_inert() should be equal to b2.m_inert()

lst = [c, t, b, b2]
for s in lst:
    print(s.cm_x(), s.cm_y(), s.mass(), s.m_inert())

S = Scene(c, Fx, Fy, 0, 0)

# exercise interface for Scene
S.get_shape()
S.get_unbal_forces()
S.get_init_velo()

# exercise setters for Scene
S.set_shape(c)
S.set_unbal_forces(Fx, Fy)
S.set_init_velo(0, 0)

t, wsol = S.sim(10, 100)

for t1, w1 in zip(t, wsol):
    print("t=", t1, "rx=", w1[0], "ry=", w1[1], "vx=", w1[2], "vy=", w1[3])

# extract ry values
print(wsol[0:, 1])

plot(wsol, t)
