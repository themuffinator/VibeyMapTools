# Building VibeyMapTools 🛠️🧃✨

This document describes how to build VibeyMapTools from source. Expect CMake, some dependencies, and a sprinkle of vibes. ✨

## 🔁 Coming from ericw-tools? Quick translation 🧭

Same workflow, new name, extra toys. If you used ericw-tools, this should feel instantly familiar.

| ericw-tools | VibeyMapTools |
|-------------|---------------|
| `qbsp` | `vmt-bsp` |
| `vis` | `vmt-vis` |
| `light` | `vmt-light` |
| `bspinfo` | `vmt-bspinfo` |
| `bsputil` | `vmt-bsputil` |
| `maputil` | `vmt-maputil` |
| `lightpreview` | `vmt-lightpreview` |

**Still the same (legacy comfy mode):**
- Quake II + Remaster support stays put (`-q2bsp`, `-lightgrid`, `-world_units_per_luxel`) 🧠🎮
- CLI flags, map formats, and output expectations
- Upstream docs still apply: https://ericwa.github.io/ericw-tools/ 📚

**VMT upgrades (build + release glow):**
- `vmt-` prefix on every binary so ericw-tools can live side-by-side 🧹✨
- Semantic versioning + tag-driven releases with CI-built packages 📦🚀
- Build metadata + `version.hh` for scripting and diagnostics 🧾🛠️


## 🧃 Prerequisites (the snack list)

### Required
- **CMake 3.14+**
- **C++20 compiler**:
  - Visual Studio 2019+ (Windows)
  - GCC 9+ (Linux)
  - Clang 10+ (macOS/Linux)
- **Git** (for submodules)
- **Intel Embree 4.x + oneTBB** (required for `vmt-light` builds)

### Optional extras (spicy toppings)
- **Qt6** (for `vmt-lightpreview`)
- **NVIDIA CUDA Toolkit** + **OptiX SDK 7.x** (GPU raytracing)
- **Intel Open Image Denoise (OIDN)** (AI-based lightmap denoising)

## 🚀 Quick Start

### Windows (Visual Studio) 🪟

```powershell
# Clone with submodules
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools

# Configure
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022" -A x64

# Build
cmake --build . --config Release
```

### Linux 🐧

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt install cmake build-essential libembree-dev libtbb-dev

# Clone with submodules
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools

# Build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --parallel
```

### macOS 🍎

```bash
# Install dependencies via Homebrew
brew install cmake embree tbb

# Clone and build
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --parallel
```

## 🧪 Compile Settings & Build Types

- Single-config generators (Ninja, Makefiles): set `-DCMAKE_BUILD_TYPE=Release|RelWithDebInfo|Debug`.
- Multi-config generators (Visual Studio, Xcode, Ninja Multi-Config): use `--config Release|RelWithDebInfo|Debug` and skip `CMAKE_BUILD_TYPE`.
- Release enables LTO/IPO by default; Debug and RelWithDebInfo disable IPO for faster iteration.
- `VIBEYMAPTOOLS_ASAN=YES` enables AddressSanitizer (Clang/GCC; MSVC where supported).
- `VIBEYMAPTOOLS_TIMETRACE=YES` emits Clang `-ftime-trace` JSON per translation unit.
- `NO_ITERATOR_DEBUG=ON` disables MSVC iterator debugging for speed.

## 🔧 Dependency Hints

### Embree + TBB (required)

If CMake cannot find them, pass the package config paths:

```bash
cmake .. -Dembree_DIR=/path/to/embree/lib/cmake/embree-4.x -DTBB_DIR=/path/to/tbb/lib/cmake/tbb
```

### NVIDIA OptiX (GPU Raytracing) ⚡

1. Install CUDA Toolkit from https://developer.nvidia.com/cuda-toolkit
2. Download OptiX SDK from https://developer.nvidia.com/designworks/optix/download
3. Set environment variable:
   ```powershell
   $env:OPTIX_ROOT_DIR = "C:\ProgramData\NVIDIA Corporation\OptiX SDK 7.7.0"
   ```

CMake will detect OptiX and enable GPU support.

### Intel OIDN (AI Denoising) 🤖

Download from https://www.openimagedenoise.org/downloads.html

```bash
cmake .. -DOpenImageDenoise_DIR=/path/to/oidn/lib/cmake/OpenImageDenoise
```

## 🧰 CMake Options

| Option | Default | Description |
|--------|---------|-------------|
| `ENABLE_LIGHTPREVIEW` | ON | Enable Qt-based `vmt-lightpreview` |
| `DISABLE_TESTS` | OFF | Skip building tests |
| `DISABLE_DOCS` | OFF | Skip docs build |
| `VIBEYMAPTOOLS_ASAN` | OFF | Enable AddressSanitizer for all targets |
| `VIBEYMAPTOOLS_TIMETRACE` | OFF | Enable Clang `-ftime-trace` output |
| `CMAKE_BUILD_TYPE` | Release | Build type (Debug/Release/RelWithDebInfo) |

## 🧪 Build Outputs

After a successful build, you'll find in `build/`:

| Binary | Description |
|--------|-------------|
| `vmt-bsp` | BSP compiler - converts .map to .bsp |
| `vmt-vis` | Visibility compiler - calculates PVS |
| `vmt-light` | Light compiler - calculates lightmaps |
| `vmt-bspinfo` | BSP information utility |
| `vmt-bsputil` | BSP manipulation utility |
| `vmt-maputil` | Lua scripting for .map workflows |
| `vmt-lightpreview` | Realtime lighting preview (experimental) |

## ✅ Running Tests

```bash
cd build
ctest --output-on-failure
```

## 🧪 Regression Testing

```bash
python tests/regression.py
```

To update golden hashes after intentional changes:
```bash
python tests/regression.py --update
```

## 🧯 Troubleshooting

### "Embree/TBB not found" 🔧
- Ensure Embree 4.x and oneTBB are installed
- Pass `embree_DIR` and `TBB_DIR` to CMake if needed

### "OptiX headers not found" ⚡
- Set `OPTIX_ROOT_DIR` to the OptiX SDK path
- Install CUDA Toolkit first

### "OIDN not found" 🤖
- Set `OpenImageDenoise_DIR` to the OIDN CMake config directory
- OIDN is optional; the bilateral filter will be used as fallback

### Lint/clangd errors in IDE 🧠
- IDEs sometimes miss the full CMake configuration
- The project should still compile correctly via CMake

## 🧑‍💻 Development

### Code Style
- 4-space indentation
- Allman brace style
- snake_case for functions, PascalCase for classes

### Adding New Features
1. Create feature branch
2. Implement changes
3. Update tests in `tests/`
4. Update documentation (CHANGELOG.md, WIKI.md)
5. Submit pull request

## 🧬 Versioning

VibeyMapTools uses [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 2.1.0)
- `VERSION` stores the base (next) version
- Git tags `vMAJOR.MINOR.PATCH[-prerelease]` are the source of truth for releases
- Non-tag builds append `-dev.<commits>+g<sha>` or `+dirty` metadata
- CMake generates `version.hh` with compile-time constants in `build/include`

### Version Header Usage

```cpp
#include <version.hh>

// Access version info
printf("VibeyMapTools %s\n", vibey::version::full());
printf("Built on %s\n", vibey::version::build_date());

// Feature detection
if (vibey::version::has_optix()) {
    // GPU raytracing available
}
```

### Creating a Release ✨
1. Update `VERSION` and `CHANGELOG.md`
2. Create an annotated tag: `git tag -a v2.1.0 -m "Release 2.1.0"`
3. Push the tag: `git push origin v2.1.0`
4. The Release GitHub Action builds and drafts the release with packages

## 🤖 CI/CD

GitHub Actions provides:
- Multi-platform builds (Windows, Linux, macOS)
- Automated testing on pushes and pull requests
- Draft releases with packaged artifacts on version tags
