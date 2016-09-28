# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from moda.theme.testing import MODA_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that moda.theme is properly installed."""

    layer = MODA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if moda.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'moda.theme'))

    def test_browserlayer(self):
        """Test that IModaThemeLayer is registered."""
        from moda.theme.interfaces import (
            IModaThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IModaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MODA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['moda.theme'])

    def test_product_uninstalled(self):
        """Test if moda.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'moda.theme'))

    def test_browserlayer_removed(self):
        """Test that IModaThemeLayer is removed."""
        from moda.theme.interfaces import IModaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IModaThemeLayer, utils.registered_layers())
