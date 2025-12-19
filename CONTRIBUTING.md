# Contributing to VibeyMapTools

Thank you for your interest in contributing to VibeyMapTools! This document provides guidelines for contributing.

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

## License

By contributing, you agree that your contributions will be licensed under the GPLv3 license.
