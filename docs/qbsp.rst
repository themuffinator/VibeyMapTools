=======
vmt-bsp
=======

BSP Compiler — Compile .map to .bsp
===================================

Synopsis
--------

.. code-block:: bash

   vmt-bsp [OPTION]... SOURCEFILE [DESTFILE]

Description
-----------

:program:`vmt-bsp` is the BSP compiler for VibeyMapTools. It takes a ``.map`` file 
as input and produces a ``.bsp`` file playable in Quake-family engines.

If the ``DESTFILE`` argument is not supplied, the output filename will be chosen 
by stripping the file extension from ``SOURCEFILE`` and appending ``.bsp``.

Supported Games
---------------

* **Quake** — Default mode
* **Quake II** — Use :option:`-q2bsp`
* **Hexen II** — Use :option:`-hexen2`
* **Half-Life** — Use :option:`-hlbsp` (experimental)

Options
-------

.. program:: vmt-bsp

General Options
~~~~~~~~~~~~~~~

.. option:: -verbose, -v

   Print out more .map information.

   Note, this switch no longer implies :option:`-loghulls`; use that if you want to see
   statistics for collision hulls.

.. option:: -quiet, -noverbose

   Suppress non-important messages (equivalent to :option:`-nopercent` :option:`-nostat` :option:`-noprogress`).

.. option:: -log

   Write log files. Enabled by default.

.. option:: -nolog

   Don't write log files.

.. option:: -nopercent

   Prevents output of percent completion information.

.. option:: -nostat

   Don't output statistic messages.

.. option:: -noprogress

   Don't output progress messages.

.. option:: -nocolor

   Don't output ANSI color codes (in case the terminal doesn't recognize colors, e.g. TB).

.. option:: -threads n

   Set number of threads to use. By default, vmt-bsp will attempt to use all available hardware threads.

.. option:: -lowpriority

   Run in a lower priority, to free up headroom for other processes. Enabled by default.

BSP Format Options
~~~~~~~~~~~~~~~~~~

.. option:: -q2bsp

   Target Quake II and the vanilla Q2BSP format, automatically switching to Qbism format
   if necessary (unless :option:`-noallowupgrade` is specified.)

.. option:: -qbism

   Target Quake II and use Qbism's extended Quake II BSP format.

.. option:: -q2rtx

   Adjust settings to best support Q2RTX.

.. option:: -hexen2

   Generate a Hexen II bsp. This can be used in addition to :option:`-bsp2` to avoid
   clipnode issues.

.. option:: -bsp2

   Create the output BSP file in BSP2 format. Allows the creation of
   much larger and more complex maps than the original BSP29 format.

.. option:: -2psb

   Create the output BSP file in 2PSB format. This is an earlier version of
   the BSP2 format, supported by the RMQ engine.

   .. deprecated:: 1.0
      Use :option:`-bsp2` instead.

.. option:: -hlbsp

   Create the output BSP file in Half-Life's format. Note that the hull
   size differences prevent this from being generally usable for the
   vanilla Quake gamecode. This cannot be used in combination with :option:`-bsp2`.

.. option:: -allowupgrade

   Allow formats to "upgrade" to compatible extended formats when a limit is
   exceeded (e.g. Quake BSP to BSP2, or Quake II BSP to Qbism BSP). Enabled by default.

.. option:: -noallowupgrade

   Opt out of :option:`-allowupgrade`.

Compilation Options
~~~~~~~~~~~~~~~~~~~

.. option:: -nofill

   Doesn't perform outside filling.

.. option:: -filltype auto | inside | outside

   Whether to fill the map from the outside in (lenient), from the inside out
   (aggressive), or to automatically decide based on the hull being used.

.. option:: -filldetail [n]

   Whether to fill enclosed pockets of empty space surrounded by solid detail. Default is 1 (enabled).

.. option:: -nomerge

   Don't perform face merging.

.. option:: -noedgereuse

   Don't reuse edges (may be useful for debugging software rendering).

.. option:: -noclip

   Doesn't build clip hulls (only applicable for Q1-like BSP formats).

.. option:: -noskip

   Doesn't remove faces using the :texture:`skip` texture.

.. option:: -nodetail

   Treat all detail brushes as structural.

.. option:: -onlyents

   Only updates .map entities.

.. option:: -loghulls

   Print log output for collision hulls.

.. option:: -logbmodels

   Print log output for bmodels.

.. option:: -chop

   Adjust brushes to remove intersections if possible. Enabled by default.

.. option:: -nochop

   Do not chop intersecting brushes.

.. option:: -chopfragment

   Always do full fragmentation for chop.

.. option:: -splitsky

   Doesn't combine sky faces into one large face.

.. option:: -splitspecial
   
   Doesn't combine sky and water faces into one large face. This allows
   for statically lit water.

.. option:: -litwater, -splitturb

   Enable lit liquids. This allows for statically lit water in compatible source ports,
   which still works but renders as fullbright on non-supporting source ports.
   The only downside is that water faces will be split up more, as per :option:`-subdivide`.
   Enabled by default.

.. option:: -transwater

   In Q1 mode, compiles maps for transparent water (lets vis see through liquids). Enabled by default.
   Has no effect in Q2 mode, because this is controlled by the mapper in Q2.

.. option:: -notranswater

   Computes portal information for opaque water.

.. option:: -oldaxis

   Use the original QBSP texture alignment algorithm. Enabled by default.

.. option:: -nooldaxis

   Use alternate texture alignment algorithm.

.. option:: -forcegoodtree

   Force use of expensive processing for SolidBSP stage. Often results
   in a more optimal BSP file in terms of file size, at the expense of
   extra processing time.

.. option:: -leaktest

   Makes it a compile error if a leak is detected.

Subdivision Options
~~~~~~~~~~~~~~~~~~~

.. option:: -subdivide [n]

   Use different texture subdivision (default 240). Lower values will
   harm framerates. Higher values may not be supported. DP+FTEQW+QSS
   support up to 4080 (unless lightmap scaling is in use), but such
   values will cause other engines to crash-to-console. Use zero to
   specify no subdivision.

.. option:: -nosubdivide

   Disable subdivision. Requires a compatible source port. See also :option:`-subdivide`.

.. option:: -lmscale n

   Change global lmscale (force :bmodel-key:`_lmscale` key on all entities).
   Outputs the LMSCALE BSPX lump.

WAD and Path Options
~~~~~~~~~~~~~~~~~~~~

.. option:: -wadpath <dir>

   Search this directory for wad files (default is cwd). Multiple
   :option:`-wadpath` args may be used. This argument is ignored for wads
   specified using an absolute path.

.. option:: -xwadpath <dir>

   Like :option:`-wadpath`, except textures found using the specified path will
   NOT be embedded into the bsp (equivalent to :option:`-notex`, but for only
   textures from specific wads).

.. option:: -path "/path/to/folder" <multiple allowed>

   Additional paths or archives to add to the search path, mostly for loose files.

.. option:: -defaultpaths

   Whether the compiler should attempt to automatically derive game/base paths for
   games that support it. Enabled by default.

.. option:: -nodefaultpaths

   Opt out of :option:`-defaultpaths`.

.. option:: -gamedir "relative/path" or "C:/absolute/path"

   Override the default mod base directory. If this is not set, or if it is relative, 
   it will be derived from the input file or the basedir if specified.

.. option:: -basedir "relative/path" or "C:/absolute/path"

   Override the default game base directory. If this is not set, or if it is relative, 
   it will be derived from the input file or the gamedir if specified.

.. option:: -filepriority archive | loose

   Which types of archives (folders/loose files or packed archives) are higher priority 
   and chosen first for path searching.

BSP Heuristics Options
~~~~~~~~~~~~~~~~~~~~~~

.. option:: -midsplitsurffraction n

   If 0 (default), use :option:`-maxnodesize` for deciding when to switch to midsplit bsp heuristic.

   If 0 < midsplitSurfFraction <= 1, switch to midsplit if the node contains more than this
   fraction of the model's total surfaces. Try 0.15 to 0.5. Works better than maxNodeSize for
   maps with a 3D skybox (e.g. ±128K unit maps).

.. option:: -midsplitbrushfraction n

   Switch to cheaper BSP partitioning test if a node contains this % of brushes in the map.

.. option:: -maxnodesize [n]

   Switch to the cheap spatial subdivision bsp heuristic when splitting
   nodes of this size (in any dimension). This gives much faster qbsp
   processing times on large maps and should generate better bsp trees.
   Default 1024, 0 to disable.

BSPX Options
~~~~~~~~~~~~

.. option:: -wrbrushes, -bspx

   Includes a list of brushes for brush-based collision. This
   allows for arbitrary collision sizes in engines that support it,
   currently only FTEQW.

.. option:: -wrbrushesonly, -bspxonly

   :option:`-wrbrushes` combined with :option:`-noclip` argument. This is NOT backwards
   compatible.

.. option:: -bmodelcontents

   Allow bmodels to have contents other than "solid" in Q1 based games,
   e.g. water in a func_door. This is supported in FTEQW; in winquake,
   the bmodel will have no collision.

   Q2 supports this feature natively and this option has no effect.

Texture Options
~~~~~~~~~~~~~~~

.. option:: -notex

   Write only placeholder textures, to depend upon replacements. This
   avoids inclusion of third-party copyrighted images inside your maps,
   but is not backwards compatible but will work in FTEQW and QSS.

   Note that the textures still need to be available to vmt-bsp.

   This only has effect in Q1 family games.

.. option:: -missing_textures_as_zero_size

   Writes missing textures (i.e. ones that vmt-bsp can't find) as 0x0 placeholders.

   This is not backwards compatible and will produce .bsp's that crash
   unsupporting engines. However, it can be useful when you want to run
   vmt-bsp + vmt-light on a map that you are missing the corresponding .wad for.

   This only has effect in Q1 family games.

T-Junction Options
~~~~~~~~~~~~~~~~~~

.. option:: -notjunc

   Alias for :option:`-tjunc none`

.. option:: -tjunc mwt | none | retopologize | rotate

   T-junction fix level:

   **none**
      Don't attempt to fix T-junctions. This is only for engines or formats
      that prefer micro-cracks over degenerate triangles.

   **rotate**
      Allow faces' vertices to be rotated to prevent zero-area triangles.

   **retopologize**
      If a face still has zero-area triangles, allow it to be re-topologized
      by splitting it into multiple fans.

   **mwt**
      Attempt to triangulate faces using a 
      `MWT <https://en.wikipedia.org/wiki/Minimum-weight_triangulation>`_
      first, only falling back to the prior two steps if it fails.

Detail Omission Options
~~~~~~~~~~~~~~~~~~~~~~~

.. option:: -omitdetail

   Detail brushes are omitted from the compile.

.. option:: -omitdetailwall

   :classname:`func_detail_wall` brushes are omitted from the compile.

.. option:: -omitdetailillusionary

   :classname:`func_detail_illusionary` brushes are omitted from the compile.

.. option:: -omitdetailfence

   :classname:`func_detail_fence` brushes are omitted from the compile.

Map Conversion Options
~~~~~~~~~~~~~~~~~~~~~~

.. option:: -convert <fmt>

   Convert a .MAP to a different .MAP format. fmt can be:

   **quake**
      Q1 vanilla map format.

   **quake2**
      Q2 vanilla map format.

   **valve**
      Valve 220 map format.

   **bp**
      Brush Primitives format.

   Conversions to "quake" or "quake2" format may not be able to match the texture 
   alignment in the source map, other conversions are lossless. The converted map 
   is saved to ``<source map name>-<fmt>.map``.

Miscellaneous Options
~~~~~~~~~~~~~~~~~~~~~

.. option:: -add [mapfile]

   The given map file will be appended to the base map.

.. option:: -leakdist [n]

   Space between leakfile points (default 0, which does not write any inbetween points).

.. option:: -oldrottex

   Use old method of texturing rotate\_ brushes where the mapper aligns
   textures for the object at (0 0 0).

.. option:: -software

   Change settings to allow for (or make adjustments to optimize for the lack of) software support.

.. option:: -nosoftware

   Explicitly drop support for software renderers.

.. option:: -notriggermodels

   For supported game code only: triggers will not write a model out,
   and will instead just write out their mins/maxs.

.. option:: -noextendedsurfflags

   Don't write .texinfo file, even if it would normally be needed (debug).

.. option:: -includeskip

   Emit skip/nodraw faces (default is to discard them). Mainly for Q2RTX.

.. option:: -aliasdef <aliases.def> [...]

   Adds alias definition files, which can transform entities in the .map into other entities.

.. option:: -texturedefs "path/to/file.def" <multiple allowed>

   Path to a texture definition file, which can transform textures in the .map into other textures.

.. option:: -epsilon n

   Customize epsilon value for point-on-plane checks.

.. option:: -microvolume n

   Microbrush volume.

.. option:: -maxedges n

   The max number of edges/vertices on a single face before it is split into another face. 
   0 means unlimited. Default is 0 for Q2, and 64 for Q1.

.. option:: -worldextent n

   Explicitly provide world extents; 0 will auto-detect. Default 0.

.. option:: -forceprt1

   Force a PRT1 output file even if PRT2 is required for vis.

Debug Options
~~~~~~~~~~~~~

.. option:: -outsidedebug

   Write a .map after outside filling showing non-visible brush sides.

.. option:: -debugchop

   Write a .map after ChopBrushes.

.. option:: -debugleak

   Write more diagnostic files for debugging leaks.

.. option:: -debugbspbrushes

   Save bsp brushes after BrushBSP to a .map, for visualizing BSP splits.

.. option:: -debugleafvolumes

   Save bsp leaf volumes after BrushBSP to a .map, for visualizing BSP splits.

.. option:: -debugexpand [single hull index] or [mins_x mins_y mins_z maxs_x maxs_y maxs_z]

   Write expanded hull .map for debugging/inspecting hulls/brush bevelling.

.. option:: -keepprt

   Avoid deleting the .prt file on leaking maps.

.. option:: -objexport

   Export the map file as .OBJ models during various compilation phases.


Game Path Specification
-----------------------

To compile a Q2 map, the compilers usually need to be able to locate an installation of the game. 
For example, the .map might reference a texture name like ``e1u1/clip``, but vmt-bsp needs to open 
the corresponding .wal file to look up the content/surface flags (playerclip, etc.) which are then 
written to the .bsp.

Terminology
~~~~~~~~~~~

**basedir**
   The directory containing the base game (e.g. ``id1`` or ``baseq2``). 
   Can be an absolute path, e.g. ``c:/quake2/baseq2`` or ``c:/quake/id1``.

**gamedir**
   Optional mod directory, e.g. ``ad`` or ``c:/quake/ad``. If a gamedir is specified 
   it will be added to the search path at a higher priority than the basedir.

Common Cases
~~~~~~~~~~~~

* Place your .map in ``<quake2>/baseq2/maps`` and compile it there — vmt-bsp will auto-detect the basedir/gamedir.

* For compiling a .map located elsewhere:

  .. code-block:: bash

     vmt-bsp -basedir "c:/quake2/baseq2" input.map

  or

  .. code-block:: bash

     vmt-bsp -basedir "c:/quake2/baseq2" -gamedir mymod input.map


Special Texture Names
---------------------

The contents inside a brush depend on the texture name(s) assigned to it.

By default brush contents are solid unless they have a special name.
All faces of a brush must have textures which indicate the same
contents. Mixed content types will cause vmt-bsp to print an error and exit.

Liquids
~~~~~~~

.. texture:: *slime
             *lava
             *

   In all Q1-like games, names beginning with an asterisk are liquids. A prefix of ``*slime``
   indicates slime, ``*lava`` is for lava, and anything else beginning with
   ``*`` will have contents as water.

.. texture:: !slime
             !lava
             !

   In all Q1-like games, for compatibility with Half-Life maps, names beginning with ``!`` 
   are treated the same as names beginning with ``*`` and create liquids.

Special Surfaces
~~~~~~~~~~~~~~~~

.. texture:: skip

   Any surfaces assigned a texture name of *skip* will be compiled into the
   bsp as invisible surfaces. Solid surfaces will still be solid (e.g. the
   player can't walk or shoot through them) but they will not be drawn.
   Water, slime and lava surfaces can be made invisible using the texture
   names *\*waterskip*, *\*slimeskip* and *\*lavaskip* respectively.

.. texture:: hint

   Hint surfaces cause a bsp split and portal to be generated on the
   surface plane, after which they are removed from the final bsp — they
   are neither visible, nor structural. Strategic placement of hint
   surfaces can be used by a map author to optimise the PVS calculations so
   as to limit overdraw by the engine (see also: :doc:`vis`).

   Use a texture with the name *hintskip* on any surfaces of a hint brush
   which you don't want to generate bsp splits or portals. All surfaces of
   a hint brush must use either the *hint* or *hintskip* texture name.

.. texture:: origin

   An origin brush (all faces textured with "origin") can be added to a
   brush entity (but not detail or compiler-internal entities like
   func_group). Doing so causes all of the brushes in the brush entity to
   be translated so the center of the origin brush lines up with 0 0 0. The
   entity key "origin" is then automatically set on the brush entity to the
   original coordinates of the center of the "origin" brush before it was
   translated to 0 0 0.

Half-Life BSP Specific
^^^^^^^^^^^^^^^^^^^^^^

.. texture:: !cur_0
             !cur_90
             !cur_180
             !cur_270
             !cur_up
             !cur_dwn

   These prefixes generate water with the given current direction:

   ===================== =====
   Content type          Value
   ===================== =====
   CONTENTS_CURRENT_0    -9
   CONTENTS_CURRENT_90   -10
   CONTENTS_CURRENT_180  -11
   CONTENTS_CURRENT_270  -12
   CONTENTS_CURRENT_UP   -13
   CONTENTS_CURRENT_DOWN -14
   ===================== =====

   During the BSP process, they act like water with extra modifier flags.

   .. note::

      Different from the vanilla HL compiler, we don't generate faces between different ``CONTENTS_CURRENT_*`` textured
      volumes.


External Map Prefab Support
---------------------------

This vmt-bsp has a prefab system using a point entity named ``misc_external_map``. 
The idea is, each ``misc_external_map`` imports brushes from an external .map file, 
applies rotations specified by the ``_external_map_angles`` key, then translates them 
to the "origin" key of the ``misc_external_map`` entity. Finally, the classname of the
``misc_external_map`` is switched to the one provided by the mapper in the
``_external_map_classname`` key. (The "origin" key is also cleared to "0 0 0" before 
saving the .bsp).

The external .map file should consist of worldspawn brushes only, although you can use 
func_group for editing convenience. Brush entities are merged with the worldspawn brushes 
during import. All worldspawn keys, and any point entities are ignored. Currently, this 
means that the "wad" key is not handled, so you need to add any texture wads required
by the external .map file to your main map.

.. other-key:: _external_map
   
   Specifies the filename of the .map to import.

.. other-key:: _external_map_classname
   
   What entity you want the external map to turn into. You can use
   internal vmt-bsp entity types such as :classname:`func_detail`, or a regular bmodel
   classname like "func_wall" or "func_door".

.. other-key:: _external_map_angles

   Rotation for the prefab, "pitch yaw roll" format. Assuming the
   external map is facing the +X axis, positive pitch is down. Yaw of
   180, for example, would rotate it to face -X.

.. other-key:: _external_map_angle

   Short version of :other-key:`_external_map_angles` for when you want to specify
   just a yaw rotation.

.. other-key:: _external_map_scale

   Scale factor for the prefab, defaults to 1. Either specify a single
   value or three scales, "x y z".


Detail Brush Support
--------------------

This version of vmt-bsp supports detail brushes which are similar in concept to 
Quake 2's detail brushes. They don't seal the map (previous versions did).

To be compatible with existing Quake 1 mapping tools, detail brushes can
be added by creating an entity with classname ``func_detail``. When vmt-bsp
reads the map file, it will add any brushes included in a func_detail
entity into the worldspawn as details and remove the func_detail entity.
Any number of func_detail entities can be used (useful for grouping) and
all included brushes will be added to the worldspawn.

When vmt-bsp detects detail brushes, it outputs a modified portal file
format with the header PRT2 (default is PRT1). This portal file contains
extra information needed by vmt-vis to compute the potentially visible set
(PVS) for the map/bsp.


Compiler-Internal Bmodels
-------------------------

.. classname:: func_group

   Bmodel that has no effect; vmt-bsp moves the brushes back into the worldspawn entity.

   The usefulness comes from the ability to set :ref:`model-entity-keys` on the brushes inside the func_group.

.. classname:: func_detail

   Solid detail. Can't be seen inside, splits world faces. Doesn't seal map.

.. classname:: func_detail_illusionary

   func_detail variant with no collision (players / monsters / gunfire) and
   doesn't split world faces. Doesn't cast shadows unless enabled with
   :bmodel-key:`_shadow` "1". Useful for hanging vines. Still creates BSP leafs, which
   is unavoidable without a new .bsp file format.

   Intersecting func_detail_illusionary brushes don't clip each other; this
   is intended to make trees/shrubs/foliage easier with :bmodel-key:`_mirrorinside` "1".

.. classname:: func_detail_wall

   func_detail variant that doesn't split world faces. Useful for when you
   want a decoration touching a floor or wall to not split the floor/wall
   faces (you'll get some overdraw instead.) If it completely covers up a
   world face, that face will get clipped away, so it's not suitable for
   fence textures; see func_detail_fence instead.

   Intersecting func_detail_wall brushes don't clip each other.

.. classname:: func_detail_fence

   Similar to func_detail_wall except it's suitable for fence textures, 
   never clips away world faces. Useful for fences, grates, etc., that are 
   solid and block gunfire.


See Also
--------

* :doc:`vis` — Visibility compiler
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
