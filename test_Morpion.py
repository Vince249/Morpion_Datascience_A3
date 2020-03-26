import unittest
import Morpion
import Fonctions_de_base

class Test_Fonctions_de_base_Action(unittest.TestCase):

    def testAction(self):
        liste = Fonctions_de_base.Action([['X','',''],['O','X',''],['','O','O']], 'X')
        self.assertEqual(liste,[['X', 0, 1], ['X', 0, 2], ['X', 1, 2], ['X', 2, 0]])


class Test_Fonctions_de_base_Result(unittest.TestCase):

    def testResult(self):
        liste = [['X','',''],['O','X',''],['','O','O']]
        liste = Fonctions_de_base.Result(liste,['X', 0, 1])
        self.assertEqual(liste, [['X','X',''],['O','X',''],['','O','O']])


class Test_Fonctions_de_base_Terminal(unittest.TestCase):

    def testTerminalPasFini(self):
        state = [['X','O','X'],['','',''],['','O','O']]
        self.assertFalse(Fonctions_de_base.Terminal_Test(state,3))

    def testTerminalPlein(self):
        state = [['X','O','X'],['O','X','X'],['X','O','O']]
        self.assertTrue(Fonctions_de_base.Terminal_Test(state,3))

    def testTerminalLigne(self):
        state = [['X','X','X'],['O','X',''],['','O','O']]
        self.assertTrue(Fonctions_de_base.Terminal_Test(state,3))
    
    def testTerminalColonnes(self):
        state = [['X','',''],['X','X',''],['X','O','O']]
        self.assertTrue(Fonctions_de_base.Terminal_Test(state,3))
    
    def testTerminalDiagonal(self):
        state = [['X','X','O'],['O','X',''],['','O','X']]
        self.assertTrue(Fonctions_de_base.Terminal_Test(state,3))


class Test_Fonctions_de_base_Utility(unittest.TestCase):

    def testUtility1(self):
        liste = [['X','X','X'],['O','X','O'],['X','O','O']]
        result = Fonctions_de_base.Utility(liste,'X')
        self.assertEqual(result, 1)

    def testUtilitymoins1(self):
        liste = [['X','X','O'],['X','O','O'],['O','X','']]
        result = Fonctions_de_base.Utility(liste,'X')
        self.assertEqual(result, -1)

    def testUtility0(self):
        liste = [['O','X','O'],['O','X','O'],['X','O','X']]
        result = Fonctions_de_base.Utility(liste,'X')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()