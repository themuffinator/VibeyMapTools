# Changelog

All notable changes to VibeyMapTools are documented here.

For the detailed changelog with full technical details, see the [docs/changelog.rst](docs/changelog.rst) file.

---

## [2.1.0] - Current

This release continues the VibeyMapTools fork with rebranding and modernization.

### Features
- **vmt-bsp**: Half-Life `!cur_*` current contents support (`CONTENTS_CURRENT_*`)

### Changed
- Project rebranded from ericw-tools to VibeyMapTools (VMT)
- All executables now prefixed with `vmt-` for clarity
- License updated to GPL v3
- Build: tag-aware SemVer metadata and release packaging automation

---

## [2.0.0-alpha11] - Unreleased

### Features
- **vmt-light**: Support Half-Life style `light` fields with `r g b brightness` or `r g b` format
- **lightpreview**: Added lightgrid visualization ("Draw Lightgrid" checkbox)

### Bug Fixes
- **vmt-light**: Fix `_bouncecolorscale` being ignored when specified via worldspawn key
- **vmt-light**: Fix using `delay 4` (local minlight) + `_light_channel_mask` together

---

## [2.0.0-alpha10]

### Changes
- **vmt-bsp**: `.texinfo.json` file is now always written
- **vmt-light**: Switchable shadow casters now self-shadow when switched off

### Features
- **vmt-vis**: Support `_noambient` on func_group to disable ambient sounds
- **vmt-light**: Allow `-hdr`, `-bspxhdr`, `-lux`, `-bspxlux` on Q2 BSPs (experimental)

### Bug Fixes
- **vmt-bsp**: Fix `func_detail_fence` causing "grey flash" on some engines
- **vmt-light**: Fix lighting of faces embedded inside `func_detail_fence`
- **vmt-light**: Better check for color content when generating `.lit` files

---

## [2.0.0-alpha9]

### Changes
- **vmt-bsp**: Never merge across liquids; deprecate `-nomergeacrossliquids`
- **vmt-bsp**: Remove treating `__TB_empty` as skip
- **vmt-bsp**: Deprecate `_chop` and replace with `_chop_order`

### Features
- **vmt-light**: Add `_surflight_atten` key for worldspawn/func_group/func_detail
- **vmt-light**: Add `_switchableshadow_target`
- **vmt-bsp**: Add `_hulls` bmodel key for omitting specific collision hulls
- **lightpreview**: Add "view -> move camera to" menu item

### Bug Fixes
- **vmt-bsp**: Fix bmodel bounds for mixed `clip` and non-`clip` brushes
- **vmt-bsp**: Fix software renderer compatibility
- **vmt-bsp**: Add support for Q2 re-release content flags
- **vmt-light**: Fix `_surflight_group`

---

## [2.0.0-alpha8]

### Changes
- **vmt-light**: Invalid "delay" settings are now warnings instead of fatal errors
- **vmt-bsp**: Q2: Write true leaf contents even if CONTENTS_SOLID is set

### Features
- **lightpreview**: Show leaf contents in status bar
- **vmt-light**: LIGHTING_E5BGR9 + HDR .lit support

### Bug Fixes
- **vmt-light**: Fix "mangle" on _sun 1 entities
- **vmt-light**: Fix sunlight artifacts
- **vmt-bsp**: Q2: Fix areaportals broken in alpha7

---

## [2.0.0-alpha7]

### Changes
- **vmt-light**: Q2: Opaque lit liquids receive light from both sides by default
- **vmt-bsp**: Remove broken `-transsky` feature

### Features
- **vmt-bsputil**: Added `--svg` export
- **lightpreview**: Add camera bookmarks, stats panel with BSP lump sizes

### Bug Fixes
- **vmt-bsp**: Fix "sides not found" warning spam on Q1 maps with sky
- **vmt-light**: Fix `-dirtdebug` causing `.lit` generation in Q2 mode
- **vmt-light**: Reduce excess memory use

---

## [2.0.0-alpha6]

### Changes
- **vmt-light**: Fix `-emissivequality high` incorrect brightness
- **vmt-bsp**: Liquids don't cause splits in perpendicular walls by default
- **packaging**: Remove "bin" subfolder from releases

### Bug Fixes
- Fix macOS builds broken since alpha1
- **lightpreview**: Package in macOS + Linux builds
- **vmt-light**: Fix `-bounce` shorthand
- **vmt-bsp**: Make Q2_SURF_ALPHATEST imply TRANSLUCENT + DETAIL
- **vmt-bsp**: Fix t-junc logic to avoid excessive welding

---

## [2.0.0-alpha5]

### Bug Fixes
- **vmt-bsp**: Fix for Q2 animated textures
- **vmt-bsp**: Fix leaks through detail
- **vmt-light**: Fix entire lightmap turning black when using _surface lights
- **vmt-light**: Fix excessive bouncing with lit water

### Enhancements
- **vmt-vis**: More performance (gmsp3v2.bsp: 18.2s → 10.6s)

---

## [2.0.0-alpha4]

### Bug Fixes
- **vmt-bsp**: Fix `-notex`
- **vmt-bsp**: Fix `func_detail_illusionary` and `misc_external_map` with `-wrbrushes`

### Enhancements
- **vmt-vis**: Major performance fixes (gmsp3v2.bsp: 153s → 18.5s)
- **vmt-light**: Performance fixes for large maps with point lights

---

## [2.0.0-alpha3]

### Bug Fixes
- **lightpreview**: Don't crash on Q1 maps with missing textures
- **vmt-light**: Fix broken sunlight in Q1 maps
- **vmt-bsp**: Q2: Fix corruption if texture name exceeds 31 chars

### New Features
- **lightpreview**: Add `.lit` file loading
- Initial **maputil** for manipulating .map files with Lua scripting
- **vmt-light**: Initial multiple bounce support with `_bounce`

---

## [2.0.0-alpha2]

Focus: Quake 2 support improvements.

### Bug Fixes
- Fix blown out lightmaps with bounce and lightstyles
- Fix lightstyles being deleted if map leaks
- Fix surface lights not illuminating back faces of lit water

### New Features
- `_light_twosided` bmodel key for two-sided surface lighting
- `_tex_saturation_boost` worldspawn key for Q2 vanilla tools emulation

---

## [2.0.0-alpha1]

First alpha release featuring **Quake 2 support**, including features for the remaster:
- `-lightgrid`
- `-world_units_per_luxel`
- `-wrnormals`

To compile Q2 maps, pass `-q2bsp` to vmt-bsp.

---

## Earlier Releases

For the complete history of earlier releases (v0.18.x and before), see:
- [docs/changelog.rst](docs/changelog.rst) - Full technical changelog
- [ericw-tools GitHub](https://github.com/ericwa/ericw-tools) - Original project

---

## Links

- [Documentation](docs/)
- [Building from Source](BUILDING.md)
- [Wiki](WIKI.md)
