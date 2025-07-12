import io
import itertools
import random
import string
import unittest
import unittest.mock


class TestMain(unittest.TestCase):

    def test_play_game(self):
        name1 = gen_name()
        name2 = gen_name()
        name3 = gen_name()
        letter = gen_letter()

        def mock_draw(self):
            self.letters.append(letter)
            return letter

        tests = [
                ("1", (name1, ), [letter]*7),
                ("1", (name1, ), ['']+[letter]*8),
                ("1", (name1, ), [letter, letter, "3", letter, letter, letter*3]),
                ("2", (name1, name2), [letter]*13),
                ("2", (name1, name2), ['']+[letter]*13),
                ("3", (name1, name2, name3), [letter]*19),
                ]

        for test in tests:
            commands = list(itertools.chain(*test))
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                    unittest.mock.patch("builtins.input", side_effect=commands), \
                    unittest.mock.patch('player.Player.drawLetter', mock_draw):
                import main
                try:
                    main.main()
                except StopIteration:
                    self.fail("I got stuck while trying to play your game. This "
                            "usually means that you had too many input calls"
                            "or you did not set them up in the correct "
                            "order. Make sure you test out your game manually "
                            "to ensure it follows the pattern outlined in the "
                            "instructions.\n\nThese are the inputs I entered:\n\n"
                            f"Number of players: {test[0]}\n"
                            f"Names of each player: {[name for name in test[1]]}\n"
                            f"Attempts (in order): {test[2]}\n")
                printed = mock_stdout.getvalue()
                for name in test[1]:
                    names_were_printed = name in printed
                    self.assertTrue(names_were_printed, "When I played your "
                            "game, I did not see the name(s) of the player(s) "
                            "when it was their turn.")
                for i in range(2, 8):
                    letters_were_printed = ' '.join([letter]*i) in printed
                    self.assertTrue(letters_were_printed, "When I "
                            "played your game, I did not see the player's "
                            "letters at each turn.")
                self.assertEqual(input.call_count, len(commands), "You did "
                        "not call the input function the correct number of "
                        "times. This should include: asking how many users "
                        "will play, asking each player for their name, "
                        "allowing each player to enter a word for their turn "
                        "(and asking again if they entered an invalid word).")

def gen_name():
    name = ""
    for i in range(random.randrange(5, 10)):
        name += gen_letter()
    return name

def gen_letter():
    return string.ascii_lowercase[random.randrange(len(string.ascii_lowercase))]
