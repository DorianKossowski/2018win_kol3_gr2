# https://github.com/danpisq/kol1_gr2

import unittest
import elements
import plane
from types import GeneratorType

class test_flight(unittest.TestCase):

	def setUp(self):
		self.test_environment = elements.Environment()
		self.test_plane = plane.Plane()

	def test_plane_init(self):
		self.assertEqual(self.test_plane.current_angle, 90)
		self.assertEqual(self.test_plane.set_angle, 90)

	def test_plane_correction_negative(self):
		self.test_plane.current_angle = 100
		self.assertEqual(self.test_plane.correction(), 20*-1)

	def test_plane_correction_positive(self):
		self.test_plane.current_angle = 0
		self.assertEqual(self.test_plane.correction(), 20*1)

	def test_plane_is_crashed(self):
		self.test_plane.current_angle = 50
		self.assertEqual(self.test_plane.is_crashed(), 0)

	def test_plane_not_crashed(self):
		self.test_plane.current_angle = 200
		self.assertEqual(self.test_plane.is_crashed(), 1)

	def test_turbulence(self):
		self.test_environment.turbulence()
		self.assertEqual(type(self.test_environment.plane.current_angle), float)

	def test_flight_generator(self):
		self.assertEqual(type(self.test_environment.flight()), GeneratorType)

	def test_flight_string(self):
		check_str = next(self.test_environment.flight())
		self.assertEqual(type(check_str), str)

	def test_sign(self):
		self.test_plane.current_angle = 120
		self.assertLess(self.test_plane.correction(), 0)
		self.test_plane.current_angle = 20
		self.assertGreater(self.test_plane.correction(), 0)

	def test_correction_difference(self):
		self.assertNotAlmostEqual(self.test_plane.current_angle, self.test_plane.correction())