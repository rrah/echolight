"""Dummy indicator that logs stuff when things happen.

Author: Robert Walker <rrah99@gmail.com>

Copyright (C) 2015 Robert Walker

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; version 2.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import indicators.indicator
import logging


logger = logging.getLogger(__name__)


class Device(indicators.indicator.Indicator):
    
    """Pretends to be an indicator so stuff can be tested."""
    
    def _report(self, msg):
        
        logger.info(msg)
        
    def flashing_start(self, colours, flash_speed):
        
        """Report the start of flashing.
        
        Arguements:
            colours: Doesn't matter, ignored.
            flash_speed: Doesn't matter, ignored.
        """
        
        self._report('Starting flashing')
        
    def flashing_stop(self):
        
        """Report the end of flashing."""
        
        self._report('Stopping flashing')
        
    def set_light(self, colour):
        
        """Report the setting of a colour."""
        
        self._report('Set to {}'.format(colour))
        
    def read_switch(self):
        
        """Never gonna give you UP, never gonna let you DOWN.
        
        Return:
            False. Always."""
        
        return False
    
    def set_brightness(self, brightness):
        
        """Baby, you light up my world.
        
        Arguements:
            brightness (int): Eh, basically ignored.
            
        Return:
            None.
        """
        
        pass