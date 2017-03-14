from sys import exit
from random import randint

print """
-------------------------------------------------------------------
Long long time ago, Dodo and princess had a pretty garden.
They were living happily with a cute shiba named Hamster.
One day when Dodo, princess and Hamster went for a hike,
Princess slipped and fell into a dark hole.
Dodo and Hamster jumped down to the hole to save princess.
When Dodo and Hamster finally landed into soft cushion of moss,
they saw little furry creatures that was carrying creatures away!
Without hesitation Dodo and Hamster followed the creatures.
-------------------------------------------------------------------
"""

raw_input("Press Enter to Continue")


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.",
        "Hamster died.",
        "Princess is gone.",
        "You don't deserve princess",
        "How did you fail at this?"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print """The fluffballs you suspect are the evil furries.
They are known to be very vicious creatures and eat anything in their way.
You are afraid that if you don't save princess in time, she will get eatten!
You must rescue her from the room filled with furries and get into an escape pod!
You and Hamster are running down the central corridor to the room full of
furries when a furry jumps out. Neon green, fluffy and fuzzy, with big brown
eyes, the furry is almost cute. However, its sharp fangs speak other wise.
The furry is blocking the door to the Room of Furries.
What do you do?

a. Hamster, I choose you!
b. Tell Furry a joke about a crow with boston accent.
c. Throw a stone at the Furry.
d. Run for the door.
"""

        action = raw_input("Choose a, b, c, or d: ")

        if action == "a":
            print """ What will Hamster do?
a. Growl
b. Charge
c. Harden
d. Reflect """


            h_action = raw_input("Choose a, b, c, or d: ")
            print "The Furry used Confusion!"

            if h_action == "a" or h_action == "b" or h_action == "c":
                return 'death'
            elif h_action == 'd':
                return 'room_full_of_Furries'
            else:
                print "What?"
                return 'central_corridor'

        elif action == "b":
            print "Lucky for you, the Furry is a bostonian."
            print "The Furry finds you a good bloke. He lets you through."
            return 'room_full_of_Furries'
        elif action == "c":
            print "You pick up a stone nearby and throw it at the Furry."
            print "The stone does no damage to plush Furry. Furry is enraged and"
            print "poisons you with its Poison Powder."
            return 'death'

        elif action == "d":
            print """ You think you were fast enough to run past the Furry.
However, you are not as fast as you think you are.
            """
            return 'death'

        else:
            print "What?"
            return 'central_corridor'


class RoomFullofFurries(Scene):

    def enter(self):
        print """ You sneak into the room full of Furries like a ninja.
You quickly glance around the room and locate the princess.
The princess is locked in a jail cell in the corner of the room.
By the looks of it, the Furries are prepping to roast her alive.
While they are busy celebrating their successful abduction, you
sneak all the way into the jail cell. The princess is surprised to
see you. She says \"Dodo! Hamster! I knew you would come to save me!\"
She looks relieved to see you guys. She continues \"There's a keypad
lock right here. You only have 10 tries. It will set off an alarm if
you get it wrong more than 10 times!\" You see that the lock has 3 digits.
"""
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD"
            if int(guess) < int(code):
                print "hint: try larger!"
            else:
                print "hint: try smaller!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The keypad unlocks."
            print """You help princess out and sneak past the Furries.
\"Come quick, it's this way!\" leads the princess. You three
run to the bridge to the Escape Pod."""
            return 'the_bridge'

        else:
            print "WRONG WRONG WRONG WRONG WRONG WRONG"
            print """The obnoxious alarm goes off. Every single Furry in
the room turns towards you."""
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print """You arrive at the Bridge with princess and Hamster.
Unfortunately, there are 3 Furries who had been guarding the Bridge.
Meanwhile, the Furries had noticed that the princess is missing. You
see the gleaming shadow of the Furries with torches and pitchforks.
What do you do?
a. Hamster, I choose you!
b. Throw a stone to divert Furries' attention and run.
c. Throw a stone at the Furry."""

        action = raw_input("Choose a, b, or c: ")

        if action == "a":
            print """ What will Hamster do?
a. Growl
b. Charge
c. Harden
d. Reflect """

            h_action = raw_input("Choose a, b, c, or d: ")
            print """The Furry1 used Poison Powder!
The Furry2 used Headbutt!
The Furry3 used Smog!"""
            return 'death'

        elif action == "b":
            print """You pick up a stone nearby and throw it away from you.
The 3 Furries skittle towards the stone to check out the noise.
You run across the bridge.
"""
            return 'escape_pod'
        elif action == "c":
            print """You pick up a stone nearby and throw it at the Furry.
The stone does no damage to plush Furry. Furry is enraged and
poisons you with its Poison Powder.
"""
            return 'death'
        else:
            print "What?"
            return 'the_bridge'
class EscapePod(Scene):

    def enter(self):
        print """You make it into the Escape Pod before the Furries catch you.
You have no idea how to work this machine. There are only three buttons
for you to choose from. Rectangle, triangle, and circle."""
        print """ Which button do you press?
1. Rectangle
2. Triangle
3. Circle
"""
        action = raw_input("Choose 1, 2, or 3: ")
        good_button = randint(1,3)

        if int(action) != good_button:
            print "You press the button!"
            print "The button doesn't do anything."
            return 'death'

        else:
            print "The pod activates. You blink through time and space."
            print "."
            print "."
            print "."
            print "."
            print "."
            print "."
            print "."
            print """You wake up to princess shaking you. She looks concerned.
\"Are you ok, Dodo? You were screaming and yelling as if you were
having a nightmare, I had to wake you up.\" You look around and realize
it was all a dream"""

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You live happily ever after!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'room_full_of_Furries': RoomFullofFurries(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
