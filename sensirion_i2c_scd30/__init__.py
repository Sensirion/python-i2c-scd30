#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from .version import version as __version__  # noqa: F401

from sensirion_i2c_scd30.device import Scd30Device  # noqa: F401

__all__ = ['Scd30Device']
