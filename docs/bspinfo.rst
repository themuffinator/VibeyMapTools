==========
vmt-bspinfo
==========

BSP Information Utility — Print information about a Quake BSP file
===================================================================

Synopsis
--------

.. code-block:: bash

   vmt-bspinfo BSPFILE [BSPFILES]

Description
-----------

:program:`vmt-bspinfo` is a utility that prints various information about each .bsp file:

* BSP type
* List of BSP lumps, the number of objects, and the total size in bytes
* List of BSPX lumps and their sizes in bytes

Additional Outputs
~~~~~~~~~~~~~~~~~~

For the purpose of previewing lightmaps in Blender, vmt-bspinfo will also pack the 
lightmaps into an atlas and output the following:

* ``mapname.bsp.geometry.obj`` — BSP faces with lightmap UV coordinates
* ``mapname.bsp.lm_0.png``, ``mapname.bsp.lm_1.png``, etc. — Lightmap atlas per used style number

For debugging, the BSP is also converted into a JSON representation and written to 
``mapname.bsp.json``.


Usage Examples
--------------

.. code-block:: bash

   # Print info for a single BSP
   vmt-bspinfo mymap.bsp

   # Print info for multiple BSPs
   vmt-bspinfo map1.bsp map2.bsp map3.bsp


See Also
--------

* :doc:`qbsp` — BSP compiler
* :doc:`bsputil` — BSP manipulation utility


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
