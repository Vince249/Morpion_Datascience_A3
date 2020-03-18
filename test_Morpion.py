import unittest
import Morpion

class TestMorpionAction(unittest.TestCase):

    def testAction(self):
        liste = Morpion.Action([['X','',''],['O','X',''],['','O','O']], 'X')
        self.assertEqual(liste,[['X', 0, 1], ['X', 0, 2], ['X', 1, 2], ['X', 2, 0]])


class TestMorpionResult(unittest.TestCase):

    def testResult(self):
        liste = [['X','',''],['O','X',''],['','O','O']]
        liste = Morpion.Result(liste,['X', 0, 1])
        self.assertEqual(liste, [['X','X',''],['O','X',''],['','O','O']])


class TestMorpionTerminal(unittest.TestCase):

    def testTerminalPasFini(self):
        state = [['X','O','X'],['','',''],['','O','O']]
        self.assertFalse(Morpion.Terminal_Test(state,3))

    def testTerminalPlein(self):
        state = [['X','O','X'],['O','X','X'],['X','O','O']]
        self.assertTrue(Morpion.Terminal_Test(state,3))

    def testTerminalLigne(self):
        state = [['X','X','X'],['O','X',''],['','O','O']]
        self.assertTrue(Morpion.Terminal_Test(state,3))
    
    def testTerminalColonnes(self):
        state = [['X','',''],['X','X',''],['X','O','O']]
        self.assertTrue(Morpion.Terminal_Test(state,3))
    
    def testTerminalDiagonal(self):
        state = [['X','X','O'],['O','X',''],['','O','X']]
        self.assertTrue(Morpion.Terminal_Test(state,3))


class TestMorpionUtility(unittest.TestCase):

    def testUtility1(self):
        liste = [['X','X','X'],['O','X','O'],['X','O','O']]
        result = Morpion.Utility(liste,'X')
        self.assertEqual(result, 1)

    def testUtilitymoins1(self):
        liste = [['X','X','O'],['X','O','O'],['O','X','']]
        result = Morpion.Utility(liste,'X')
        self.assertEqual(result, -1)

    def testUtility0(self):
        liste = [['O','X','O'],['O','X','O'],['X','O','X']]
        result = Morpion.Utility(liste,'X')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()