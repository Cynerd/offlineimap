productname = 'OfflineIMAP'
versionstr = "3.0.2"
revno = long('$Rev: 135 $'[6:-2])
revstr = "Rev %d" % revno
datestr = '$Date: 2002-07-17 14:57:07 -0500 (Wed, 17 Jul 2002) $'


versionlist = versionstr.split(".")
major = versionlist[0]
minor = versionlist[1]
patch = versionlist[2]
copyright = "Copyright (C) 2002 John Goerzen"
author = "John Goerzen"
author_email = "jgoerzen@complete.org"
description = "Disconnected Universal IMAP Mail Synchronization/Reader Support"
bigcopyright = """%(productname)s %(versionstr)s (%(revstr)s)
%(copyright)s <%(author_email)s>""" % locals()

banner = bigcopyright + """
This software comes with ABSOLUTELY NO WARRANTY; see the file
COPYING for details.  This is free software, and you are welcome
to distribute it under the conditions laid out in COPYING."""

homepage = "http://www.quux.org/devel/offlineimap"
homegopher = "gopher://quux.org/1/devel/offlineimap"
license = """Copyright (C) 2002 John Goerzen <jgoerzen@complete.org>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA"""

cmdhelp = """
       offlineimap [ -1 ] [ -a accountlist ] [ -c configfile ]
       [ -d ] [ -u interface ]

       offlineimap -h | --help

       -1     Disable   all  multithreading  operations  and  use
              solely a single-thread sync.  This effectively sets
              the maxsyncaccounts and all maxconnections configu-
              ration file variables to 1.

       -a accountlist
              Overrides the accounts section in the config  file.
              Lets  you  specify  a  particular account or set of
              accounts to sync without having to edit the  config
              file.   You  might  use  this  to  exclude  certain
              accounts, or to sync some accounts  that  you  nor-
              mally prefer not to.

       -c configfile
              Specifies  a  configuration  file to use in lieu of
              the default, ~/.offlineimaprc.

       -d     Enables IMAP protocol stream and parsing debugging.
              This  is  useful  if you are trying to track down a
              malfunction or figure out what is  going  on  under
              the  hood.   I suggest that you use this with -1 in
              order to make the results more sensible.  Note that
              this  output  will  contain  full  IMAP protocol in
              plain text, including passwords, so  take  care  to
              remove  that from the debugging output before send-
              ing it to anyone else.

       -h, --help
              Show summary of options.

       -u interface
              Specifies an alternative user interface  module  to
              use.   This  overrides the default specified in the
              configuration file.  The UI specified with -u  will
              be  forced to be used, even if its isuable() method
              states that it cannot be.   Use  this  option  with
              care.
"""
