#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        known_payload = {
                "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        with patch.object(GithubOrgClient, 'org',
                          new_callable=unittest.mock.PropertyMock,
                          return_value=known_payload) as mock_org:
            client = GithubOrgClient("testorg")
            url = client._public_repos_url
            self.assertEqual(url, known_payload["repos_url"])
            mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()