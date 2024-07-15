import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def visualize_directory_structure(directory, indent=''):
  path = Path(directory)
  if not path.exists() or not path.is_dir():
    print(Fore.RED + 'Path not found')
    return
  
  print(Fore.BLUE + indent + path.name + '/')
  
  for item in sorted(path.iterdir()):
    if item.is_dir():
      visualize_directory_structure(item, indent + '    ')
    else:
      print(Fore.GREEN + indent + '    ' + item.name)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    directory = sys.argv[1]
    visualize_directory_structure(directory)
    