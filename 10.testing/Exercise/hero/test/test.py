from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('my_hero', 1, 100, 20)

    def test_correct_init(self):
        self.assertEqual('my_hero', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_method_enemy_hero_name_same_as_my_hero_name(self):
        enemy_hero = Hero('my_hero', 1, 90, 20)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_my_health_below_zero(self):
        self.hero.health = 0
        enemy_hero = Hero('some_bad_hero', 1, 90, 20)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_enemy_hero_health_below_zero(self):
        enemy_hero = Hero('some_bad_hero', 1, 0, 20)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight some_bad_hero. He needs to rest", str(ex.exception))

    def test_battle_method_enemy_and_my_hero_health_falls_below_zero(self):
        self.hero.health = 20
        enemy_hero = Hero('some_bad_hero', 1, 20, 20)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual('Draw', result)

    def test_battle_method_i_win(self):
        enemy_hero = Hero('some_bad_hero', 1, 20, 20)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(85, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual('You win', result)

    def test_battle_method_enemy_wins(self):
        enemy_hero = Hero('some_bad_hero', 1, 100, 100)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(2, enemy_hero.level)
        self.assertEqual(85, enemy_hero.health)
        self.assertEqual(105, enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected_result = "Hero my_hero: 1 lvl\n" \
                          "Health: 100\n" \
                          "Damage: 20\n"
        result = self.hero.__str__()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
