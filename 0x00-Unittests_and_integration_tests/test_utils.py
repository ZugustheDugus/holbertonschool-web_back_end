#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Dict, Sequence, Any, Callable


class TestAccessNestedMap(unittest.TestCase):
    """
    testing class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expect: Any
                               ):
        """
        test access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expect)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expect: Any
                                         ):
        """
        test access nested map exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(expect, e.exception)


class TestGetJson(unittest.TestCase):
    """
    test get json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_get: Callable):
        """
        test get json
        """
        mock_get.return_value.json.return_value = test_payload
        output = get_json(test_url)
        self.assertEqual(output, test_payload)


class TestMemoize(unittest.TestCase):
    """
    test memoize
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:
            """
            test class
            """
            def a_method(self):
                """
                a method
                """
                return 42

            @memoize
            def a_property(self):
                """
                a property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
