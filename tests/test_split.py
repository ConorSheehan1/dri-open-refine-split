import unittest

from split import process_file
from split import setup_params

# handle python 2 v 3 cases
try:
  FileNotFoundError
except:
  FileNotFoundError = IOError

class ProcessFile(unittest.TestCase):
  def test_process_file_not_found(self):
    with self.assertRaises(FileNotFoundError) as context:
      process_file('asdf', 'asdf')

    self.assertTrue("No such file or directory: 'asdf'" in str(context.exception)) 


# class ProcessFile(unittest.TestCase):
#   def test_cli_args(self):
#     pass

#   def test_gui_args(self):
#     pass

if __name__ == '__main__':
    unittest.main()
