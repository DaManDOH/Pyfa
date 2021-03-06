#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import threading
import eos.types
class PrefetchThread(threading.Thread):
    def run(self):
        # We're a daemon thread, as such, interpreter might get shut down while we do stuff
        # Make sure we don't throw tracebacks to console
        try:
            eos.types.Character.setSkillList(eos.db.getItemsByCategory("Skill", eager=("effects", "attributes", "attributes.info.icon", "attributes.info.unit", "icon")))
        except:
            pass

prefetch = PrefetchThread()
prefetch.daemon = True
prefetch.start()
