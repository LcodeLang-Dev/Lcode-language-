# Lcode Language - Changelog

All notable changes to the Lcode Language project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.76] - 2026-06-05

### ✨ Added

#### Try/Catch Error Handling
- Graceful error management without program crashes
- Error messages stored in `#error` variable
- Catch blocks execute when errors occur

```lcode
try
    set result divide 10 by 0 into result
catch error
    say(Error: #error)
done
```

#### For Loop with Range
- Loop through numeric ranges efficiently
- Support for step values
- Backward iteration support

```lcode
for i from 1 to 10
    say(#i)
done

for i from 0 to 100 step 5
    say(#i)
done
```

#### Built-in Math Functions
- `sqrt(value) into result` - Square root
- `abs(value) into result` - Absolute value
- `max(val1, val2) into result` - Maximum
- `min(val1, val2) into result` - Minimum
- `power(base, exponent) into result` - Exponentiation
- `floor(value) into result` - Round down
- `ceil(value) into result` - Round up

#### String Escape Sequences
- `\n` - Newline
- `\t` - Tab character
- `\r` - Carriage return
- `\\` - Backslash

```lcode
set text Hello\nWorld\tTabbed
say(#text)
```

#### Debug Mode
- `debug on` - Enable debug output
- `debug off` - Disable debug output
- Shows detailed error messages
- Traces execution flow

```lcode
debug on
// Your code here
debug off
```

#### Enhanced Error Tracking
- Error messages logged instead of silent failures
- Descriptive error messages for all operations
- Better exception handling throughout

#### Function Parameters Framework
- Structure in place for future full implementation
- Tasks can be called with parameters
- Foundation for v0.77 enhancement

### 🔧 Changed

#### Error Handling
- All operations now log errors gracefully
- File operations report specific errors
- Math operations handle edge cases better
- String operations are more robust

#### Output
- Version banner displayed on startup
- Better error message formatting
- Improved debugging output

#### Code Structure
- Added error tracking system
- Added debug mode flag
- Improved code organization
- Better separation of concerns

### 🐛 Fixed

- Fixed variable resolution edge cases
- Improved condition evaluation accuracy
- Better handling of invalid input
- Fixed escape sequence processing

### 📚 Documentation

- Added comprehensive README.md
- Added FEATURE_ROADMAP.md
- Added VERSION.md
- Added CHANGELOG.md (this file)
- Added 10 test code files
- Added master test runner

### 🧪 Testing

- Added 65+ test cases
- 100% test pass rate
- Test coverage for all features
- Master test runner for automation

### 📦 Project Updates

- Version numbering system
- Release information
- Known limitations documented
- Future roadmap planned

---

## [0.75] - 2026-05-29

### ✨ Added

#### List Operations
- `check if <value> in <list> into <var>` - Check if item exists
- `mass replace <list> with <replacement> in <text> into <var>` - Replace multiple items

#### Cryptography Enhancements
- XOR encryption/decryption fixes
- Improved key handling
- Better error handling

### 🐛 Fixed

- XOR routing issues fixed
- List container validation improved
- String replacement edge cases

### 📈 Performance

- Optimized list operations
- Faster string processing

---

## [0.72] - 2026-05-22

### ✨ Added

#### System Information
- `say time` - Display current date and time
- `say os` - Display operating system info

#### File Operations
- `delete file <filename>` - Remove files
- Better error reporting for file operations

#### Memory Management
- `reset brain` - Clear all variables
- Better variable handling

#### Module System
- Improved import functionality
- Better library path resolution

### 🐛 Fixed

- Module loading improvements
- File path handling
- Better error messages

---

## [0.71] - 2026-05-15

### ✨ Added

#### String Operations
- Enhanced uppercase/lowercase
- Better string combining
- Improved replace functionality

#### Conditional Enhancements
- Better condition evaluation
- Support for more operators

#### Loop Improvements
- Loop optimization
- Better block handling

---

## [0.70] - 2026-05-08

### ✨ Added

#### Core Language Features
- Variables and assignment
- Data types (string, number, boolean, empty)
- Comments with //

#### Control Flow
- `when`/`else` conditionals
- `repeat` loops
- `during` conditional loops
- `loop` for array iteration
- `task` function definitions

#### Operations
- Basic arithmetic (add, subtract, multiply, divide)
- String manipulation (uppercase, lowercase, combine, replace)
- List operations (create, push, pop, show)
- Variable referencing with #

#### File I/O
- `read file` - Read file contents
- `write` - Write to file
- `append` - Append to file

#### Cryptography
- Caesar cipher (encrypt/decrypt)
- Base64 encoding/decoding
- SHA hashing (MD5, SHA1, SHA256, SHA512)
- XOR encryption
- String reversal (encrypt/decrypt reverse)

#### Utilities
- `say()` - Print output
- `ask()` - Get user input
- `input()` - Get input with prompt
- `sleep()` - Pause execution
- `clear()` - Clear screen
- `exit()` - Exit program
- `length()` - Get length
- `type()` - Get variable type
- `random()` - Generate random number
- Module import system

---

## Version Comparison Table

| Feature | v0.70 | v0.71 | v0.72 | v0.75 | v0.76 |
|---------|-------|-------|-------|-------|-------|
| Variables | ✅ | ✅ | ✅ | ✅ | ✅ |
| Conditionals | ✅ | ✅ | ✅ | ✅ | ✅ |
| Loops | ✅ | ✅ | ✅ | ✅ | ✅ ⭐ |
| Tasks | ✅ | ✅ | ✅ | ✅ | ✅ |
| Math | ✅ | ✅ | ✅ | ✅ | ✅ ⭐ |
| Strings | ✅ | ✅ ⭐ | ✅ | ✅ | ✅ ⭐ |
| Lists | ✅ | ✅ | ✅ | ✅ ⭐ | ✅ |
| Crypto | ✅ | ✅ | ✅ | ✅ ⭐ | ✅ |
| File I/O | ✅ | ✅ | ✅ ⭐ | ✅ | ✅ |
| Error Handling | ❌ | ❌ | ❌ | ❌ | ✅ ⭐ |
| Debug Mode | ❌ | ❌ | ❌ | ❌ | ✅ ⭐ |
| For Loops | ❌ | ❌ | ❌ | ❌ | ✅ ⭐ |

⭐ = New/Enhanced in this version

---

## Upgrade Instructions

### From v0.75 to v0.76

**No breaking changes** - All v0.75 code is compatible.

#### To use new features:

1. **Try/Catch:**
```lcode
try
    // your code
catch error
    say(Error: #error)
done
```

2. **For Loops:**
```lcode
for i from 1 to 10
    say(#i)
done
```

3. **Math Functions:**
```lcode
sqrt(25) into root
```

4. **Debug Mode:**
```lcode
debug on
// your code
debug off
```

---

## Future Releases

### v0.77 (July 2026)
- Dictionary/object support
- List methods (sort, reverse, join)
- String interpolation
- Global vs local scope

### v0.78 (August 2026)
- JSON support
- REPL mode
- Enhanced debugging
- Performance optimization

### v0.80 (October 2026)
- Feature complete for v0.x
- Standard library
- IDE plugins

### v1.0 (2027)
- Production ready
- Language stabilization
- Full documentation
- Community libraries

---

## Supported Platforms

### Operating Systems
- ✅ Windows (7+)
- ✅ macOS (10.12+)
- ✅ Linux (all distributions)

### Python Versions
- ✅ Python 3.6
- ✅ Python 3.7
- ✅ Python 3.8+
- ⚠️  Python 2.x (not supported)

---

## Community Feedback

We appreciate all feedback! Please report:
- 🐛 Bugs via GitHub Issues
- 💡 Feature requests via Discussions
- 📖 Documentation improvements via Pull Requests

---

## Credits

**Creator:** LcodeLang-Dev  
**Contributors:** Community members  
**Inspired by:** Readability and accessibility

---

## License

All releases are under the MIT License. See LICENSE file for details.

---

**Last Updated:** June 5, 2026  
**Next Release:** July 2026 (v0.77)  
**Documentation:** See README.md and FEATURE_ROADMAP.md
