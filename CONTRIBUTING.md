# Contributing to VibeyMapTools

Thank you for your interest in contributing to VibeyMapTools! This document provides guidelines for contributing.

Coming from ericw-tools? The flow is the same, but release automation lives in GitHub Actions and binaries are prefixed with `vmt-`.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone --recursive https://github.com/YOUR_USERNAME/VibeyMapTools.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`

## Development Setup

See [BUILDING.md](BUILDING.md) for detailed build instructions.

### Quick Start

```bash
cmake -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build
```

## Code Style

This project uses `clang-format` for consistent code formatting.

- Run `scripts/format-code.sh` before committing
- Follow the style defined in `.clang-format`
- Use 4-space indentation
- Allman brace style
- `snake_case` for functions, `PascalCase` for classes

## Submitting Changes

### Pull Request Process

1. Ensure your code builds without errors
2. Run the test suite: `ctest --test-dir build`
3. Update documentation if adding new features
4. Update `CHANGELOG.md` with your changes
5. Submit a pull request with a clear description

### Commit Messages

Use clear, descriptive commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for test changes

Example: `feat: add support for PBR lightmaps`

## Reporting Issues

- Use the issue templates when available
- Include reproduction steps for bugs
- Provide system information (OS, compiler version)
- Attach sample .map files if relevant

## Questions?

- Open a Discussion on GitHub
- Check the [WIKI.md](WIKI.md) for documentation

## Release Process (Maintainers)

This is for contributors with release privileges.

1. Update `VERSION` with the next release number (e.g., `2.1.1`).
2. Update `CHANGELOG.md` and `docs/changelog.rst` with user-visible changes.
3. Build and test locally:
   - `cmake -B build -DCMAKE_BUILD_TYPE=Release`
   - `cmake --build build --config Release`
   - `ctest --test-dir build --output-on-failure --build-config Release`
4. Commit the changes:
   - `git add VERSION CHANGELOG.md docs/changelog.rst`
   - `git commit -m "chore: release vX.Y.Z"`
5. Tag the release and push:
   - `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
   - `git push origin main`
   - `git push origin vX.Y.Z`

GitHub Actions will build packages and attach them to the release. You can create a GitHub Release
manually (Publish Release) or rely on the workflow to draft it on tag push.

For more detailed steps and packaging notes, see the release section in [WIKI.md](WIKI.md).

## License

By contributing, you agree that your contributions will be licensed under the GPLv3 license.
