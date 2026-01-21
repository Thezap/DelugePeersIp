# -*- coding: utf-8 -*-
# Copyright (C) 2026 Thezap <me@thezap.eu>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of PeersIps and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from deluge.plugins.init import PluginInitBase


class CorePlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .core import Core as PluginClass
        self._plugin_cls = PluginClass
        super(CorePlugin, self).__init__(plugin_name)
