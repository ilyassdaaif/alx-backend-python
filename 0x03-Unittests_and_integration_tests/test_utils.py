#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    def test_memoize(self):
        """Test that when calling a_property twice,
        a_method is only called once"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42
        ) as mock_method:
            test_obj = TestClass()

            # First call
            result1 = test_obj.a_property

            # Second call
            result2 = test_obj.a_property

            # Assertions
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
