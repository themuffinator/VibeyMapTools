================
vmt-preview
================

Real-Time Lighting Preview — GUI tool for interactive BSP compilation and visualization
========================================================================================

Description
-----------

:program:`vmt-preview` is a graphical tool that unifies :doc:`qbsp`, :doc:`vis`, 
and :doc:`light` with a 3D viewport for visualizing the output in real-time.

.. note::

   This tool is experimental and primarily packaged in the Windows build.
   Coming from ericw-tools? ``vmt-preview`` is the modernized successor to the
   classic lightpreview flow, with extra visibility and selection tooling.

Features
--------

* Real-time 3D preview of BSP geometry
* Interactive lighting visualization
* Multiple view modes for debugging
* Camera bookmarks
* Stats panel with BSP lump sizes
* Lightgrid visualization (for Q2 remaster maps)
* Support for .lit file loading

Previews
--------

The preview panel now covers much more than lightmaps. Enjoy a broader debugging
toolkit with quick visual feedback. 🎛️✨

* 🧭 **HUD overlay** with faces, leafs, portal counts, vis state, and selection info
* 🧱 **Portals and leaks**: auto-watch .prt/.pts/.lin and refresh as you iterate
* 🧲 **Selection ray** to confirm hit tests when clicking geometry
* 🎯 **Selection tools**: copy face + texture info, focus camera on face/leaf, solo a texture
* 🌈 **Lightgrid samples** listed in HUD when BSPX lightgrid data is present

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

* :kbd:`Alt-1` - Lightmapped (default)
* :kbd:`Alt-2` - Lightmap Only
* :kbd:`Alt-3` - Fullbright
* :kbd:`Alt-4` - Normals
* :kbd:`Alt-5` - Flat shading
* :kbd:`H` - Toggle HUD overlay (viewport focused)
* :kbd:`T` - Toggle solo selected texture


Usage
-----

.. code-block:: bash

   vmt-preview mymap.map

The tool will automatically compile the map and display it in the viewport.
Changes to lighting parameters can be previewed interactively.

Qt6 Setup
---------

`vmt-preview` builds when Qt6 is installed and ``ENABLE_LIGHTPREVIEW=ON``.
Required Qt6 components: Core, Gui, Widgets, OpenGL, OpenGLWidgets.

Example (Windows, Qt Online Installer):

.. code-block:: powershell

   cmake -B build -DENABLE_LIGHTPREVIEW=ON -DCMAKE_PREFIX_PATH="C:\Qt\6.6.2\msvc2019_64"

Example (macOS, Homebrew):

.. code-block:: bash

   brew install qt@6
   cmake -B build -DENABLE_LIGHTPREVIEW=ON -DCMAKE_PREFIX_PATH="$(brew --prefix qt@6)"

Example (Linux, Debian/Ubuntu):

.. code-block:: bash

   sudo apt install qt6-base-dev qt6-base-dev-tools libgl1-mesa-dev
   cmake -B build -DENABLE_LIGHTPREVIEW=ON


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
