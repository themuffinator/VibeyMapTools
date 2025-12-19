.. VibeyMapTools documentation master file

==================================
VibeyMapTools Documentation
==================================

**VibeyMapTools** (VMT) is a modern BSP compilation toolset for Quake engine mapping.

.. note::
   
   This project is a fork of `ericw-tools <https://github.com/ericwa/ericw-tools>`_ 
   with rebranding, modernization, and continued development.

Quick Start
===========

.. code-block:: bash

   # Basic compilation
   vmt-bsp mymap.map
   vmt-vis mymap.bsp
   vmt-light mymap.bsp

   # High-quality lighting
   vmt-light -extra4 -bounce 2 -denoise mymap.bsp

Tool Reference
==============

.. toctree::
   :maxdepth: 2
   
   qbsp
   vis
   light
   bspinfo
   bsputil
   maputil
   lightpreview

Appendix
========

.. toctree::
   :maxdepth: 1

   changelog

Indices and Tables
==================

* :ref:`genindex`
* :ref:`search`

Links
=====

* `GitHub Repository <https://github.com/themuffinator/VibeyMapTools>`_
* `Issue Tracker <https://github.com/themuffinator/VibeyMapTools/issues>`_
* `Releases <https://github.com/themuffinator/VibeyMapTools/releases>`_
