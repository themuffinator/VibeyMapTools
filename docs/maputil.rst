=======
maputil
=======

MAP File Utility — Scripting and manipulation of Quake MAP files
=================================================================

Synopsis
--------

.. code-block:: bash

   maputil MAPFILE [OPTION]...

Description
-----------

:program:`maputil` is a utility for manipulating Quake .map files using Lua scripting.
It allows for complex transformations, queries, and format conversions on map data.

Options
-------

.. program:: maputil

.. option:: --script <path to Lua script file>

   Execute the given Lua script.

.. option:: --query \"<Lua expression>\"

   Perform a query on entities and print out matching results.
   See the Lua layout section for available globals.
   
   Note that query has the same access as script but is more suitable 
   for small read-only operations.

.. option:: --strip_extended_info

   Removes extended Quake II/III information on faces.

.. option:: --convert <quake | valve | etp | bp>

   Convert the current map to the given format:

   * ``quake`` — Quake vanilla format
   * ``valve`` — Valve 220 format
   * ``etp`` — Extended Texture Projection format
   * ``bp`` — Brush Primitives format

.. option:: --save \"<output path>\"

   Save the current map to the given output path.

.. option:: --game <quake | quake2 | hexen2 | halflife>

   Set the current game; used for certain conversions or operations.


Lua Data Layout
---------------

The Lua environment provides access to map data through the following structure:

.. code-block:: lua

   entities = table[]
    [E].dict = array
        [D] = [ key, value ]
    [E].brushes = table[]
     [S].texture = string
     [S].plane_points = [ [ x, y, z ] [ x, y, z ] [ x, y, z ] ]
     [S].raw = table (can only contain ONE member:)
         .quaked = table
          .shift = [ x, y ]
          .rotate = number
          .scale = [ x, y ]
         .valve = table
          .axis = [ [ x, y, z ] [ x, y, z ] ]
          .shift = [ x, y ]
          .rotate = number
          .scale = [ x, y ]
         .bp = table
          .axis = [ [ x, y, z ] [ x, y, z ] ]
         .etp = table
          .shift = [ x, y ]
          .rotate = number
          .scale = [ x, y ]
          .tx2 = boolean
     [S].info = table or nil
         .contents = number
         .value = number
         .flags = number
     [S].plane = [ x, y, z, d ] (read-only)
     [S].vecs = [ [ x, y, z, d ] [ x, y, z, d ] ] (read-only)


Usage Examples
--------------

.. code-block:: bash

   # Query all entities with a specific classname
   maputil mymap.map --query "return entities:filter(function(e) return e.dict.classname == 'light' end)"

   # Convert map to Valve 220 format
   maputil mymap.map --convert valve --save mymap_valve.map

   # Run a custom Lua script
   maputil mymap.map --script transform.lua --save mymap_modified.map


See Also
--------

* :doc:`qbsp` — BSP compiler
* :doc:`bsputil` — BSP manipulation


Author
------

| VibeyMapTools contributors


Reporting Bugs
--------------

Please post bug reports at https://github.com/themuffinator/VibeyMapTools/issues.

Improvements to the documentation are welcome and encouraged.


Copyright
---------

| Copyright © 2024 VibeyMapTools contributors

License GPLv3: GNU GPL version 3 or later
https://gnu.org/licenses/gpl-3.0.html

This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
