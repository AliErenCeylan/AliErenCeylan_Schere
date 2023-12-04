import random
while 0 == 0:
    Start = input()
    if Start == "":
        character = ["Aatrox","Ahri","Akali","Akshan","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","Aurelion Sol","Azir","Bard","Bel'Veth","Bltizcrank","Brand","Braum",
                     "Brair","Caitlyn","Camille","Cassiopeia","Cho'Gath","Corki","Darius","Diana","Dr.Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz",
                     "Galio","Gangplank","Garen","Gnar","Gragas","Graves","Gwen","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan IV.","Jax","Jayce","Jhin","Jinx",
                     "K'Sante","Kai'sa","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","Kha'Zix","Kindred","Kled","Kog'Maw","LeBlanc","Lee Sin","Leona",
                     "Lillia","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Milio","Miss Fortune","Mordekaiser","Morgana","Naafiri","Nami","Nasus",
                     "Nautilus","Neeko","Nidalee","Nilah","Nocturne","Nunu & Willump","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","Rek'Sai",
                     "Rell","Renata Glasc","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Senna","Seraphine","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir",
                     "Skarner","Sona","Soraka","Swain","Sylas","Syndra","Tahm Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate",
                     "Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vex","Vi","Viego","Viktor","Vladimir","Volibear","Warwick","Wukong","Xayah","Xerath","Xin Zhao",
                     "Yasuo","Yone","Yorick","Yuumi","Zac","Zed","Zeri","Zigga","Zilean","Zoe","Zyra"]
        lane = ["Top","Jungle","Mid","Bot","Support"]
        boots = ["Berserker's Greaves","Boots of Swiftness","Sorcerer's Shoes","Mercury's Treads","Mobility Boots","Ionian Boots of Lucidity","Plated Steelcaps"]
        mythic = ["Crown of the Shattered Queen","Divine Sunderer","Duskblade of Draktharr","Echoes of Helia","Eclipse","Evenshroud","Everfrost","Galeforce","Goredrinker",
                  "Guinsoo's Rageblade","Heartsteel","Hextech Rocketbelt","Iceborn Gauntlet","Infinity Edge","Jak'Sho, The Protean","Liandry's Anguish","Locket of the Iron Solari",
                  "Luden's Tempest","Moonstone Renewer","Navori Quickblades","Night Harvester","Radiant Virtue","Riftmaker","Rod of Ages","Shurelya's Battlesong","Stridebreaker",
                  "Trinity Force","Youmuu's Ghostblade"]
        legendary = ["Abyssal Mask","Anathema's Chains","Archangel's Staff","Ardent Censer","Axiom Arc","Banshee's Veil","Black Cleaver",
                     "Blade of the Ruined King","Bloodthirster","Chempunk Chainsword","Chemtech Putrifier","Cosmic Drive","Dead Man's Plate","Death's Dance",
                     "Demonic Embrace","Edge of Night","Essence Reaver","Fimbulwinter","Force of Nature","Frozen Heart","Gargoyle Stoneplate","Guardian Angel",
                     "Hextech Gunblade","Horizon Focus","Hullbreaker","Immortal Shieldbow","Imperial Mandate","Knight's Vow","Kraken Slayer","Lich Bane",
                     "Lord Dominik's Regards","Manamune","Maw of Malmortius","Mejai's Soulstealer","Mercurial Scimitar","Mikael's Blessing","Morellonomicon","Mortal Reminder",
                     "Muramana","Nashor's Tooth","Phantom Dancer","Prowler's Claw","Rabadon's Deathcap","Randuin's Omen","Rapid Firecannon","Ravenous Hydra",
                     "Redemption","Runaan's Hurricane","Rylai's Crystal Scepter","Seraph's Embrace","Serpent's Fang","Serylda's Grudge","Shadowflame",
                     "Silvermere Dawn","Spear of Shojin","Spirit Visage","Staff of Flowing Water","Statikk Shiv","Sterak's Gage","Stormrazor","Sunfire Aegis",
                     "The Collector","Thornmail","Titanic Hydra","Turbo Chemtank","Umbral Glaive","Vigilant Wardstone","Void Staff","Warmog's Armor","Winter's Approach","Wit's End",
                     "Zeke's Convergence","Zephyr","Zhonya's Hourglass"]
        summoners = ["Flash","Ghost","Ignite","Exhaust","Cleanse","Teleport","Barrier","Heal"]
        jungle_item = ["Red Smite","Green Smite","Blue Smite"]
        ability = ["Q","W","E"]
        primary_runes = ["Press the Attack","Lethal Tempo","Fleet Footwork","Conqueror","Electrocute","Predator","Dark Harvest","Hail of Blades","Glacial Augment",
                         "Unsealed Spellbook","First Strike","Grasp of the Undying","Aftershock","Guardian","Summon Aery","Arcane Comet","Phase Rush"]
        precision_runes_top = ["Overheal","Triumph","Presence of Mind"]
        precision_runes_mid = ["Legend: Alacrity","Legend: Tenacity","Legend: Bloodline"]
        precision_runes_bot = ["Goup de Grace","Cut Down","Last Stand"]
        domination_runes_top = ["Cheap Shot","Taste of Blood","Sudden Impact"]
        domination_runes_mid = ["Zombie Ward","Ghost Poro","Eyeball Collection"]
        domination_runes_bot = ["Treasure Hunter","Ingenious Hunter","Relentless Hunter","Ultimate Hunter"]
        sorcery_runes_top = ["Nullifying Orb","Manaflow Band","Nimbus Cloak"]
        sorcery_runes_mid = ["Transcendence","Celerity","Absolute Focus"]
        sorcery_runes_bot = ["Scorch","Waterwalking","Gathering Storm"]
        resolve_runes_top = ["Demolish","Font of Life","Shield Bash"]
        resolve_runes_mid = ["Conditioning","Second Wind","Bone Plating"]
        resolve_runes_bot = ["Overgrowth","Revitalize","Unflinching"]
        inspiration_runes_top = ["Hextech Flashtraption","Magical Footwear","Perfect Timing"]
        inspiration_runes_mid = ["Future's Market","Minion Dematerializer","Biscuit Delivery"]
        inspiration_runes_bot = ["Cosmis Insight","Approach Velocity","Time Warp Tonic"]
        stat_mods_top = ["Adaptive Force","Attack Speed","Ability Haste"]
        stat_mods_mid = ["Adaptive Force","Armor","Magic Resist"]
        stat_mods_bot = ["Health Scaling","Armor","Magic Resist"]

        numbers = [1,2,3,4]
        number = (random.choice(numbers))

        spr = [random.choice(precision_runes_top),random.choice(precision_runes_mid),random.choice(precision_runes_bot)]
        sdr = [random.choice(domination_runes_top),random.choice(domination_runes_mid),random.choice(domination_runes_bot)]
        ssr = [random.choice(sorcery_runes_top),random.choice(sorcery_runes_mid),random.choice(sorcery_runes_bot)]
        srr = [random.choice(resolve_runes_top),random.choice(resolve_runes_mid),random.choice(resolve_runes_bot)]
        sir = [random.choice(inspiration_runes_top),random.choice(inspiration_runes_mid),random.choice(inspiration_runes_bot)]

        role = random.choice(lane)
        primary__runes = random.choice(primary_runes)
        print("Character: ",random.choice(character))
        print("Role: ",role)
        print("Boots: ",random.choice(boots))
        print("Mythic: ",random.choice(mythic))
        print("Legendarys: ",random.sample(legendary,4))
        if role == "Jungle":
            print("Summoners: ","Smite,", random.choice(summoners))
            print("Jungle Item: ",random.choice(jungle_item))
        else:
            print("Summoners",random.sample(summoners,2))
        print("First Max: ", random.choice(ability))
        print("Primary Runes: ", primary__runes)

        if primary__runes == "Press the Attack" or primary__runes == "Lethal Tempo" or primary__runes == "Fleet Footwork" or primary__runes == "Conqueror":
            print(random.choice(precision_runes_top),",",random.choice(precision_runes_mid),",",random.choice(precision_runes_bot))
            if number == 1:
                print(random.sample(sdr,2))
            elif number == 2:
                print(random.sample(ssr,2))
            elif number == 3:
                print(random.sample(srr,2))
            elif number == 4:
                print(random.sample(sir,2))
        elif primary__runes == "Electrocute" or primary__runes == "Predator" or primary__runes == "Dark Harvest" or primary__runes == "Hail of Blades":
            print(random.choice(domination_runes_top),",",random.choice(domination_runes_mid),",",random.choice(domination_runes_bot))
            if number == 1:
                print(random.sample(spr,2))
            elif number == 2:
                print(random.sample(ssr,2))
            elif number == 3:
                print(random.sample(srr,2))
            elif number == 4:
                print(random.sample(sir,2))
        elif primary__runes == "Summon Aery" or primary__runes == "Arcane Comet" or primary__runes == "Phase Rush":
            print(random.choice(sorcery_runes_top),",",random.choice(sorcery_runes_mid),",",random.choice(sorcery_runes_bot))
            if number == 1:
                print(random.sample(spr,2))
            elif number == 2:
                print(random.sample(sdr,2))
            elif number == 3:
                print(random.sample(srr,2))
            elif number == 4:
                print(random.sample(sir,2))
        elif primary__runes == "Grasp of the Undying" or primary__runes == "Aftershock" or primary__runes == "Guardian":
            print(random.choice(resolve_runes_top),",",random.choice(resolve_runes_mid),",",random.choice(resolve_runes_bot))
            if number == 1:
                print(random.sample(spr,2))
            elif number == 2:
                print(random.sample(sdr,2))
            elif number == 3:
                print(random.sample(ssr,2))
            elif number == 4:
                print(random.sample(sir,2))
        elif primary__runes == "Glacial Augment" or primary__runes == "Unsealed Spellbook" or primary__runes == "First Strike":
            print(random.choice(inspiration_runes_top),",",random.choice(inspiration_runes_mid),",",random.choice(inspiration_runes_bot))
            if number == 1:
                print(random.sample(spr,2))
            elif number == 2:
                print(random.sample(sdr,2))
            elif number == 3:
                print(random.sample(ssr,2))
            elif number == 4:
                print(random.sample(srr,2))
        print(random.choice(stat_mods_top),",",random.choice(stat_mods_mid),",",random.choice(stat_mods_bot))