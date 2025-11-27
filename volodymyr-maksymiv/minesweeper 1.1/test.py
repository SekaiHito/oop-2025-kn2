import unittest
import os
import json
from game_logic import GameLogic

class TestMinesweeperLogic(unittest.TestCase):
    
    def setUp(self):

        self.logic = GameLogic()
        self.logic.SCORES_FILE = 'test_scores.json'

    def tearDown(self):

        if os.path.exists('test_scores.json'):
            os.remove('test_scores.json')

    def test_initial_state(self):

        self.assertEqual(self.logic.current_difficulty, 'Легко')
        self.assertTrue(self.logic.first_click)
        self.assertFalse(self.logic.game_over)
        self.assertIsNone(self.logic.start_time)

    def test_difficulty_settings(self):

        self.logic.reset_state('Легко')
        settings = self.logic.get_current_settings()
        self.assertEqual(settings['grid_size'], 7)
        self.assertEqual(settings['mine_percentage'], 0.20)

        self.logic.reset_state('Складно')
        settings = self.logic.get_current_settings()
        self.assertEqual(settings['grid_size'], 12)
        self.assertEqual(settings['mine_percentage'], 0.30)

    def test_mines_calculation(self):

        self.logic.reset_state('Легко')
        mines, total = self.logic.calculate_mines_count()
        self.assertEqual(mines, 10)
        self.assertEqual(total, 49)

        self.logic.reset_state('Складно')
        mines, total = self.logic.calculate_mines_count()
        self.assertEqual(mines, 44)
        self.assertEqual(total, 144)

    def test_timer_logic(self):

        self.assertEqual(self.logic.get_elapsed_time(), 0.0)
        
        self.logic.start_timer()

        self.assertIsNotNone(self.logic.start_time)
        
        elapsed = self.logic.get_elapsed_time()
        self.assertGreaterEqual(elapsed, 0.0)

    def test_score_saving_loading(self):

        self.assertIsNone(self.logic.get_best_score())

        self.logic.save_score(15.5)
        self.assertEqual(self.logic.get_best_score(), 15.5)

        self.logic.save_score(20.0)
        self.assertEqual(self.logic.get_best_score(), 15.5)

        self.logic.save_score(10.0)
        self.assertEqual(self.logic.get_best_score(), 10.0)

if __name__ == '__main__':
    unittest.main()