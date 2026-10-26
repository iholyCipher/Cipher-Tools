# Changelog

All notable changes to the **Cipher Tools** project will be documented in this file.

## [3.5.0] - 2026-10-26 (Titan Suite Expansion & World-Class Architecture)
### Added
- **Complete 150-Tool Suite**: Expanded to 11 comprehensive disciplines and 150 precision power tools.
- **Modern CLI Engine**: Full support for headless CLI flags (`--tool`, `--category`, `--search`, `--list`, `--json`, `--test`, `--info`, `--version`).
- **Comprehensive Automated Test Runner (`test_suite.py`)**: 100% test coverage validating all 150 tools with mocked I/O.
- **GitHub Actions CI Pipeline**: Continuous multi-version Python testing (`.github/workflows/ci.yml`).
- **Standards & Packaging**: Added `pyproject.toml`, `setup.py`, `requirements.txt`, `LICENSE` (MIT), and `CONTRIBUTING.md`.
- **JSON Export (`--json`)**: Machine-readable full catalog export for third-party scripts and front-ends.

### Changed
- **Privacy & Sanitization**: Removed all local personal directory paths and username hardcodings.
- **REPL Interface**: Added dynamic prompt `operator@cipher-titan:~$`, graceful `Ctrl+C` interrupt handling, and search commands (`s <query>`).
- **Python 3.12+ / 3.14+ Compatibility**: Updated UTC datetime handling to `datetime.now(timezone.utc)`.

## [3.0.0] - 2026-10-23
- Initial Centurion architecture with 100 tools across 10 categories.
