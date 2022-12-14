import unittest
from pathlib import Path

from src import solution



class AoC_2022_Puzzle_2_Tests(unittest.TestCase):


	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_score_of_shape_thrown(self):
		self.assertEqual(solution.get_score_of_your_throw("X"), 1) #rock
		self.assertEqual(solution.get_score_of_your_throw("Y"), 2) #paper
		self.assertEqual(solution.get_score_of_your_throw("Z"), 3) #scissors


	def test_round_result_scoring(self):
		points_loss = 0
		points_draw = 3
		points_win = 6
																									#you	opp
		self.assertEqual(solution.determine_num_points_from_round_result("X", "A"), points_draw) 	#R		R
		self.assertEqual(solution.determine_num_points_from_round_result("X", "B"), points_loss) 	#R		P
		self.assertEqual(solution.determine_num_points_from_round_result("X", "C"), points_win) 	#R		S
		self.assertEqual(solution.determine_num_points_from_round_result("Y", "A"), points_win) 	#P		R
		self.assertEqual(solution.determine_num_points_from_round_result("Y", "B"), points_draw) 	#P		P
		self.assertEqual(solution.determine_num_points_from_round_result("Y", "C"), points_loss) 	#P		S
		self.assertEqual(solution.determine_num_points_from_round_result("Z", "A"), points_loss) 	#S		R
		self.assertEqual(solution.determine_num_points_from_round_result("Z", "B"), points_win) 	#S		P
		self.assertEqual(solution.determine_num_points_from_round_result("Z", "C"), points_draw) 	#S		S

	def test_calc_final_score_of_round(self):
		self.assertEqual(solution.calc_score_of_round("A Y"), 8)

	def test_calc_your_total_score(self):
		self.assertEqual(solution.calc_your_total_score(self.data), 15)

	def test_get_your_throw_from_opp_throw_and_round_result(self):
		rock = "X"
		paper = "Y"
		scissors = "Z"

																											#opp	res
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("A", "X"), scissors) 		#R		L
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("B", "X"), rock) 			#P		L
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("C", "X"), paper) 			#S		L
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("A", "Y"), rock) 			#R		D
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("B", "Y"), paper) 			#P		D
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("C", "Y"), scissors) 		#S		D
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("A", "Z"), paper) 			#R		W
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("B", "Z"), scissors) 		#P		W
		self.assertEqual(solution.get_your_throw_from_opp_throw_and_round_result("C", "Z"), rock) 			#S		W

	def test_modify_round_for_adjusted_cypher(self):
		self.assertEqual(solution.modify_round_for_adjusted_cypher("A Y"), "A X")

	def test_adjust_data_for_new_cypher(self):
		exp_result = ["A X", "B X", "C X"]
		self.assertEqual(solution.adjust_data_for_new_cypher(self.data), exp_result)