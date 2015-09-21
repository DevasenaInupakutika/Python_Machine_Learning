#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os')
    @mock.patch('mymodule.os.path')

    def test_rm(self, mock_os):

        # Instantiate our service
        reference = RemovalService()

        # Set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")


        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")        
 
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
