from typing import List, Dict

"""
[
  ["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
  ["3","0","2","1","0"],
  ["5","0","1","0","1"],
  ["10","1","0","0","0"]
]
"""

def get_unique_foods_or_tables(orders: List[List[str]], idx: int) -> List[str]:
  unique: List[str] = []
  for order in orders:
    if not (order[idx] in unique):
      unique.append(order[idx])
  return unique

def count_foods_by_table(foods: List[str], tables: List[int], orders: List[List[str]]):
  counter: Dict[str, Dict[str, int]] = {}
  for table in tables:
    if not (str(table) in counter):
      counter[str(table)] = {}
      for food in foods:
        if not (food in counter[str(table)]):
          counter[str(table)][food] = 0

  for order in orders:
    counter[order[1]][order[2]] += 1

  return counter


def cast_str_to_num(to_cast: List[str]) -> List[int]:
  result: List[int] = []
  for num in to_cast:
    result.append(int(num))
  return result

def transform_orders_to_display_table(orders: List[List[str]]):
  foods = sorted(get_unique_foods_or_tables(orders, 2))
  tables = sorted(cast_str_to_num(get_unique_foods_or_tables(orders, 1)))
  display_table: List[List[str]] = [
    ["Table"] + foods
  ]

  for table in tables:
    row = [str(table)] + ["0"] * len(foods)
    display_table.append(row)

  counter = count_foods_by_table(foods, tables, orders)


  for i in range(len(display_table)):
    for j in range(len(display_table[i])):
      if i > 0 and j != 0:
        food = display_table[0][j]
        table = display_table[i][0]
        display_table[i][j] = str(counter[table][food])


  return display_table



def main():
  orders = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
  ]
  display_table = transform_orders_to_display_table(orders)
  print(display_table)


main()
