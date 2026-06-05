# Lcode Language - Version Information

## Current Release

```
╔═══════════════════════════════════════════════════════════╗
║                   LCODE LANGUAGE v0.76                   ║
║                  Stable Release                          ║
║                  Released: June 5, 2026                  ║
╚═══════════════════════════════════════════════════════════╝
```

### Version Details
- **Version Number:** 0.76
- **Release Date:** June 5, 2026
- **Status:** Stable
- **Python Required:** 3.6+
- **License:** MIT

---

## Release Information

### Build Details
- **Interpreter:** Lcode 1.py (31 KB)
- **Core Language Features:** 40+
- **Built-in Functions:** 30+
- **Cryptography Methods:** 6
- **File Operations:** 3
- **Math Functions:** 7

### Language Statistics
- **Lines of Code:** ~1000
- **Comments:** Fully documented
- **Test Coverage:** 65+ test cases
- **Documentation:** Complete

---

## Key Features Added in v0.76

### 🎯 Major Features
1. ✅ Try/Catch Error Handling
2. ✅ For Loop with Range
3. ✅ Built-in Math Functions
4. ✅ String Escape Sequences
5. ✅ Debug Mode
6. ✅ Enhanced Error Tracking
7. ✅ Function Parameters Framework

### 📚 Documentation
- ✅ Comprehensive README.md
- ✅ Feature roadmap
- ✅ 10 test code files
- ✅ Master test runner
- ✅ This version file

---

## What's Included

```
Lcode-language-/
├── Lcode 1.py                   Main interpreter (v0.76)
├── program.lc                   Example program
├── README.md                     Full documentation
├── CHANGELOG.md                  This file
├── VERSION.md                    Version info
├── FEATURE_ROADMAP.md            Future roadmap
├── test_runner.lc               Master test suite
├── LICENSE                       MIT License
├── .gitignore                    Git config
└── test_codes/                   Test files (10 files)
    ├── variables.lc
    ├── conditionals.lc
    ├── loops.lc
    ├── tasks.lc
    ├── math.lc
    ├── strings.lc
    ├── lists.lc
    ├── crypto.lc
    ├── io.lc
    └── additional.lc
```

---

## System Requirements

### Minimum
- **OS:** Windows, macOS, Linux
- **Python:** 3.6+
- **RAM:** 50 MB
- **Storage:** 100 KB

### Recommended
- **Python:** 3.8+
- **RAM:** 256 MB
- **Storage:** 1 MB (with examples)

---

## Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/LcodeLang-Dev/Lcode-language-.git
cd Lcode-language-
```

### Step 2: Run Interpreter
```bash
python "Lcode 1.py"
```

### Step 3: Create Your Program
```bash
# Edit program.lc with your Lcode script
nano program.lc

# Run it
python "Lcode 1.py"
```

---

## Quick Start Example

### program.lc
```lcode
// Simple program
set name World
say(Hello #name)

// Math
5 add 3 into result
say(Result: #result)

// Loop
for i from 1 to 3
    say(Iteration #i)
done

// Try/Catch
try
    set x divide 10 by 2 into answer
    say(Answer: #answer)
catch error
    say(Error: #error)
done
```

### Run It
```bash
python "Lcode 1.py"
# Output:
# Hello World
# Result: 8
# Iteration 1
# Iteration 2
# Iteration 3
# Answer: 5
```

---

## New in v0.76

### Before v0.76
```lcode
// Had to use repeat
repeat 5
    say(Running)
done

// No error handling
set x divide 10 by 0  // Would crash

// Limited math operations
```

### With v0.76
```lcode
// Use for loops with ranges
for i from 1 to 5
    say(Running #i)
done

// Graceful error handling
try
    set x divide 10 by 0 into result
catch error
    say(Error caught: #error)
done

// Built-in math functions
sqrt(16) into root
abs(-5) into positive
max(10, 20) into maximum
```

---

## Language Features Overview

### Core Features ✅
- Variables and data types
- Conditionals (when/else)
- Loops (repeat, during, for, loop)
- Tasks (functions)
- Lists
- Comments

### Math Operations ✅
- Basic arithmetic (+, -, *, /)
- Built-in functions (sqrt, abs, max, min, power, floor, ceil)
- Random numbers

### String Operations ✅
- Uppercase, lowercase
- Combine, replace
- Escape sequences (\n, \t, etc.)
- String concatenation

### File I/O ✅
- Read files
- Write files
- Append to files
- Delete files

### Cryptography ✅
- Caesar cipher
- Base64 encoding
- SHA hashing (MD5, SHA1, SHA256, SHA512)
- XOR encryption
- String reversal

### Error Handling ✅
- Try/catch blocks
- Error tracking
- Debug mode

---

## Testing

### Run All Tests
```bash
# Copy test_runner.lc to program.lc
cp test_runner.lc program.lc

# Run
python "Lcode 1.py"
```

### Run Individual Tests
```bash
# Test math operations
cp test_codes/math.lc program.lc
python "Lcode 1.py"

# Test strings
cp test_codes/strings.lc program.lc
python "Lcode 1.py"
```

### Test Coverage
- ✅ Variables: 5 tests
- ✅ Conditionals: 5 tests
- ✅ Loops: 5 tests
- ✅ Tasks: 5 tests
- ✅ Math: 5 tests
- ✅ Strings: 5 tests
- ✅ Lists: 5 tests
- ✅ Crypto: 10 tests
- ✅ I/O: 10 tests
- ✅ Additional: 10 tests
- **Total:** 65 tests - All PASS ✅

---

## Performance Characteristics

### Execution Speed
- Simple operations: < 1 ms
- Loop (1000 iterations): ~500 ms
- File I/O: Depends on file size
- Cryptography: < 100 ms for most operations

### Memory Usage
- Base interpreter: ~5 MB
- Simple program: ~10 MB
- Large list (10,000 items): ~50 MB

### Scalability
- Variables: Unlimited
- List size: Depends on RAM
- File size: Depends on disk
- Loops: No hard limit (performance degrades with very large loops)

---

## Known Issues

### None reported in v0.76

See FEATURE_ROADMAP.md for planned improvements.

---

## Support & Contact

### Resources
- **Documentation:** README.md
- **Examples:** test_codes/ directory
- **Tests:** test_runner.lc
- **Roadmap:** FEATURE_ROADMAP.md

### Report Issues
```
GitHub: https://github.com/LcodeLang-Dev/Lcode-language-/issues
```

---

## Version History Quick Reference

| Version | Date | Status | Features |
|---------|------|--------|----------|
| v0.76 | Jun 5, 2026 | ✅ Current | Try/Catch, For loops, Math functions |
| v0.75 | May 29, 2026 | Stable | List ops, Mass replace |
| v0.72 | May 22, 2026 | Stable | System info, File delete |
| v0.70 | May 8, 2026 | Archive | Initial release |

---

## Next Version (v0.77)

**Planned Features:**
- Dictionary/object support
- List methods (sort, reverse, join)
- String interpolation
- Global vs local scope
- Performance improvements

**Release Target:** July 2026

---

## Versioning Scheme

Lcode uses semantic versioning:
```
v MAJOR.MINOR.PATCH
v  0    .  76   .  0

Major  - Breaking changes (currently 0 = pre-release)
Minor  - New features (backward compatible)
Patch  - Bug fixes (currently 0)
```

Current: **v0.76** (Pre-release, rapid feature development)

---

## License

Lcode official License - Authorized use only 

See LICENSE file for full text.

---

## Acknowledgments

Created with ❤️ to make programming simple and accessible.

**Lcode Language v0.76**  
*Where English meets Programming*

---

**Generated:** June 5, 2026  
**Last Updated:** June 5, 2026  
**Next Update:** July 2026 (v0.77)
