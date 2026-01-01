# AGENTS.md

Instructions for AI coding agents working on VibeyMapTools.

## Project Overview

VibeyMapTools (VMT) is a BSP compilation toolset for Quake engine mapping. It is a fork of [ericw-tools](https://github.com/ericwa/ericw-tools) with rebranding and modernization.

### Tools

| Tool | Purpose | Source Directory |
|------|---------|------------------|
| `vmt-bsp` | BSP compiler (.map → .bsp) | `src/qbsp/` |
| `vmt-vis` | Visibility compiler (PVS) | `src/vis/` |
| `vmt-light` | Lighting compiler (lightmaps) | `src/light/` |
| `vmt-bspinfo` | BSP information utility | `src/bspinfo/` |
| `vmt-bsputil` | BSP manipulation utility | `src/bsputil/` |
| `maputil` | Map file Lua scripting | `src/maputil/` |
| `lightpreview` | Real-time preview GUI | `src/lightpreview/` |

## Repository Structure

```
VibeyMapTools/
├── .github/        # CI workflows, templates
├── extern/         # Third-party dependencies (submodules)
├── assets/         # Images, branding
├── cmake/          # CMake modules
├── docs/           # Sphinx documentation (.rst files)
├── scripts/        # Build and utility scripts
├── src/            # All source code
│   ├── common/     # Shared library code
│   ├── include/    # Public headers
│   ├── qbsp/       # vmt-bsp source
│   ├── vis/        # vmt-vis source
│   ├── light/      # vmt-light source
│   ├── bspinfo/    # vmt-bspinfo source
│   ├── bsputil/    # vmt-bsputil source
│   ├── maputil/    # maputil source
│   └── lightpreview/ # Qt-based preview tool
├── tests/          # Test suite (maps/ subdirectory contains test .map files)
├── CMakeLists.txt
├── README.md
└── ... (other root files)
```

## Build System

### CMake Configuration

The project uses CMake with the following key variables:

```cmake
# Build type
-DCMAKE_BUILD_TYPE=Release|Debug|RelWithDebInfo

# Optional features
-DENABLE_LIGHTPREVIEW=YES|NO    # Qt6 GUI tool
-DERICWTOOLS_ASAN=YES|NO        # Address sanitizer

# Dependencies (auto-detected if installed)
-Dembree_DIR=/path/to/embree
-DTBB_DIR=/path/to/tbb
```

### Building

```bash
# Standard build
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel

# Run tests
ctest --test-dir build

# Create package
cmake --build build --target package
```

### Dependencies

- **Required**: C++20 compiler, CMake 3.14+
- **Recommended**: Intel Embree 4.x, oneTBB
- **Optional**: Qt6 (for lightpreview), CUDA/OptiX (GPU lighting), Intel OIDN (denoising)

## Code Conventions

### Style

- **Formatter**: clang-format (see `.clang-format`)
- **Indentation**: 4 spaces
- **Brace style**: Allman
- **Naming**:
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
  - Member variables: `m_camelCase` or `camelCase_`

### Running Formatter

```bash
scripts/format-code.sh
```

### File Organization

- Headers in `src/include/common/` for shared code
- Tool-specific code in `src/` subdirectories
- New features should have corresponding tests in `tests/`

## Testing

### Test Framework

Uses Catch2 for unit testing. Test files are in `tests/`.

```bash
# Run all tests
ctest --test-dir build

# Run specific test
./build/tests/tests "[qbsp]"
```

### Test Maps

Sample .map files in `tests/maps/` are used for integration testing.

## Documentation

### Sphinx Docs

Documentation uses Sphinx with reStructuredText in `docs/`:

```bash
# Install dependencies
pip install -r docs/requirements.txt

# Build HTML docs
cd docs && make html
```

### Key Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `WIKI.md` | Documentation hub |
| `CHANGELOG.md` | Version history |
| `BUILDING.md` | Build instructions |
| `CONTRIBUTING.md` | Contribution guide |
| `docs/*.rst` | Tool reference docs |

## Making Changes

### Workflow

1. Create a feature branch
2. Make changes following code conventions
3. Run formatter: `scripts/format-code.sh`
4. Build and test: `cmake --build build && ctest --test-dir build`
5. Update documentation if needed
6. Update `CHANGELOG.md` for user-facing changes

### Common Tasks

#### Adding a Command-Line Option

1. Add option parsing in tool's `main.cpp`
2. Add to help text
3. Document in `docs/<tool>.rst`
4. Add test case if applicable

#### Modifying BSP Processing

1. Core logic is in `src/common/` (shared) or tool-specific directories in `src/`
2. BSP format definitions in `src/include/common/bspfile.hh`
3. Consider backwards compatibility with existing .bsp files

#### Adding a New Entity Key

1. Add parsing in relevant tool (qbsp/light/vis)
2. Document in `docs/<tool>.rst` under appropriate section
3. Use existing key/value parsing patterns

## CI/CD

### GitHub Actions

- `.github/workflows/ci.yml` - Main CI pipeline (build, test)
- `.github/workflows/release.yml` - Release build + packaging on version tags

### Triggering Releases

1. Update `VERSION` file
2. Update `CHANGELOG.md`
3. Tag: `git tag -a v<version> -m "Release v<version>"`
4. Push: `git push origin v<version>`

## Important Files

| File | Purpose | When to Update |
|------|---------|----------------|
| `VERSION` | Version number | Before releases |
| `CHANGELOG.md` | User-facing changes | Every PR with user-visible changes |
| `CMakeLists.txt` | Build configuration | Adding files, dependencies |
| `docs/conf.py` | Sphinx config | Rarely |

## Gotchas

- **Tool naming**: Executables use `vmt-` prefix, but source directories don't (e.g., `src/qbsp/` builds `vmt-bsp`)
- **Submodules**: Run `git submodule update --init --recursive` after cloning
- **Qt6**: Only needed for `lightpreview`, disabled by default
- **Embree/TBB**: Auto-downloaded on some platforms, may need manual install on others

## Contact

- Issues: https://github.com/themuffinator/VibeyMapTools/issues
- Original project: https://github.com/ericwa/ericw-tools
