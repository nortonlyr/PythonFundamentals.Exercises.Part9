import unittest
import os
import hashlib
import json_helper


class JsonHelperTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._json_stubs = [
            {
                "name": "Mario",
                "neutral_special": "Fireball",
                "side_special": "Cape",
                "up_special": "Super Jump Punch",
                "down_special": "F.L.U.D.D.",
                "final_smash": "Mario Finale"
            },
            {
                "name": "Link",
                "neutral_special": "Bow and Arrows",
                "side_special": " Boomerang",
                "up_special": " Spin Attack",
                "down_special": "Remote Bomb",
                "final_smash": "Ancient Bow and Arrow"
            }
        ]

    def test_read_json(self):
        expected = self._json_stubs[0]
        file_path = os.path.join('./', 'data', 'super_smash_bros', 'mario.json')
        actual = json_helper.read_json(file_path)
        self.assertEqual(expected, actual)

    def test_read_all_json_files(self):
        expected = self._json_stubs
        file_path = os.path.join('./', 'data', 'super_smash_bros')
        actual = json_helper.read_all_json_files(file_path)
        self.assertEqual(expected, actual)

    def _getmd5(self, file):
        hasher = hashlib.md5()
        with open(file, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def test_write_pickle(self):

        expected_md5 = self._getmd5('golden_output.pickle')

        file_contents = self._json_stubs
        json_helper.write_pickle("output.pickle", file_contents)
        actual_md5 = self._getmd5('output.pickle')

        print(f"{expected_md5} : {actual_md5}")
        self.assertEqual(expected_md5, actual_md5)

    def test_load_pickle(self):
        expected = self._json_stubs

        file_path = os.path.join('./', 'golden_output.pickle')
        actual = json_helper.load_pickle(file_path)

        self.assertEqual(expected, actual)
