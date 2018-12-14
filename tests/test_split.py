# functions being tested
from split import process_file
from split import setup_params

import sys
import argparse
import unittest
try:
    from unittest.mock import patch  # python 3.3+
except ImportError:
    from mock import patch  # python 2.6-3.2

# TODO drop support for 2.7?
# handle python 2 v 3 cases
try:
  FileNotFoundError
except:
  FileNotFoundError = IOError


class TestSplit(unittest.TestCase):
  # https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
  # output helper (hides pdb output too)
  def get_stdout(self):
    if not hasattr(sys.stdout, "getvalue"):
      self.fail("need to run in buffered mode")
    return sys.stdout.getvalue().strip()

  def test_process_file_not_found(self):
    with self.assertRaises(FileNotFoundError) as context:
      process_file('asdf', 'asdf')

    self.assertTrue("No such file or directory: 'asdf'" in str(context.exception)) 

  def test_setup_params_cli_args(self):
    filename = "./tests/fixtures/qdc1.xml"
    outputdir = "./tests/fixtures/out"
    args = argparse.Namespace(filename=filename, outputdir=outputdir)
    # args = ["--filename " + filename, " --outputdir " + outputdir]
    # with patch('argparse._sys.argv', args):
    with patch('argparse.ArgumentParser.parse_args',return_value=args):
      self.assertEqual((filename, outputdir), setup_params())
      output = self.get_stdout()
      self.assertTrue("Processing input file ./tests/fixtures/qdc1.xml" in output)
      self.assertTrue("Creating output xml files in ./tests/fixtures/out" in output)

  def test_setup_params_gui_args(self):
    # import pdb; pdb.set_trace()
    # gui = True
    pass
  

if __name__ == '__main__':
    unittest.main()
