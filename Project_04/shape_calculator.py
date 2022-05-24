class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
    
  def set_width(self, width):
    self.width = width
    return self.width

  def set_height(self, height):
    self.height = height
    return self.height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    pic_width = self.width * '*' + '\n'
    pic_height = ''

    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    else:
      for line in range(self.height):
        pic_height += pic_width

      return pic_height

  def get_amount_inside(self, other):
    division_width = self.width // other.width
    division_height = self.height // other.height

    return division_width * division_height
      
class Square(Rectangle):

  def __init__ (self, side):
    self.height = side
    self.width = side

  def __str__(self):
    return 'Square(side={})'.format(self.width)

  def set_side(self, side):
    self.height = side
    self.width = side
    return self.height, self.width
    
