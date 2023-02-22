import os
import json


def list_python_files(dir):
  for root, dirs, files in os.walk(dir):
    print(root)
    for name in list(dirs):
      if name.startswith('.'):
        dirs.remove(name)
    for file in files:
      if file.endswith('.py'):
        yield '/'.join(os.path.join(root, file).split(os.path.sep)[3:])


for root, dirs, files in os.walk('.'):
  for name in list(dirs):
    if name.startswith('.'):
      dirs.remove(name)

  if 'package.json' in files:
    with open(os.path.join(root, 'package.json'), 'r') as f:
      package = json.load(f)
      repository = package['repository']

      package['urls'] = [
        [os.path.join(root.split(os.path.sep)[-1], file), f'{repository}/src/{file}']
        for file in list_python_files(os.path.join(root, 'src'))
      ]
    with open(os.path.join(root, 'package.json'), 'w') as f:
      json.dump(package, f, indent=2)
