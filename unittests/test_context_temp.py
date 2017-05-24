import os
from unittest import TestCase

from context_temp import temp_directory, temp_file

# =============================================================================

class TestContexts(TestCase):
    def test_temp_dir(self):
        created_td = ''
        with temp_directory() as td:
            created_td = td
            name = os.path.join(td, 'a.txt')
            with open(name, 'w') as f:
                f.write('foo')

            os.path.isfile(name)

        # verify that the temp directory has been cleaned up
        self.assertFalse(os.path.exists(created_td))

        # -- test failure still cleans up
        try:
            with temp_directory() as td:
                created_td = td
                raise RuntimeError()
        except:
            pass

        self.assertFalse(os.path.exists(created_td))

    def test_temp_file(self):
        with temp_file() as filename:
            self.assertTrue(os.path.exists(filename))

        self.assertFalse(os.path.exists(filename))
