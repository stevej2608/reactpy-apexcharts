# Contributor Guide

Thank you for your interest in contributing to ReactPy Apexcharts!

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/reactpy-apexcharts.git
   cd reactpy-apexcharts

   ```
## Executing test environment commands

By utilizing `hatch`, the following commands are available to manage the development environment.

### Tests

| Command | Description |
| --- | --- |
| `hatch test` | Run Python tests using the current environment's Python version |
| `hatch test --all` | Run tests using all compatible Python versions |
| `hatch test --python 3.9` | Run tests using a specific Python version |
| `hatch test -k test_navigate_with_link` | Run only a specific test |


### Type Checking

```bash
pyright
```

### Documentation

| Command | Description |
| --- | --- |
| `hatch run docs:serve` | Start the [`mkdocs`](https://www.mkdocs.org/) server to view documentation locally |
| `hatch run docs:build` | Build the documentation |



### Code Style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check .
ruff format .
```

## Submitting Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b my-feature-branch
   ```
2. Make your changes and commit them with a clear commit message
3. Push to your fork:
   ```bash
   git push origin my-feature-branch
   ```
4. Open a Pull Request on GitHub

## Questions?

If you have questions, please open an issue on GitHub or reach out to the maintainers.

Thank you for contributing!
