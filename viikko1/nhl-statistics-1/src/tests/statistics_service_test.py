import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )  

    def test_loytaa_oikean_pelaajan(self):
        loydettyPelaaja = self.stats.search("Kurri")
        self.assertEqual(loydettyPelaaja.name, "Kurri")
        self.assertEqual(loydettyPelaaja.team, "EDM")
        self.assertEqual(loydettyPelaaja.goals, 37)
        self.assertEqual(loydettyPelaaja.assists, 53)

    def test_palauttaa_tyhjan_jos_pelaajaa_ei_loydy(self):
        self.assertEqual(self.stats.search("Kurra"), None)

    def test_listaa_joukkueen_pelaajat(self):
        odotettuLista = list((Player("Semenko", "EDM", 4, 12), Player("Kurri", "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)))
        joukkueLista = self.stats.team("EDM")
        for i in range(3):
            self.assertEqual(joukkueLista[i].name, odotettuLista[i].name)

    def test_listaa_maaritellyn_maaran_parhaimpia_pelaajia(self):
        odotettuLista = list((Player("Gretzky", "EDM", 35, 89), Player("Lemieux", "PIT", 45, 54), Player("Yzerman", "DET", 42, 56)))
        parhaatLista = self.stats.top(3)
        for i in range(3):
            self.assertEqual(parhaatLista[i].name, odotettuLista[i].name)