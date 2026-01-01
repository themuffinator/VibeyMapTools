# VibeyMapTools Wiki 📚✨

Welcome to the VibeyMapTools documentation hub. This page is your neon sign to the docs, the quick-start spells, and the "wait what does that flag do?" rabbit hole. 🐇🔮

---

## 🧭 Documentation Index

### Getting Started
| Document | Description |
|----------|-------------|
| [README.md](README.md) | Project overview and quick start |
| [BUILDING.md](BUILDING.md) | Compilation instructions for all platforms |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |

### Tool Reference
| Tool | Documentation | Description |
|------|---------------|-------------|
| **vmt-bsp** | [qbsp.rst](docs/qbsp.rst) | BSP compiler - converts .map to .bsp |
| **vmt-vis** | [vis.rst](docs/vis.rst) | Visibility compiler - calculates PVS |
| **vmt-light** | [light.rst](docs/light.rst) | Light compiler - calculates lightmaps |
| **vmt-bspinfo** | [bspinfo.rst](docs/bspinfo.rst) | BSP information utility |
| **vmt-bsputil** | [bsputil.rst](docs/bsputil.rst) | BSP manipulation utility |
| **vmt-maputil** | [maputil.rst](docs/maputil.rst) | Map file Lua scripting tool |
| **vmt-preview** | [lightpreview.rst](docs/lightpreview.rst) | Real-time lighting preview (experimental) |

### Full Documentation
The complete documentation is available in the [`docs/`](docs/) folder and at **github.com/themuffinator/VibeyMapTools**.

---

## 🔁 Coming from ericw-tools? TL;DR ✨

Same workflow, new name, bonus polish. The big changes are mostly naming + release tooling:

- `qbsp/vis/light` -> `vmt-bsp/vmt-vis/vmt-light`
- All binaries are `vmt-` prefixed to differentiate from ericw-tools (including `vmt-maputil` and `vmt-preview`)
- CI-built packages + semantic versioning
- Quake II + Remaster support is unchanged (`-q2bsp`, `-lightgrid`, `-world_units_per_luxel`)
- Upstream docs still apply: https://ericwa.github.io/ericw-tools/ 📚

**Rename cheat sheet (old -> new):**

| ericw-tools | VibeyMapTools |
|-------------|---------------|
| `qbsp` | `vmt-bsp` |
| `vis` | `vmt-vis` |
| `light` | `vmt-light` |
| `bspinfo` | `vmt-bspinfo` |
| `bsputil` | `vmt-bsputil` |
| `maputil` | `vmt-maputil` |
| `lightpreview` | `vmt-preview` |


---

## 🚀 Quick Start

### Basic Compilation
```bash
vmt-bsp mymap.map      # Compile geometry
vmt-vis mymap.bsp       # Calculate visibility
vmt-light mymap.bsp     # Calculate lighting
```

### High-Quality Lighting
```bash
vmt-light -extra4 -bounce 2 mymap.bsp
```

### GPU-Accelerated Lighting
```bash
vmt-light -gpu -extra4 -denoise mymap.bsp
```

---

## ✨ Feature Snacks

### GPU Raytracing (`-gpu`) ⚡
Leverages NVIDIA OptiX for massively parallel raytracing. Requires:
- NVIDIA GPU with RTX cores
- CUDA Toolkit
- OptiX SDK 7.x

### AI Denoising (`-denoise`) 🤖
Uses Intel Open Image Denoise (OIDN) to clean up stochastic noise in lightmaps. Best with high sample counts or bounce lighting.

### Incremental Lighting (`-incremental`) 🔁
Keeps caches so you can relight fast without reprocessing everything.

### Bounce Lighting (`-bounce N`) 💡
Simulates indirect illumination by bouncing light off surfaces. Higher values = more realistic but slower.

### HDR Lightmaps (`-hdr`) 🌈
Generates high dynamic range lightmaps for engines that support it.

### Surface Lights (`_surface`) 🌟
Turn any texture into an emissive light source by naming it in a light entity's `_surface` key.

### Stochastic Sampling (`-stochastic`) 🎲
Randomized sampling for complex scenes - trades some noise for significantly faster compile times.

---

## 🎮 Game Support

| Game | Status |
|------|--------|
| **Quake** | ✅ Full support |
| **Quake II** | ✅ Full support (`-q2bsp`) |
| **Quake II Remaster** | ✅ Supported (`-lightgrid`, etc.) |
| **Hexen II** | ✅ Supported |
| **Half-Life** | 🧪 Experimental |

---

## 🧪 Common Workflows

### For Quake Mappers
```bash
# Development (fast)
vmt-bsp mymap.map
vmt-vis -fast mymap.bsp
vmt-light mymap.bsp

# Release (high quality)
vmt-bsp mymap.map
vmt-vis mymap.bsp
vmt-light -extra4 -bounce 1 -soft mymap.bsp
```

### For Quake II Mappers
```bash
vmt-bsp -q2bsp mymap.map
vmt-vis mymap.bsp
vmt-light mymap.bsp
```

### For Q2 Remaster
```bash
vmt-bsp -q2bsp mymap.map
vmt-vis mymap.bsp
vmt-light -lightgrid -world_units_per_luxel 8 mymap.bsp
```

---

## 🛰️ Additional Resources

- **Issue Tracker**: Report bugs and request features on GitHub

---

## 🧾 License

VibeyMapTools is licensed under the [GNU General Public License v3](COPYING).

Based on [ericw-tools](https://github.com/ericwa/ericw-tools) by Eric Wasylishen.
