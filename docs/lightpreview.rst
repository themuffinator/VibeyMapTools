================
vmt-lightpreview
================

Real-Time Lighting Preview — GUI tool for interactive BSP compilation and visualization
========================================================================================

Description
-----------

:program:`vmt-lightpreview` is a graphical tool that unifies :doc:`qbsp`, :doc:`vis`, 
and :doc:`light` with a 3D viewport for visualizing the output in real-time.

.. note::

   This tool is experimental and primarily packaged in the Windows build.

Features
--------

* Real-time 3D preview of BSP geometry
* Interactive lighting visualization
* Multiple view modes for debugging
* Camera bookmarks
* Stats panel with BSP lump sizes
* Lightgrid visualization (for Q2 remaster maps)
* Support for .lit file loading

Controls
--------

Movement
~~~~~~~~

* :kbd:`W` :kbd:`A` :kbd:`S` :kbd:`D` — Fly movement (forward/left/back/right)
* :kbd:`Q` :kbd:`E` — Move down/up
* :kbd:`Arrow Keys` — Alternative movement
* :kbd:`Page Up` / :kbd:`Page Down` — Alternative up/down

View Modes
~~~~~~~~~~

* :kbd:`Alt-1` — Lightmapped (default)
* :kbd:`Alt-2` — Lightmap Only
* :kbd:`Alt-3` — Fullbright
* :kbd:`Alt-4` — Normals
* :kbd:`Alt-5` — Flat shading


Usage
-----

.. code-block:: bash

   vmt-lightpreview mymap.map

The tool will automatically compile the map and display it in the viewport.
Changes to lighting parameters can be previewed interactively.


See Also
--------

* :doc:`qbsp` — BSP compiler
* :doc:`vis` — Visibility compiler
* :doc:`light` — Lighting compiler


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