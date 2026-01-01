<div align="center">

<img src="assets/img/banner_2x1.png" alt="VibeyMapTools Banner" width="800">

# VibeyMapTools (VMT)

**Modern BSP compilation tools for Quake engine mapping**

[![Build Status](https://img.shields.io/github/actions/workflow/status/themuffinator/VibeyMapTools/ci.yml?branch=main&style=flat-square)](../../actions)
[![Release](https://img.shields.io/github/v/release/themuffinator/VibeyMapTools?style=flat-square)](../../releases)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue?style=flat-square)](COPYING)

[**Download**](../../releases) · [**Documentation**](docs/) · [**Wiki**](WIKI.md) · [**Changelog**](CHANGELOG.md)

</div>

---

## 🛠️ Tools

<table>
<tr>
<td width="120"><b>vmt-bsp</b></td>
<td>Compile .map to .bsp</td>
</tr>
<tr>
<td><b>vmt-vis</b></td>
<td>Calculate PVS visibility</td>
</tr>
<tr>
<td><b>vmt-light</b></td>
<td>Calculate lightmaps with GPU acceleration</td>
</tr>
<tr>
<td><b>vmt-bspinfo</b></td>
<td>BSP information utility</td>
</tr>
<tr>
<td><b>vmt-bsputil</b></td>
<td>BSP manipulation utility</td>
</tr>
</table>

## ⚡ Quick Start

```bash
# Standard compilation
vmt-bsp mymap.map
vmt-vis mymap.bsp
vmt-light mymap.bsp

# High-quality with GPU acceleration
vmt-light -gpu -extra 4 -bounce 2 -denoise mymap.bsp
```

## ✨ Key Features

<table>
<tr>
<td width="50%">

**🎮 GPU Raytracing**
NVIDIA OptiX acceleration with `-gpu` flag

**🤖 AI Denoising**
Intel OIDN integration via `-denoise`

**📊 Stochastic Sampling**
Faster complex scenes with `-stochastic`

</td>
<td>

**⚡ Incremental Lighting**
Cache-based iteration with `-incremental`

**🌈 HDR Support**
High dynamic range lightmaps via `-lithdr`

**🎨 PBR Baking**
Normal map integration in lightmaps

</td>
</tr>
</table>

## 📦 Downloads

| Platform | Package |
|:--------:|---------|
| <img src="https://cdn.simpleicons.org/windows" width="16"> **Windows** | `vibeymaptools-windows-*.zip` |
| <img src="https://cdn.simpleicons.org/linux" width="16"> **Linux** | `vibeymaptools-linux-*.tar.gz` |
| <img src="https://cdn.simpleicons.org/apple" width="16"> **macOS** | `vibeymaptools-macos-*.tar.gz` |

➡️ [**Latest Release**](../../releases/latest)

## 🔧 Building from Source

```bash
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools && cmake -B build && cmake --build build
```

<details>
<summary><b>Requirements</b></summary>

- CMake 3.14+
- C++20 compiler (MSVC 2019+, GCC 9+, Clang 10+)
- Intel Embree (recommended)

**Optional:**
- CUDA + OptiX SDK (GPU raytracing)
- Intel OIDN (AI denoising)

</details>

See [**BUILDING.md**](BUILDING.md) for detailed instructions.

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [BUILDING.md](BUILDING.md) | Build instructions, versioning, CI/CD |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |
| [WIKI.md](WIKI.md) | Documentation hub and quick reference |
| [docs/](docs/) | Full tutorials and reference |

## 📜 License

GPL v3 — See [COPYING](COPYING)

<div align="center">
<sub>
Based on <a href="https://github.com/ericwa/ericw-tools">ericw-tools</a> by Eric Wasylishen
</sub>
</div>

