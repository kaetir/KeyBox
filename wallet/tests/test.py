import unittest

from wallet.genRngPasswd import *


class tests_rng(unittest.TestCase):
    """
    class de test des gen password
    """

    def test_passwd(self):
        for i in range(5, 30):
            passwd = random_string(i)
            self.assertEqual(len(passwd), i, "mot de passe pas de la bonne longueur")
            self.assertTrue( all(x in string.printable.replace(string.whitespace, "") for x in passwd), "Not readable")



if __name__ == '__main__':
    unittest.main()