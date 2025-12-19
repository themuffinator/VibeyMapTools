# Building VibeyMapTools

This document describes how to build VibeyMapTools from source.

## Prerequisites

### Required
- **CMake** 3.16 or later
- **C++17 compatible compiler**:
  - Visual Studio 2019+ (Windows)
  - GCC 9+ (Linux)
  - Clang 10+ (macOS/Linux)
- **Git** (for submodule dependencies)

### Optional (for enhanced features)
- **Intel Embree 3.x/4.x** - CPU raytracing acceleration (highly recommended)
- **Intel TBB** - Thread Building Blocks (usually bundled with Embree)
- **NVIDIA CUDA Toolkit** - For GPU raytracing
- **NVIDIA OptiX SDK 7.x** - GPU raytracing backend
- **Intel Open Image Denoise (OIDN)** - AI-based lightmap denoising

## Quick Start

### Windows (Visual Studio)

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

### Linux

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt install cmake build-essential libembree-dev libtbb-dev

# Clone with submodules
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools

# Build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

### macOS

```bash
# Install dependencies via Homebrew
brew install cmake embree tbb

# Clone and build
git clone --recursive https://github.com/themuffinator/VibeyMapTools.git
cd VibeyMapTools
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(sysctl -n hw.ncpu)
```

## Optional Dependencies Setup

### Intel Embree

Download from https://www.embree.org/ or install via package manager.

Set `EMBREE_ROOT_DIR` if not in standard location:
```bash
cmake .. -DEMBREE_ROOT_DIR=/path/to/embree
```

### NVIDIA OptiX (GPU Raytracing)

1. Install CUDA Toolkit from https://developer.nvidia.com/cuda-toolkit
2. Download OptiX SDK from https://developer.nvidia.com/designworks/optix/download
3. Set environment variable:
   ```powershell
   $env:OPTIX_ROOT_DIR = "C:\ProgramData\NVIDIA Corporation\OptiX SDK 7.7.0"
   ```

CMake will automatically detect OptiX and enable GPU support.

### Intel OIDN (AI Denoising)

Download from https://www.openimagedenoise.org/downloads.html

```bash
cmake .. -DOpenImageDenoise_DIR=/path/to/oidn/lib/cmake/OpenImageDenoise
```

## CMake Options

| Option | Default | Description |
|--------|---------|-------------|
| `SKIP_TBB_INSTALL` | OFF | Skip TBB library installation |
| `SKIP_EMBREE_INSTALL` | OFF | Skip Embree library installation |
| `CMAKE_BUILD_TYPE` | Release | Build type (Debug/Release/RelWithDebInfo) |

## Build Outputs

After a successful build, you'll find in `build/`:

| Binary | Description |
|--------|-------------|
| `vmt-bsp` | BSP compiler - converts .map to .bsp |
| `vmt-vis` | Visibility compiler - calculates PVS |
| `vmt-light` | Light compiler - calculates lightmaps |
| `vmt-bspinfo` | BSP information utility |
| `vmt-bsputil` | BSP manipulation utility |
| `lightpreview` | Real-time lighting preview (experimental) |

## Running Tests

```bash
cd build
ctest --output-on-failure
```

## Regression Testing

```bash
python tests/regression.py
```

To update golden hashes after intentional changes:
```bash
python tests/regression.py --update
```

## Troubleshooting

### "Embree not found"
- Ensure Embree is installed and `EMBREE_ROOT_DIR` is set correctly
- Check that the Embree version matches (3.x or 4.x)

### "OptiX headers not found"
- Set `OPTIX_ROOT_DIR` environment variable to the OptiX SDK path
- Ensure CUDA Toolkit is installed first

### "OIDN not found"
- Set `OpenImageDenoise_DIR` to the OIDN CMake config directory
- OIDN is optional - bilateral filter will be used as fallback

### Lint/clangd errors in IDE
- These are often due to IDE not understanding the CMake configuration
- The project should still compile correctly via CMake

## Development

### Code Style
- 4-space indentation
- Allman brace style
- Snake_case for functions, PascalCase for classes

### Adding New Features
1. Create feature branch
2. Implement changes
3. Update tests in `tests/`
4. Update documentation (CHANGELOG.md, WIKI.md)
5. Submit pull request

## Versioning

VibeyMapTools uses [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 2.1.0)
- Version stored in `VERSION` file
- CMake generates `version.hh` with compile-time constants

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

### Creating a Release

**Manual:**
1. Update VERSION file with new version
2. Update CHANGELOG.md
3. Create tag: `git tag -a v2.1.0 -m "Release 2.1.0"`
4. Push tag: `git push origin v2.1.0`

**Automated (via GitHub Actions):**
1. Go to Actions → "Release Automation"
2. Click "Run workflow"
3. Select bump type (patch/minor/major)
4. Optionally add pre-release tag (alpha/beta/rc)

## CI/CD

GitHub Actions provides:
- Multi-platform builds (Windows, Linux, macOS)
- Automated testing on every push
- Draft releases on version tags
- Nightly builds from main branch

