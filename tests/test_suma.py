from unittest import TestCase
from helpers.suma import suma_int

#los test se corren de esta manera : python -m unittest

class suma_intTest(TestCase):
    def test_suma_int_ok(self):
        rta = suma_int(1, 2)
        self.assertEquals(rta, 3)
        rta = suma_int(10, 2)
        self.assertEquals(rta, 12)
        rta = suma_int(1, 20.1)
        self.assertEquals(rta, 21)
        self.assertEquals(type(rta), int)

    def test_suma_int_with_str(self):
        with self.assertRaises(TypeError):
            suma_int(1, "pepe")