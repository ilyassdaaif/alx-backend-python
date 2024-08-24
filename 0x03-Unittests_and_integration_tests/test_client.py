#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the expected
        list of repos.
        """
        # Define test payload
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        # Define expected result
        expected_repos = ["repo1", "repo2", "repo3"]

        # Mock _public_repos_url property
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test-org/repos"
        ) as mock_public_repos_url:
            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            self.assertEqual(repos, expected_repos)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )


if __name__ == "__main__":
    unittest.main()
