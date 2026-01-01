=======
vmt-vis
=======

Visibility Compiler — Compute PVS for a Quake BSP file
=======================================================

Synopsis
--------

.. code-block:: bash

   vmt-vis [OPTION]... BSPFILE

Description
-----------

:program:`vmt-vis` is the visibility compiler for VibeyMapTools. It calculates 
the Potentially Visible Set (PVS) for a BSP file, which determines what parts 
of the map can potentially be seen from any given location.

vmt-vis looks for a ``.prt`` file by stripping the file extension from BSPFILE 
(if any) and appending ".prt". It then calculates PVS information before updating 
the .bsp file, overwriting any existing PVS data.

This vis tool supports the PRT2 format for Quake maps with detail brushes. 
See the :doc:`qbsp` documentation for details.

.. note::

   Compiling a map (without the ``-fast`` parameter) can take a long time, even
   days or weeks in extreme cases. vmt-vis will attempt to write a state file
   every five minutes so that progress will not be lost in case the
   computer needs to be rebooted or an unexpected power outage occurs.

Options
-------

.. program:: vmt-vis

Logging Options
~~~~~~~~~~~~~~~

.. option:: -log

   Write log files. Enabled by default.

.. option:: -nolog

   Don't write log files.

.. option:: -verbose, -v

   Verbose output.

.. option:: -nopercent

   Don't output percentage messages.

.. option:: -nostat

   Don't output statistic messages.

.. option:: -noprogress

   Don't output progress messages.

.. option:: -nocolor

   Don't output color codes (for TB, etc).

.. option:: -quiet, -noverbose

   Suppress non-important messages (equivalent to :option:`-nopercent` :option:`-nostat`
   :option:`-noprogress`).

Performance Options
~~~~~~~~~~~~~~~~~~~

.. option:: -lowpriority [0]

   Run in a lower priority, to free up headroom for other processes.

.. option:: -threads n

   Set number of threads explicitly. By default vmt-vis will attempt to
   detect the number of CPUs/cores available.

.. option:: -fast

   Skip detailed calculations and calculate a very loose set of PVS
   data. Sometimes useful for a quick test while developing a map.

Game Options
~~~~~~~~~~~~

.. option:: -gamedir "relative/path" or "C:/absolute/path"

   Override the default mod base directory. If this is not set, or if it is relative, 
   it will be derived from the input file or the basedir if specified.

.. option:: -basedir "relative/path" or "C:/absolute/path"

   Override the default game base directory. If this is not set, or if it is relative, 
   it will be derived from the input file or the gamedir if specified.

.. option:: -filepriority archive | loose

   Which types of archives (folders/loose files or packed archives) are higher priority 
   and chosen first for path searching.

.. option:: -path "/path/to/folder" <multiple allowed>

   Additional paths or archives to add to the search path, mostly for loose files.

.. option:: -q2rtx

   Adjust settings to best support Q2RTX.

.. option:: -defaultpaths

   Whether the compiler should attempt to automatically derive game/base paths for
   games that support it. Enabled by default.

.. option:: -nodefaultpaths

   Opt out of :option:`-defaultpaths`.

Output Options
~~~~~~~~~~~~~~

.. option:: -noambientsky

   Disable ambient sound generation for textures with names beginning with 'SKY'.

.. option:: -noambientwater

   Disable ambient sound generation for textures with names beginning
   with ``*WATER`` or ``*04WATER``.

.. option:: -noambientslime

   Disable ambient sound generation for textures with names beginning
   with ``*SLIME``.

.. option:: -noambientlava

   Disable ambient sound generation for textures with names beginning
   with ``*LAVA``.

.. option:: -noambient

   Disable all ambient sound generation.

   .. seealso::

      :bmodel-key:`_noambient` for selectively disabling ambient sounds.

.. option:: -noautoclean

   Don't remove extra files on successful completion. Default is to remove them.

Advanced Options
~~~~~~~~~~~~~~~~

.. option:: -level n

   Select a test level from 0 to 4 for detailed visibility calculations.
   Lower levels are not necessarily faster in all cases. It is not
   recommended that you change the default level unless you are
   experiencing problems. Default 4.

.. option:: -visdist n
   
   Allow culling of areas further than n units.

.. option:: -nostate

   Ignore saved state files, for forced re-runs.

.. option:: -phsonly

   Re-calculate the PHS of a Quake II BSP without touching the PVS.


Model Entity Keys
-----------------

.. bmodel-key:: "_noambient" "1"

   Disables ambient sound emission from these specific brushes.


See Also
--------

* :doc:`qbsp` — BSP compiler
* :doc:`light` — Lighting compiler


Author
------

| Based on original work by id Software
| Kevin Shanahan (aka Tyrann) — http://disenchant.net
| Eric Wasylishen
| VibeyMapTools contributors


Reporting Bugs
--------------

Please post bug reports at https://github.com/themuffinator/VibeyMapTools/issues.

Improvements to the documentation are welcome and encouraged.


Copyright
---------

| Copyright © 2024 VibeyMapTools contributors
| Copyright © 2017 Eric Wasylishen
| Copyright © 2013 Kevin Shanahan
| Copyright © 1997 id Software

License GPLv3: GNU GPL version 3 or later
https://gnu.org/licenses/gpl-3.0.html

This is free software: you are free to change and redistribute it. 
There is NO WARRANTY, to the extent permitted by law.
