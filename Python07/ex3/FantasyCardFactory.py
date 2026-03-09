from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardfactory(CardFactory):
    def __init__(self):
        self.data = {
            'creatures': [
                ('Shadow Assassin', 3, 'Rare', 3, 6),
                ('Stone Golem', 6, 'Common', 10, 3),
                ('Forest Nymph', 2, 'Uncommon', 4, 2),
                ('Frost Giant', 7, 'Epic', 12, 8),
                ('Thunder Bird', 5, 'Rare', 6, 7),
                ('Undead Knight', 4, 'Uncommon', 5, 5),
                ('Crystal Sphinx', 8, 'Legendary', 9, 9),
                ('Venomous Spider', 2, 'Common', 2, 4),
                ('Phoenix Reborn', 6, 'Legendary', 5, 8),
                ('Deep Sea Kraken', 9, 'Epic', 15, 10),
                ('Arcane Elemental', 4, 'Rare', 4, 6),
                ('Goblin Raider', 1, 'Common', 2, 2),
                ('Iron Valkyrie', 5, 'Epic', 7, 6),
                ('Moonlight Wolf', 3, 'Uncommon', 4, 4),
                ('Solar Seraph', 8, 'Legendary', 10, 12),
                ('Cursed Scarecrow', 3, 'Common', 5, 3),
                ('Desert Manticore', 5, 'Rare', 6, 5),
                ('Void Stalker', 4, 'Epic', 3, 9),
                ('Ancient Ent', 7, 'Rare', 14, 4),
                ('Lava Slime', 2, 'Common', 6, 2),
                ('Storm Griffin', 5, 'Uncommon', 5, 7),
                ('Necromancer Lord', 6, 'Epic', 6, 6),
                ('Golden Pixie', 1, 'Rare', 1, 1),
                ('Obsidian Gargoyle', 4, 'Uncommon', 8, 4),
                ('Abyssal Dragon', 10, 'Legendary', 20, 15),
                ],
            'spells': [
                ("Lightning Bolt", 3, "Common", "Deal 3 damage to target"),
                ("Healing Touch", 2, "Common", "Restore 5 HP to an ally"),
                ("Fireball", 5, "Uncommon",
                 "Deal 6 area damage to all enemies"),
                ("Ice Nova", 4, "Rare", "Freeze all enemies for 1 turn"),
                ("Arcane Intellect", 3, "Common",
                 "Draw 2 cards from your deck"),
                ("Divine Shield", 2, "Uncommon",
                 "Target creature gains Invincibility for 1 turn"),
                ("Shadow Word: Pain", 4, "Rare",
                 "Destroy a creature with 3 Attack or less"),
                ("Meteor Shower", 8, "Legendary",
                 "Deal 12 damage split among all enemies"),
                ("Wind Walk", 1, "Common", "Target creature gains Stealth"),
                ("Poison Cloud", 5, "Uncommon",
                 "Deal 2 damage to all enemies for 3 turns"),
                ("Time Warp", 10, "Legendary",
                 "Take an extra turn after this one"),
                ("Mirror Image", 3, "Rare",
                 "Summon two 1/1 copies of a creature"),
                ("Blood Sacrifice", 2, "Epic",
                 "Lose 3 HP to gain 2 Mana crystals"),
                ("Nature's Wrath", 6, "Rare",
                 "Destroy all non-Legendary creatures"),
                ("Thunderstorm", 5, "Epic",
                 "Deal 4 damage and reduce enemy Attack by 2"),
                ("Holy Light", 7, "Legendary",
                 "Fully restore HP to your Hero"),
                ("Entangling Roots", 2, "Common",
                 "Target creature cannot attack next turn"),
                ("Mind Control", 9, "Epic",
                 "Take control of an enemy creature"),
                ("Blizzard", 6, "Rare",
                 "Deal 2 damage and Freeze all enemies"),
                ("Cursed Curse", 1, "Common",
                 "Target deals -1 damage permanently"),
                ("Dragon's Breath", 5, "Uncommon",
                 "Deal 5 damage in a cone shape"),
                ("Resurrection", 7, "Epic", "Summon a random fallen ally"),
                ("Mana Leak", 2, "Uncommon",
                 "Counter the next spell played by enemy"),
                ("Gravity Well", 4, "Rare",
                 "Group all enemies together and Stun them"),
                ("Final Judgement", 10, "Legendary",
                 "Clear the entire battlefield"),
            ],
            'artifacts': [
                ("Mana Crystal", 2, "Uncommon", 6,
                 "Permanent: +1 mana per turn"),
                ("Ancient Shield", 3, "Common", 5,
                 "Absorb 2 damage from each attack"),
                ("Void Pendant", 4, "Rare", 3,
                 "Deathrattle: Draw 2 shadow spells"),
                ("King's Crown", 6, "Legendary", 4,
                 "Battlecry: Give all allies +2/+2"),
                ("Cursed Idol", 1, "Common", 8,
                 "Enemy spells cost 1 more mana"),
                ("Sun Core", 5, "Epic", 5,
                 "At start of turn, heal all allies for 2"),
                ("Rusty Compass", 2, "Common", 4,
                 "Discover a random location card"),
                ("Dragon Scale", 4, "Uncommon", 7,
                 "Ignore the first damage taken each turn"),
                ("Infinity Hourglass", 10, "Legendary", 1,
                 "Active: Restart the current turn"),
                ("Soul Jar", 3, "Rare", 10,
                 "Gain 1 durability when a creature dies"),
                ("Wizard Staff", 5, "Uncommon", 6,
                 "Spell damage is increased by 1"),
                ("Assassin's Cloak", 4, "Rare", 3,
                 "Your hero has Stealth during your turn"),
                ("Alchemist's Kit", 2, "Common", 5,
                 "Transform a random card into a Potion"),
                ("Thunder Forge", 6, "Epic", 4,
                 "After you play a card, deal 1 damage to a random enemy"),
                ("Gorgon's Eye", 5, "Rare", 2,
                 "Active: Turn an enemy creature into a 0/5 Stone Statue"),
                ("Amulet of Life", 3, "Uncommon", 6,
                 "Your healing effects are doubled"),
                ("War Drum", 4, "Common", 4,
                 "Give your creatures +1 Attack this turn"),
                ("Frost Orb", 5, "Epic", 3,
                 "Freeze any character that attacks your hero"),
                ("Bounty Map", 1, "Rare", 1,
                 "Battlecry: Reveal the top 3 cards of your deck"),
                ("Demonic Pact", 0, "Legendary", 5,
                 "Gain 2 mana this turn, then lose 2 HP"),
                ("Lifeblood Ring", 3, "Uncommon", 8,
                 "Whenever you spend mana, restore 1 HP"),
                ("Gravity Anchor", 7, "Epic", 4,
                 "Creatures cannot be returned to the hand"),
                ("Mirror Shield", 5, "Rare", 5,
                 "Reflect the first spell targeted at you"),
                ("Phoenix Feather", 6, "Legendary", 1,
                 "If you die, restore 10 HP instead (Once)"),
                ("Blacksmith's Anvil", 2, "Common", 10,
                 "Active: Give a weapon +1/+1"),
            ]
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        new_name = random.choice(self.data['creatures'])[0]
        new_mana = random.choice(self.data['creatures'])[1]
        new_rarity = random.choice(self.data['creatures'])[2]
        new_attack = random.choice(self.data['creatures'])[3]
        new_health = random.choice(self.data['creatures'])[4]

        if isinstance(name_or_power, int):
            new_mana = name_or_power
        elif isinstance(name_or_power, str):
            new_name = name_or_power

        new_creature = CreatureCard(new_name, new_mana,
                                    new_rarity, new_attack, new_health)
        return new_creature

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        new_name = random.choice(self.data['spells'])[0]
        new_mana = random.choice(self.data['spells'])[1]
        new_rarity = random.choice(self.data['spells'])[2]
        new_effect = random.choice(self.data['spells'])[3]

        if isinstance(name_or_power, int):
            new_mana = name_or_power
        elif isinstance(name_or_power, str):
            new_name = name_or_power

        new_spell = SpellCard(new_name, new_mana, new_rarity, new_effect)
        return new_spell

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        new_name = random.choice(self.data['artifacts'])[0]
        new_mana = random.choice(self.data['artifacts'])[1]
        new_rarity = random.choice(self.data['artifacts'])[2]
        new_durability = random.choice(self.data['artifacts'])[3]
        new_effect = random.choice(self.data['artifacts'])[4]

        if isinstance(name_or_power, int):
            new_mana = name_or_power
        elif isinstance(name_or_power, str):
            new_name = name_or_power

        new_artifact = ArtifactCard(new_name, new_mana, new_rarity,
                                    new_durability, new_effect)
        return new_artifact

    def create_themed_deck(self, size: int) -> dict:
        available: list = (self.data['creatures']
                           + self.data['spells']
                           + self.data['artifacts'])
        deck: dict = {}
        if size > 60:
            print("error, deck is 60 card max")
            return None
        selection = random.sample(available, size)
        for i, card in enumerate(selection):
            if card in self.data['creatures']:
                newcard = CreatureCard(*card)
            elif card in self.data['spells']:
                newcard = SpellCard(*card)
            elif card in self.data['artifacts']:
                newcard = ArtifactCard(*card)
            deck[f"card {i+1}"] = newcard
        return deck

    def get_supported_types(self) -> dict:
        supported = {'supported_types': []}
        for key in self.data:
            supported['supported_types'].append(key)
        return supported
