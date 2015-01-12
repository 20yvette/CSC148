# Lab 2 - Pokemon vs. Digimon
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Lab 2: Pokemon vs. Digimon.

This module contains stub classes for Pokemon and Digimon.
Make sure you understand the inheritance relationships
between the three classes, and then start implementing methods!
"""


class Creature:
    """Base creature class.

    This class is an abstract class, meaning it isn't meant to be
    used directly. It serves as a base class for both Pokemon and Digimon.

    Attributes:
    - name (str): the name of the Creature
    - health (int): the amount of health of the Creature. Cannot go below 0.
    """

    def __init__(self, name, health):
        """ (Creature, str, int) -> NoneType
        Create a new Creature with the given name and amount of health.
        """
        self.name = name
        self.health = health

    def roar(self):
        """ (Creature) -> str
        Return a string representing this Creature's roar.
        """
        return '...'

    def attack(self, enemy):
        """ (Creature, Creature) -> NoneType
        Make this Creature attack enemy.
        Usually makes enemy lose health.
        """
        raise NotImplementedError

    def take_damage(self, damage):
        """ (Creature, int) -> NoneType
        Reduce this Creature's health by damage, to a minimum of 0.
        Call self.faint if health reaches 0.
        """
        if self.health > 0:
            if self.health - damage > 0:
                self.health = self.health - damage
            else:
                self.health = 0
        else:
            self.faint

    def faint(self):
        """ (Creature) -> NoneType
        Make this Creature unable to take actions.
        Called when this Creature's health reaches 0.
        """
        print(self.name + ' is dead')


class Pokemon(Creature):
    """Pokemon class.

    Non-Inherited Attributes:
    - pokemon_type (str): either 'grass', 'fire', or 'water',
      indicating Pokemon's type
    """
    def __init__(self, name, pokemon_type):
        """ (Pokemon, str, str) -> NoneType
        Create a new Pokemon with the given name and type.
        """
        self.name = name
        self.pokemon_type = pokemon_type
        self.creature_type = 'pokemon'
        self.health = 50

    # Overridden methods
    def roar(self):
        print(self.name + ' ' + self.name + '!')

    def attack(self, enemy):
        if enemy.creature_type == 'pokemon':
            if self.pokemon_type == 'fire' and enemy.pokemon_type == 'grass':
                enemy.take_damage(40)
                print('Attack was super effective!')
            elif self.pokemon_type == 'water' and enemy.pokemon_type == 'fire':
                enemy.take_damage(40)
                print('Attack was super effective!')
            elif self.pokemon_type == 'grass' and enemy.pokemon_type == 'water':
                enemy.take_damage(40)
                print('Attack was super effective!')
            else:
                enemy.take_damage(20)
        else:
            enemy.take_damage(20)

class Digimon(Creature):
    """Digimon class.

    Non-Inherited Attributes:
    - charging (bool): whether this Digimon is charging for its next attack
    """
    def __init__(self, name):
        """ (Digimon, str) -> NoneType
        Create a new Digimon with the given name.
        """
        self.name = name
        self.creature_type = 'digimon'
        self.charges = 1
        self.health = 40

    # Overridden methods
    def roar(self):
        print('Digimon {} awaiting command!'.format(self.name))

    def attack(self, enemy):
        enemy.take_damage(15*(self.charges))
        charges = 1
            
    # New method
    def charge(self):
        """ (Digimon) -> int
        Save energy, making this Digimon's next attack deal double damage.
        """
        self.charges = 2
        return None

    def de_charge(self):
        """ (Digimon) -> int
        Release energy for the attack.
        """
        self.charges = 1
        return None
    
