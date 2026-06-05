# Lcode Language

A simple, readable scripting language with normal human words and less logic.

## Overview

Lcode is an English-based programming language designed to make coding accessible to everyone, even those with no programming experience. If you're tired of reading complex logic from traditional programming languages, Lcode is here to change that. Written in Python, it prioritizes readability and simplicity, making it easy for high school students and beginners to understand and write.

Currently at **v0.75** with extensive feature support and regular updates.

## Features

- **Human-Readable Syntax**: Write code using conversational English
- **Variable Management**: Set and manipulate variables with simple commands
- **Conditionals**: Use `when/else` statements for decision-making
- **Loops**: `repeat` for fixed iterations, `during` for conditional loops, `loop` for array iteration
- **Functions**: Create reusable `task` blocks
- **Math Operations**: `add`, `subtract`, `multiply`, `divide`
- **String Manipulation**: `uppercase`, `lowercase`, `combine`, `replace`
- **Cryptography**: Caesar cipher, Base64, SHA hashing, XOR encryption
- **File I/O**: `read file`, `write`, `append`
- **List Operations**: `push`, `pop`, `check if`, `mass replace`
- **Input/Output**: `say` for output, `input()` for user input
- **Random Numbers**: Generate random integers
- **System Information**: Check OS, time, and manage memory

## Installation

### Requirements
- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/LcodeLang-Dev/Lcode-language-.git
cd Lcode-language-
```

2. Run your Lcode programs:
```bash
python "Lcode 1.py"
```

Make sure your `.lc` files are in the same directory, or update the file path in the code.

## Quick Start

### Your First Program

Create a file named `program.lc`:

```lcode
set name Edikan
say(Welcome #name)
```

Run it:
```bash
python "Lcode 1.py"
```

Output:
```
Welcome Edikan
```

## Language Syntax

### Variables

Set and use variables with the `set` command:

```lcode
set username John
set age 25
say(Hello #username)
```

### Basic Values

- **Text**: `"hello"` or `hello` (strings)
- **Numbers**: `42`, `3.14`
- **Boolean**: `yes` (true), `no` (false)
- **Empty**: `empty` (None/null)

### Conditionals

```lcode
when #age is greater than 18
    say(You are an adult)
else
    say(You are a minor)
done
```

Supported comparisons:
- `is equal to` (==)
- `is not equal to` (!=)
- `is greater than` (>)
- `is less than` (<)
- `is greater than or equal to` (>=)
- `is less than or equal to` (<=)

### Loops

**Repeat Loop** - Run code a fixed number of times:
```lcode
repeat 5
    say(This runs 5 times)
done
```

**During Loop** - Run while a condition is true:
```lcode
set counter 0
during #counter is less than 5
    say(Count: #counter)
    set counter #counter add 1
done
```

**Loop Through List** - Iterate over array items:
```lcode
list fruits
apple push to fruits
banana push to fruits

loop fruits into fruit
    say(#fruit)
done
```

### Functions (Tasks)

Define and call reusable blocks:

```lcode
task greet
    say(Hello from a task)
done

call greet
```

### Input & Output

```lcode
set name input(What is your name)
say(Nice to meet you #name)

ask(Press enter to continue)
```

### Math Operations

```lcode
set a 10
set b 5

a add b into result1
a subtract b from result2
a multiply b by result3
a divide b by result4

say(Results: #result1 #result2 #result3 #result4)
```

### String Operations

```lcode
set text hello

text uppercase into upper
text lowercase into lower
text combine world into combined
text replace e with a into replaced
```

### List Operations

```lcode
list numbers

1 push to numbers
2 push to numbers
3 push to numbers

pop numbers into last_item
say(Last item: #last_item)

check if 2 in numbers into found
say(Found: #found)
```

### File Operations

```lcode
write Hello World to file data.txt

read file data.txt into content
say(#content)

append New line to file data.txt
```

### Cryptography

**Caesar Cipher:**
```lcode
set message hello
message encrypt caesar world with key 3 into encrypted
encrypted decrypt caesar world with key 3 into decrypted
```

**Base64:**
```lcode
set text secret
text encrypt base64 into encoded
encoded decrypt base64 into decoded
```

**Hashing:**
```lcode
set password mypass123
password hash sha256 into hashed
```

**XOR Encryption:**
```lcode
set data confidential
data encrypt xor with key secret into encrypted
encrypted decrypt xor with key secret into decrypted
```

**Reverse:**
```lcode
set original backwards
original encrypt reverse into reversed
```

### Special Commands

```lcode
// Check time
say time

// Check operating system
say os

// Get length of variable
length(#myvar)

// Get type of variable
type(#myvar)

// Clear screen
clear()

// Pause execution
sleep(2)

// Delete a file
delete file oldfile.txt

// Reset all variables
reset brain

// Exit program
exit()
```

### Comments

Use `//` to add comments:

```lcode
// This is a comment
set name John  // Variable assignment
```

## Full Example Program

```lcode
// Initialize
set name Edikan
set x 10

// Output with variable
say(Welcome #name)

// Conditional
when #x is greater than 5
    say(Big number)
else
    say(Small number)
done

// Repeat loop
repeat 3
    say(Loop running)
done

// Random number
set luck random(1,10)
say(Your lucky number is: #luck)

// Task definition
task greet
    say(Hello from function)
done

// Call task
call greet

// User input
set user input(Enter your name)
say(#user joined the program)

// String info
length(#user)
type(#luck)

// Timing
say(Waiting...)
sleep(2)
say(Done waiting)
```

## File Structure

```
Lcode-language-/
├── Lcode 1.py           # Main interpreter
├── program.lc           # Example program
├── README.md            # This file
├── LICENSE              # MIT License
└── .gitignore          # Git ignore file
```

## How It Works

1. The `.lc` file is read by `Lcode 1.py`
2. The interpreter parses and executes each line
3. Variables are stored in memory and can be referenced with `#variablename`
4. Blocks (tasks, loops, conditionals) are processed sequentially

## Version History

### v0.75
- Latest release with comprehensive feature support
- XOR encryption/decryption fixes
- Mass replace and list checking functionality
- Improved string operations

### v0.72
- System information commands
- File deletion support
- Memory reset functionality

## Testing Your Code

To test Lcode programs:

1. Create a `.lc` file with your code
2. Save it in the same directory as `Lcode 1.py`
3. Update the filename in `Lcode 1.py` if needed (default: `program.lc`)
4. Run: `python "Lcode 1.py"`

## Troubleshooting

**Module not found error**
- Ensure your `.lc` file is in the correct directory
- Check file permissions

**Unknown command error**
- Verify syntax matches the examples above
- Check for typos in command keywords

**Variable not found**
- Make sure you've set the variable with `set` before using it
- Variable names are case-sensitive

## Future Roadmap

Planned features for future versions:
- Dictionary/object support
- More cryptographic algorithms
- Standard library modules
- Improved error messages
- Web/browser support
- More built-in functions

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Improve documentation
- Submit pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by **LcodeLang-Dev**

---

**Made with ❤️ to make programming simple and accessible to everyone.**

Have questions? Found a bug? Let me know!
