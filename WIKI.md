# VibeyMapTools Wiki

Welcome to the VibeyMapTools documentation hub. This wiki provides an overview of the project and links to detailed documentation.

---

## 📚 Documentation Index

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
| **maputil** | [maputil.rst](docs/maputil.rst) | Map file Lua scripting tool |
| **lightpreview** | [lightpreview.rst](docs/lightpreview.rst) | Real-time lighting preview (experimental) |

### Full Documentation
The complete documentation is available in the [`docs/`](docs/) folder and at: **[github.com/themuffinator/VibeyMapTools](https://github.com/themuffinator/VibeyMapTools)**

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

## ✨ Key Features

### GPU Raytracing (`-gpu`)
Leverages NVIDIA OptiX for massively parallel raytracing. Requires:
- NVIDIA GPU with RTX cores
- CUDA Toolkit
- OptiX SDK 7.x

### AI Denoising (`-denoise`)
Uses Intel Open Image Denoise (OIDN) to clean up stochastic noise in lightmaps. Best used with high sample counts or bounce lighting.

### Bounce Lighting (`-bounce N`)
Simulates indirect illumination by bouncing light off surfaces. Higher values = more realistic but slower.

### HDR Lightmaps (`-lithdr`)
Generates high dynamic range lightmaps in LIGHTING_E5BGR9 format for engines that support it.

### Surface Lights (`_surface`)
Turn any texture into an emissive light source by specifying the texture name in a light entity's `_surface` key.

### Stochastic Sampling (`-stochastic`)
Randomized sampling for complex scenes - trades some noise for significantly faster compile times.

---

## 🎮 Game Support

| Game | Status |
|------|--------|
| **Quake** | ✅ Full support |
| **Quake II** | ✅ Full support (use `-q2bsp`) |
| **Quake II Remaster** | ✅ Supported (`-lightgrid`, etc.) |
| **Hexen II** | ✅ Supported |
| **Half-Life** | ⚠️ Experimental |

---

## 🔧 Common Workflows

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

## 📖 Additional Resources

- **Issue Tracker**: Report bugs and request features on GitHub
- **Discord**: Join the Quake Mapping Discord for community support
- **func_msgboard**: Classic Quake mapping community forum

---

## 📜 License

VibeyMapTools is licensed under the [GNU General Public License v3](COPYING).

Based on [ericw-tools](https://github.com/ericwa/ericw-tools) by Eric Wasylishen.
