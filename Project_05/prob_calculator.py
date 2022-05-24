import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):

    self.contents = list()

    for key, value in balls.items():
      self.contents += [key] * int(value)
       
  def draw(self, no_to_draw):

    result = list()
    
    if no_to_draw > len(self.contents):
      return self.contents
    
    for i in range(no_to_draw):
      number = random.randint(0, len(self.contents) - 1)
      result.append(self.contents[number])
      del self.contents[number]

    return result
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0

  for experiment in range(num_experiments):
    exp_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)

    for ball in drawn:
      if ball in exp_copy:
        exp_copy[ball] -= 1

    if all(x <= 0 for x in exp_copy.values()):
      count += 1

  return count / num_experiments
