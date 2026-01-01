==========
vmt-bsputil
==========

BSP Manipulation Utility — Modify and inspect Quake BSP files
==============================================================

Synopsis
--------

.. code-block:: bash

   vmt-bsputil [OPTION]... BSPFILE

Description
-----------

:program:`vmt-bsputil` is a utility for in-place manipulation of Quake BSP files.
It provides various operations for modifying, converting, extracting, and 
inspecting BSP data.

Options
-------

.. program:: vmt-bsputil

Scaling
~~~~~~~

.. option:: --scale x y z

   Scale the .bsp by the given scale factors.

   This is experimental, only a few entity properties are edited:

   - ``origin``
   - ``lip``
   - ``height``

Entity Operations
~~~~~~~~~~~~~~~~~

.. option:: --replace-entities ENTFILE

   Replaces the .bsp's entity lump with the contents of ENTFILE.

   .. note::
   
      This can also handle BSPFILE being a path to a .MAP file,
      updating one map file given the entities in a second, ENTFILE.

.. option:: --extract-entities

   Extract the entity data from *BSPFILE* and create a plain text
   .ent file. The output filename is generated from *BSPFILE* by
   stripping the .bsp extension and adding the .ent extension.

Format Conversion
~~~~~~~~~~~~~~~~~

.. option:: --convert FORMAT

   Convert the input .bsp to one of the given formats:

   * ``bsp29`` — Standard Quake BSP
   * ``bsp2`` — Extended BSP2 format
   * ``bsp2rmq`` — RMQ engine BSP2 format
   * ``hexen2`` — Hexen II BSP
   * ``hexen2bsp2`` — Hexen II BSP2 format
   * ``hexen2bsp2rmq`` — Hexen II BSP2 RMQ format
   * ``hl`` — Half-Life BSP
   * ``q2bsp`` — Quake II BSP
   * ``qbism`` — Qbism extended Q2 BSP

   .. warning::
   
      This is a "container" conversion only, so most conversions will not be usable.

Texture Operations
~~~~~~~~~~~~~~~~~~

.. option:: --extract-textures

   Extract the texture data from *BSPFILE* and create a Quake WAD
   file. The output filename is generated from *BSPFILE* by
   stripping the .bsp extension and adding the .wad extension.

.. option:: --replace-textures WADFILE

   Replace any textures in *BSPFILE* with updated versions from *WADFILE*.

   .. note::

      A warning will be issued if any texture sizes don't match between
      *BSPFILE* and *WADFILE*.

Decompilation
~~~~~~~~~~~~~

.. option:: --decompile

   Decompile *BSPFILE* to ``BSPFILE.decompile.map``.

.. option:: --decompile-geomonly

   Decompile *BSPFILE* to ``BSPFILE.decompile.map`` without texturing.

.. option:: --decompile-ignore-brushes

   Decompile *BSPFILE* to ``BSPFILE.decompile.map`` without using the Q2 brushes lump.

.. option:: --decompile-hull N

   Decompile only the given hull number to ``BSPFILE.decompile.hullN.map``.

BSPX Lump Operations
~~~~~~~~~~~~~~~~~~~~

.. option:: --extract-bspx-lump LUMPNAME OUTFILENAME

   Write the BSPX lump *LUMPNAME* to *OUTFILENAME*.

.. option:: --insert-bspx-lump LUMPNAME INFILENAME

   Read *INFILENAME* and insert it as a BSPX lump *LUMPNAME* in *BSPFILE*.

.. option:: --remove-bspx-lump LUMPNAME

   Removes *LUMPNAME* from *BSPFILE*.

Inspection and Debugging
~~~~~~~~~~~~~~~~~~~~~~~~

.. option:: --check
   
   Load *BSPFILE* into memory and run a set of tests to check that
   all internal data structures are self-consistent. Currently the tests
   are very basic and not all warnings will result in errors from all
   versions of the Quake engine. This option is not targeted at level
   designers, but is intended to assist with development of the vmt-bsp
   tool and check that a "clean" bsp file is generated.

.. option:: --modelinfo

   Print some information on all models in the .bsp.

   .. deprecated:: 2.0
      Use the .json export of :doc:`bspinfo` instead.

.. option:: --findfaces x y z nx ny nz

   Find faces with the given x, y, z coordinates inside the face, and
   the face having the given normal nx, ny, nz.

.. option:: --findleaf x y z

   Prints the leaf at the given coordinates.

.. option:: --settexinfo facenum texinfonum

   Change the texinfo of a given face.

Export Options
~~~~~~~~~~~~~~

.. option:: --svg

   Writes a top-down SVG rendering of *BSPFILE*.


Usage Examples
--------------

.. code-block:: bash

   # Extract entities to a .ent file
   vmt-bsputil --extract-entities mymap.bsp

   # Replace textures from a WAD file
   vmt-bsputil --replace-textures newtextures.wad mymap.bsp

   # Decompile a BSP to a .map file
   vmt-bsputil --decompile mymap.bsp

   # Convert BSP format
   vmt-bsputil --convert bsp2 mymap.bsp


See Also
--------

* :doc:`qbsp` — BSP compiler
* :doc:`bspinfo` — BSP information utility
* :doc:`maputil` — MAP file manipulation


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
