# -*- coding: utf-8 -*-
#
# Copyright: (c) 2022, Cédric Servais <cedric.servais@outlook.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r"""
options:
  log_level:
    description:
      - The log level of the module
    required: false
    default: 'INFO'
    type: str
    choices:
    - 'CRITICAL'
    - 'FATAL'
    - 'ERROR'
    - 'WARN'
    - 'WARNING'
    - 'INFO'
    - 'DEBUG'
    - 'NOTSET'
"""
