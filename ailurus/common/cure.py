#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
# Copyright (C) 2009-2010, Ailurus Developers Team
#
# Ailurus is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ailurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ailurus; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from __future__ import with_statement
import sys, os
if __name__ == '__main__':
    sys.path.insert(0, '/home/ds/workspace/Ailurus/ailurus')
from lib import *

class Autostart_Workrave(C):
    __doc__ = _('Automatically start up Workrave')
    path = os.path.expanduser('~/.config/autostart/')
    file = path + 'workrave.desktop'
    def exists(self):
        if UBUNTU or MINT:
            if APT.installed('workrave') and not os.path.exists(self.file):
                return True
        if FEDORA:
            if RPM.installed('workrave') and not os.path.exists(self.file):
                return True
        return False
    def cure(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.file, 'w') as f:
            f.write('[Desktop Entry]\n'
                    'Name=Workrave\n'
                    'Exec=workrave\n'
                    'Encoding=UTF-8\n'
                    'Version=1.0\n'
                    'Type=Application\n'
                    'X-GNOME-Autostart-enabled=true\n')

if __name__ == '__main__':
    obj = Autostart_Workrave()
    assert obj.exists()
    obj.cure()
    assert False == obj.exists()