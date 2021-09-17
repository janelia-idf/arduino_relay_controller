"""
Copyright 2013 Peter Polidoro

This file is part of arduino_relay_controller.

arduino_relay_controller is free software: you can redistribute it
and/or modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.

arduino_relay_controller is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with arduino_relay_controller.  If not, see
<http://www.gnu.org/licenses/>.  """

from distutils.core import setup


setup(
    name='arduino_relay_controller',
    version='0.1.0',
    author='Peter Polidoro',
    author_email='peter@polidoro.io',
    packages=['arduino_relay_controller',
              # 'arduino_relay_controller/gui',
              # 'arduino_relay_controller/webserver',
              ],
    scripts=['bin/arduino_relay_controller_cli.py',
             # 'bin/arduino_relay_controller_gui.py',
             # 'bin/arduino_relay_controller_webserver.py',
             ],
    # package_data={'arduino_relay_controller/webserver':['templates/*.html',
    #                                                  'static/*.css',
    #                                                  'static/js/jquery/*.js',
    #                                                  'static/js/scripts/*.js',
    #                                                  ],
    #               },
    url='https://bitbucket.org/peterpolidoro/arduino_relay_controller',
    license='LICENSE.LESSER.txt',
    description='Software to control the Arduino relay controllers.',
    long_description=open('README.txt').read(),
)
