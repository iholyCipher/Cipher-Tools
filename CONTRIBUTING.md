# Contributing to Cipher Tools

Thank you for your interest in contributing to **Cipher Tools - Titan Suite**! 🚀

## Core Principles
1. **Zero External Dependencies**: All tools should utilize Python's standard library whenever possible. External dependencies should only be optional enhancements.
2. **Resilience & Graceful Degradation**: Always handle missing OS privileges (non-admin), timeouts on network calls, and platform differences gracefully.
3. **Structured Modularity**: Place tools into their respective categories under the `modules/` directory and register them in `cipher_tools.py`.

## Running Tests
Before submitting a PR, ensure all 150 tools pass the automated test suite:
```bash
python test_suite.py
```
Or via the CLI:
```bash
python cipher_tools.py --test
```

## Submitting Pull Requests
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/awesome-tool`).
3. Commit your changes (`git commit -m 'feat: add awesome tool'`).
4. Push to the branch (`git push origin feature/awesome-tool`).
5. Open a Pull Request.
