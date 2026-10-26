# Contributing to Cipher Tools

Thank you for your interest in contributing to **Cipher Tools**! 🚀

## Core Principles

1. **Zero External Dependencies**: All tools must use only Python's standard library. External packages are strictly optional enhancements.
2. **Resilience & Graceful Degradation**: Handle missing OS privileges, network timeouts, and platform differences gracefully — never crash.
3. **Structured Modularity**: Place tools into their respective category modules under `modules/` and register them in `modules/registry.py`.
4. **Cross-Platform**: Prefer platform-agnostic logic. Use `os.name` / `platform.system()` guards for platform-specific code paths.

## Development Setup

```bash
git clone https://github.com/ithecipher/Cipher-Tools.git
cd Cipher-Tools
python cipher_tools.py --test
```

No virtual environment or dependency installation is needed — the project has zero pip dependencies.

## Running Tests

Before submitting a PR, ensure all 1,250 tools pass the automated test suite:

```bash
# Quick registry integrity check
python cipher_tools.py --test

# Full exhaustive test suite (runs every tool with mocked I/O)
python test_suite.py

# Test a specific range
python test_suite.py --start 626 --end 1250
```

## Code Style

- Use clear, descriptive function names: `tool_NNN_descriptive_name()`.
- Include a print header with the tool number and name at the start of each tool function.
- Wrap all user inputs with `input().strip()` and provide sensible defaults.
- Wrap risky operations in `try/except` blocks with informative error messages.

## Submitting Pull Requests

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/awesome-tool`).
3. Add your tool function to the appropriate category module.
4. Register the tool in `modules/registry.py`.
5. Run `python test_suite.py` and confirm 100% pass rate.
6. Commit your changes (`git commit -m 'feat: add awesome tool'`).
7. Push to the branch (`git push origin feature/awesome-tool`).
8. Open a Pull Request with a clear description of what your tool does.

## Reporting Issues

- Use the [GitHub Issues](https://github.com/ithecipher/Cipher-Tools/issues) tracker.
- Include your Python version, OS, and the exact error output.
- If a specific tool fails, include the tool ID number.
