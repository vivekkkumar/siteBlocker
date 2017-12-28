import unittest
import os
import datetime
import shutil
import blocker.blocker


# Below is a simple unit test example template
# Test cases always should perform
# Arrange - creating= objects and dependencies etc,
# Act - implementing functionality,
# Assert - make claims like pass or fail.

class blockerTest(unittest.TestCase):           # subclass unittest mandatory

    def setUp(self):                            # need to create a backup file to not alter original file
                                                # if setup fails tear down will not be called.
        self.orig_file = 'some_dir'

        # creating a backup of the file

        self.filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
        self.bkp_file_path = self.os.path.dirname(self.orig_file)
        self.bkp_filename = os.path.join(self.bkp_file_path, self.filename)
        shutil.copy(self.bkp_file_path, self.bkp_filename)

    def test_create_blocker(self):                               # name of the test case
        self.appObject = blocker(17,23, ['www.facebook.com', 'www.google.com'])

    def test_missing_list_sites(self):
        with self.assertRaises(AttributeError):                  # Raises an key error and excepts.
            self.appObject = blocker(17, 23)

    @unittest.skip("WIP")                                        # Decorator with WIP message and the test is skipped
    def test_blocker_consistent(self):
        self.assertFalse(self.blocker.is_consistent())

    def test_blocker_method_block_sites(self):
        self.assertTrue(callable(self.appObject.block_sites))

    def tearDown(self):                                    # Again this is another fixture for cleaning some references,
                                                           # call this method at the last. We are creating a backup of /etc/hosts
                                                           # we replace the backup here after tests complete
        shutil.copy(self.bkp_file_path, self.orig_file)