from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.super_dog = Hero('Burya', 2, 100, 1)
        self.enemy = Hero('Losha', 7, 100, 1)

    def test_correct_initialization(self):
        self.assertEqual('Burya', self.super_dog.username)
        self.assertEqual(2, self.super_dog.level)
        self.assertEqual(100, self.super_dog.health)
        self.assertEqual(1, self.super_dog.damage)

    def test_you_cannot_fight_yourself_raises(self):
        enemy = Hero('Burya', 7, 100, 1)
        with self.assertRaises(Exception) as ex:
            self.super_dog.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_below_zero_raises(self):
        self.super_dog.health = -1

        with self.assertRaises(ValueError) as ex:
            self.super_dog.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_equal_zero_raises(self):
        self.super_dog.health = 0

        with self.assertRaises(ValueError) as ex:
            self.super_dog.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_health_below_zero_raises(self):
        self.enemy.health = -1

        with self.assertRaises(ValueError) as ex:
            self.super_dog.battle(self.enemy)

        self.assertEqual("You cannot fight Losha. He needs to rest", str(ex.exception))

    def test_enemy_health_equal_zero_raises(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ex:
            self.super_dog.battle(self.enemy)

        self.assertEqual("You cannot fight Losha. He needs to rest", str(ex.exception))

    def test_hero_health_decreases_after_battle(self):
        expected = 93
        self.super_dog.battle(self.enemy)
        self.assertEqual(expected, self.super_dog.health)

    def test_enemy_health_changes_after_battle_when_hero_loses(self):
        expected = 98 + 5
        result = self.super_dog.battle(self.enemy)
        self.assertEqual(expected, self.enemy.health)
        self.assertEqual('You lose', result)

    def test_enemy_damage_changes_after_battle_when_hero_loses(self):
        expected = 6
        self.super_dog.battle(self.enemy)
        self.assertEqual(expected, self.enemy.damage)

    def test_enemy_level_changes_after_battle_when_hero_loses(self):
        expected = 8
        self.super_dog.battle(self.enemy)
        self.assertEqual(expected, self.enemy.level)

    # TODO
    def test_draw_when_health_is_zero_after_battle(self):
        super_dog = Hero('Burya', 100, 100, 1)
        enemy = Hero('Losha', 100, 50, 1)
        result = super_dog.battle(enemy)
        self.assertEqual(0, super_dog.health)
        self.assertEqual(-50, enemy.health)
        self.assertEqual("Draw", result)

    def test_hero_level_changes_after_battle_when_enemy_loses(self):
        self.enemy.health = 5
        self.super_dog.level = 20
        expected = 21
        result = self.super_dog.battle(self.enemy)
        self.assertEqual(expected, self.super_dog.level)
        self.assertEqual('You win', result)

    def test__str__method(self):
        expected = f"Hero Burya: 2 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 1\n"
        self.assertEqual(expected, self.super_dog.__str__())

if __name__ == '__main__':
    main()
