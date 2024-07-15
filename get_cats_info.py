def get_cats_info(path):
  cats = []
  try:
    with open(path, 'r',encoding='utf-8') as file:
      lines = file.readlines()
      for line in lines:
        cat_info = line.strip().split(',')
        cats.append({
          'id': cat_info[0],
          'name': cat_info[1],
          'age': cat_info[2],
        })
  except FileNotFoundError:
    print('File not found')
  return cats

cats_info = get_cats_info('files/cats.txt')

print(cats_info)