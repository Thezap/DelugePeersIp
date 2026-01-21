# -*- coding: utf-8 -*-
# Copyright (C) 2026 Thezap <me@thezap.eu>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of PeersIps and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from __future__ import unicode_literals

import os

from deluge import component
from twisted.internet.task import LoopingCall
import logging
import logging.handlers

import deluge.configmanager
from deluge.core.rpcserver import export
from deluge.plugins.pluginbase import CorePluginBase

log = logging.getLogger(__name__)


class Core(CorePluginBase):
    def __init__(self, plugin_name):
        super().__init__(plugin_name)
        self.looping = None
        self.my_logger = logging.getLogger(plugin_name)
        self.my_logger.setLevel(logging.DEBUG)


    def enable(self):
        log.debug("initializing my plugin")
        self.looping = LoopingCall(self.loop)
        self.looping.start(interval=int(os.getenv("PEERS_IPS_INTERVAL", '10')))

        handler = logging.handlers.SysLogHandler(address=os.getenv("PEERS_IPS_LOG_PATH", '/dev/log'))
        self.my_logger.addHandler(handler)

    def loop(self):
        peers_list = []
        torrents = component.get("TorrentManager").torrents.items()
        for tk, tv in torrents:
            log.debug("Starting torrent %s, %s", tk, tv)
            peer_info = tv.get_peers()
            for peer in peer_info:
                log.debug("peer: %s", peer)
                ip, port = peer['ip'].rsplit(':', 1)
                self.my_logger.info(f"torrentid={tk} ip={ip}")



    def disable(self):
        pass

    def update(self):
        pass
