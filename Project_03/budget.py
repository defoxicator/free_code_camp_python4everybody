class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
    
  # Deposit
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : amount, "description" : description})

  # Withdraw
  def withdraw(self, amount, description = ""):
    
    # Checking if withdrawal is possible
    if self.check_funds(amount) == True:
      amount *= -1
      self.ledger.append({"amount" : amount, "description" : description})
      return True
    else:
      return False
      
  # Transfer
  def transfer(self, amount, other):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount' : amount * (-1), 'description' : "Transfer to {}".format(other.name)})
      other.ledger.append({'amount' : amount, 'description' : "Transfer from {}".format(self.name)})
      return True
    else:
      return False
    
  # Balance
  def get_balance(self):
    money = 0
    for transaction in self.ledger:
      money += transaction['amount']
    return money

  # Checking if withdraw or transfer is possible
  def check_funds(self, amount):
    money = self.get_balance()
    if amount > money:
      return False
    else: 
      return True 

  # Text version title
  def __str__(self):

    # Title
    length_title_half = len(self.name) // 2
    if len(self.name) % 2 != 0:
      title = (15 - length_title_half) * "*" + self.name + (14 - length_title_half) * "*"
    else:
      title = (15 - length_title_half) * "*" + self.name + (15 - length_title_half) * "*"

    description = list()
    amount = list()

    # Descriptions
    for desc in self.ledger:
      desc_1 = desc['description']
      desc_2 = desc_1[0:23]
      description.append(desc_2)

    # Money money money
    for amo in self.ledger:
      amo_1 = str(amo['amount'])
      is_decimal = amo_1.find(".")
      
      if is_decimal == -1:
        amo_1 = amo_1 + ".00"

      amo_2 = amo_1[-7:]
      amount.append(amo_2)

    # Creating a table
    table = list()
    table.append(title)
    table.append('\n')
    table_length = len(amount)
    total_money = 0
    
    for i in range(0, table_length):
      table.append(description[i])
      space = (30 - len(description[i]) - len(amount[i])) * " "
      table.append(space)
      table.append(amount[i])
      table.append('\n')
      total_money += float(amount[i])

    table.append("Total: {}".format(total_money))
    good_table = ''.join(str(i) for i in table)
    return good_table
    
def create_spend_chart(categories):

  # title and scale 100 -> 0
  scale = list()
  title = 'Percentage spent by category\n'
  scale.append('  ' + str(0) + '| ')
  
  for i in range(10, 100, 10):
    scale.append(' ' + str(i) + '| ')
    
  scale.append('100| ')
  scale = scale[::-1]

  # Calculating 
  
  total_withdrawals = 0
  list_withdrawals = list()
  percents = list()
  
  for category in categories:

    withdrawals = 0
    
    for dictionary in category.ledger:
      amount = dictionary['amount']
      
      if amount < 0:
        # Calculating amount spent
        withdrawals += abs(amount)
    
    # Total withdrawals
    total_withdrawals += withdrawals
    list_withdrawals.append(withdrawals)

  # Calculating percents
  for w in list_withdrawals:
    percent = int(w / total_withdrawals * 10)
    percents.append(percent)

  # Top of the graph
  for p in percents:

    for char in range(10 - p):
      scale[char] = scale[char] + "   "

    for char in range(p + 1):
      scale[char + (10 - p)] = scale[char + (10 - p)] + ("o  ")

  for char in range(11):
    scale[char] = scale[char] + ("\n")

  scale.append('    -' + len(list_withdrawals) * '---' + '\n')

  # Finding the longest name
  name_length = 0
  name_list = list()
  
  for category in categories:
    if len(category.name) > name_length:
      name_length = len(category.name)

  # Printing names
  for category in categories:
    i = 0
    for char in range(name_length):
      name_list.append("     ")
      
      if i < len(category.name):
        name_list[char] += category.name[i] + '  '
        i += 1
        
      else:
        name_list[char] += '   '
  
  for i in range(len(name_list)):
    name_list[i] += '\n'
  
  names = ''.join(name_list)
  scale.append(names)
  chart = ''.join(scale)
  chart = chart.rstrip()
  chart = title + chart + '  '
  
  return chart