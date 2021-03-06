#!/usr/bin/env python
#######################################
# Installation module for Keepnote
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update "

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/mdrasmus/keepnote.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="keepnote"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python-gnome2-extras-dev,aspell,aspell-en,python,python-gtk2,python-glade2,libgtk2.0-dev,libsqlite3-0"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install --prefix={INSTALL_LOCATION}"
