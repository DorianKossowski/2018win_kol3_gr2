# https://github.com/danpisq/kol1_gr2

import unittest
import elements
import plane

class test_flight(unittest.TestCase):

	def setUp(self):
		self.test_environment = elements.Environment()
		self.test_plane = plane.Plane()

	def test_plane_init(self):
		self.assertEqual(self.test_plane.current_angle, 90)
		self.assertEqual(self.test_plane.set_angle, 90)

	def test_plane_correction(self):
		self.test_plane.current_angle = 100
		self.assertEqual(self.test_plane.correction(), 20*-1)
		self.test_plane.current_angle = 0
		self.assertEqual(self.test_plane.correction(), 20*1)

	def test_plane_is_crashed(self):
		self.test_plane.current_angle = 50
		self.assertEqual(self.test_plane.is_crashed(), 0)
		self.test_plane.current_angle = 200
		self.assertEqual(self.test_plane.is_crashed(), 1)