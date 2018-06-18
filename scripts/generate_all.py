import os
import subprocess

all_fnames = [
  'generate_SpeciesName_bind_test.py',
  'generate_UnitSystem_bind_test.py',
  'generate_DataType_bind_test.py',
  'generate_Numbering_bind_test.py',
  'generate_LanguageName_bind_test.py',
  'generate_ComputeCallbackName_bind_test.py',
]

dir_path = os.path.dirname(os.path.realpath(__file__))
for fname in all_fnames:
  fname = os.path.join(dir_path, fname)
  print('\nRunning script:\n{}\nto generate binding and test files.\n'.format(fname))
  subprocess.call(['python', fname])
