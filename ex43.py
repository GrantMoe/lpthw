from sys import exit

class Scene(object):

  def enter(self):
    pass


class Engine(object):

  def __init__(self, scene_map):
    self.scene_map = scene_map

  def play(self):
    current_scene = self.scene_map.opening_scene()
    end_scene = self.scene_map.next_scene('game_over')

    while current_scene != end_scene:
      print('-' * 10)
      next_scene = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene)

    exit(0)
      

class Death(Scene):

  def enter(self):
    print("\n\tYou are dead now.\n")
    return('game_over')


class CentralCorridor(Scene):

  def enter(self):
    print("\nYou are in a corridor, the central one.\n")
    print("You see an angry Gothon!")
    print("\nDo you fight, do you flee, or do you tell a joke?")

    choice = input("> ")

    if "joke" in choice:
      print("\nThe Gothon is amused and/or perplexed.")
      print("It allows you to continue.\n")
      return('laser_weapon_armory')
    else:
      print("\nTurns out Gothons are both faster and stronger than you.\n")
      return('death')


class LaserWeaponArmory(Scene):

  def enter(self):
      print("\nYou enter the Laser Weapon Armory.\n")
      print("The armory is totally empty except for a neutron bomb")
      print("The bomb has a note tapped to it that reads 'Take Me'.")
      print("\nDo you take the bomb?")

      choice = input("> ")

      if choice == "yes" or choice == "take bomb":
        return('the_bridge')
      else:
        print("\nWithout a weapon, you are forced to joke for your life.")
        print("You are only so funny.\n")
        return('death')


class TheBridge(Scene):

  def enter(self):
    print("\nYou stumble onto the bridge!\n")
    print("You are struck with a sudden thought:")
    print("It sure would be a shame if someone were to plant a neutron bomb here.")
    print("\nSo?:")

    choice = input("> ")

    if 'plant' in choice:
      print("\n YOU PLANT THE BOMB!!!!!!!!")
      print("\n Do you stand around to watch it explode, or do you head for the escape pods?")

      choice = input("> ")

      if 'pod' in choice or 'escape' in choice:
        return('escape_pod')
      else:
        print("\nThe bomb explodes, and so do you.\n")
        return('death')
    else:
      print("\nThe bomb takes umbrage and decides to trigger itself.\n")
      return('death')
    

class EscapePod(Scene):

  def enter(self):
    print("\nYou run to the escape pods.")
    print("There is one left.")
    print("It literally has your name on it.")   
    print("\n\t\tCLIFFHANGER ENDING!\n")
    return('game_over')


class GameOver(Scene):

  def enter(self):
    print("\n\t\tGAME OVER\n\n")
    return('game_over')


class Map(object):

  scenes = {
    'death': Death(),
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'game_over': GameOver()
}

  def __init__(self, start_scene):
    self.start_scene = start_scene
    
  def next_scene(self, scene_name):
    return(self.scenes[scene_name])

  def opening_scene(self):
    return(self.scenes[self.start_scene])



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()