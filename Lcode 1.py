import time
import random
import os
import base64
import hashlib
import platform
import json
import math
import re
from datetime import datetime

# Central runtime memory containers
variables = {}
tasks = {}
imported_modules = set()
error_messages = []
debug_mode = False

# Version info
VERSION = "0.76"
RELEASE_DATE = "June 5, 2026"

def log_error(error_msg):
    """Track errors for error handling"""
    global error_messages
    error_messages.append(error_msg)
    if debug_mode:
        print(f"[DEBUG] Error: {error_msg}")

def resolve_value(text):
    """Normalizes language primitives and resolves variable notation references."""
    text = str(text)
    text = text.replace("yes", "True")
    text = text.replace("no", "False")
    text = text.replace("empty", "None")

    result = ""
    i = 0

    while i < len(text):
        if text[i] == "#":
            i += 1
            var_name = ""
            while i < len(text) and (text[i].isalnum() or text[i] == "_"):
                var_name += text[i]
                i += 1
            result += str(variables.get(var_name, "undefined"))
        else:
            result += text[i]
            i += 1

    return result.strip()

def process_escape_sequences(text):
    """Process escape sequences like \\n, \\t, \\r"""
    text = text.replace("\\n", "\n")
    text = text.replace("\\t", "\t")
    text = text.replace("\\r", "\r")
    text = text.replace("\\\\", "\\")
    return text

def eval_condition(condition):
    """
    Evaluates human English conversational conditions natively,
    with a fallback for legacy symbolic operators.
    """
    condition = resolve_value(condition)
    condition_lower = condition.lower()
    
    # Text-to-logic structural operator mappings
    translations = [
        ("is not equal to", "!="),
        ("is equal to", "=="),
        ("is greater than or equal to", ">="),
        ("is less than or equal to", "<="),
        ("is greater than", ">"),
        ("is less than", "<"),
        ("is more than", ">")
    ]
    
    has_custom_op = False
    for word_op, sym_op in translations:
        if word_op in condition_lower:
            idx = condition_lower.find(word_op)
            left = condition[:idx].strip()
            right = condition[idx + len(word_op):].strip()
            op = sym_op
            has_custom_op = True
            break
            
    if not has_custom_op:
        operators = ["==", "!=", ">=", "<=", ">", "<"]
        op = None
        for sym in operators:
            if sym in condition:
                left, right = condition.split(sym, 1)
                op = sym
                break
        if not op:
            if condition == "True": return True
            if condition == "False": return False
            return False
    else:
        left = left.strip()
        right = right.strip()
        
    def clean_val(v):
        if v == "True": return True
        if v == "False": return False
        if v == "None": return None
        try:
            if "." in v: return float(v)
            return int(v)
        except ValueError:
            return v.strip('"').strip("'")
    
    l_val = clean_val(left)
    r_val = clean_val(right)
    
    if op == "==": return l_val == r_val
    if op == "!=": return l_val != r_val
    if op == ">":  return l_val > r_val
    if op == "<":  return l_val < r_val
    if op == ">=": return l_val >= r_val
    if op == "<=": return l_val <= r_val

    return False


# --- Native Cryptography Implementations ---
def simple_encrypt(text, key):
    result = ""
    key = int(key) % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def simple_decrypt(text, key):
    result = ""
    key = int(key) % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result


def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()


def base64_decrypt(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except:
        return "Invalid base64"


def hash_encrypt(text, hash_type="sha256"):
    h_type = hash_type.lower()
    if h_type == "md5": return hashlib.md5(text.encode()).hexdigest()
    elif h_type == "sha1": return hashlib.sha1(text.encode()).hexdigest()
    elif h_type == "sha256": return hashlib.sha256(text.encode()).hexdigest()
    elif h_type == "sha512": return hashlib.sha512(text.encode()).hexdigest()
    return hashlib.sha256(text.encode()).hexdigest()


def xor_encrypt(text, key):
    result = ""
    key_str = str(key)
    for i, char in enumerate(text):
        xor_val = ord(char) ^ ord(key_str[i % len(key_str)])
        result += chr(xor_val)
    return result.encode('latin1').hex()


def xor_decrypt(text, key):
    try:
        data = bytes.fromhex(text)
        result = ""
        key_str = str(key)
        for i, byte in enumerate(data):
            xor_val = byte ^ ord(key_str[i % len(key_str)])
            result += chr(xor_val)
        return result
    except:
        return "Invalid XOR data"


# --- Built-in Math Functions (v0.76) ---
def builtin_sqrt(value):
    try:
        return math.sqrt(float(value))
    except:
        return "Error: Invalid sqrt input"

def builtin_abs(value):
    try:
        return abs(float(value))
    except:
        return "Error: Invalid abs input"

def builtin_max(val1, val2):
    try:
        return max(float(val1), float(val2))
    except:
        return "Error: Invalid max input"

def builtin_min(val1, val2):
    try:
        return min(float(val1), float(val2))
    except:
        return "Error: Invalid min input"

def builtin_power(base, exp):
    try:
        return math.pow(float(base), float(exp))
    except:
        return "Error: Invalid power input"

def builtin_round(value, decimals=0):
    try:
        return round(float(value), int(decimals))
    except:
        return "Error: Invalid round input"

def builtin_floor(value):
    try:
        return math.floor(float(value))
    except:
        return "Error: Invalid floor input"

def builtin_ceil(value):
    try:
        return math.ceil(float(value))
    except:
        return "Error: Invalid ceil input"


def execute_block(block, task_params=None):
    i = 0
    while i < len(block):
        line = block[i].strip()
        if line.lower() == "stop":
            break
        if line.lower() == "skip":
            i += 1
            continue
        execute_line(line)
        i += 1


def handle_input_flow(prompt_text):
    """Intercepts input tracking; easily swapped for JavaScript prompts over Web UIs."""
    return input(prompt_text)


def execute_line(line):
    global debug_mode
    
    line = line.strip()
    if not line or line.startswith("//"):
        return

    line_lower = line.lower()

    # DEBUG MODE (v0.76)
    if line_lower == "debug on":
        debug_mode = True
        print("[DEBUG MODE ENABLED]")
        return
    
    elif line_lower == "debug off":
        debug_mode = False
        print("[DEBUG MODE DISABLED]")
        return

    # IMPORT
    if line_lower.startswith("import "):
        module_name = line[7:].strip().strip('"')
        possible_paths = [module_name, f"lib/{module_name}", f"{module_name}.lc", f"lib/{module_name}.lc"]
        found_path = None
        for path in possible_paths:
            if os.path.exists(path):
                found_path = path
                break
        
        if found_path:
            if found_path not in imported_modules:
                imported_modules.add(found_path)
                with open(found_path, "r") as f:
                    mod_code = f.read()
                run(mod_code)
        else:
            log_error(f"Module '{module_name}' not found")
        return

    # SAY TIME
    if line_lower == "say time":
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return

    # SAY OS
    elif line_lower == "say os":
        print(f"Running on {platform.system()} version {platform.release()}")
        return

    # RESET BRAIN
    elif line_lower == "reset brain":
        variables.clear()
        return

    # DELETE FILE
    elif line_lower.startswith("delete file "):
        filename = resolve_value(line[12:].strip().strip('"'))
        try:
            if os.path.exists(filename):
                os.remove(filename)
            else:
                log_error(f"File does not exist: {filename}")
        except Exception as e:
            log_error(f"Error deleting file: {str(e)}")
        return

    # CHECK IF IN LIST
    elif line_lower.startswith("check if ") and " in " in line_lower and " into " in line_lower:
        idx_in = line_lower.find(" in ")
        idx_into = line_lower.rfind(" into ")
        
        search_val = resolve_value(line[9:idx_in].strip().strip('"').strip("'"))
        list_name = line[idx_in + 4:idx_into].strip()
        var_name = line[idx_into + 6:].strip()
        
        if list_name in variables and isinstance(variables[list_name], list):
            string_list = [str(element) for element in variables[list_name]]
            if str(search_val) in string_list:
                variables[var_name] = "yes"
            else:
                variables[var_name] = "no"
        else:
            log_error(f"List container not found: {list_name}")
        return

    # MASS REPLACE
    elif line_lower.startswith("mass replace ") and " with " in line_lower and " in " in line_lower and " into " in line_lower:
        idx_with = line_lower.find(" with ")
        idx_in = line_lower.find(" in ")
        idx_into = line_lower.rfind(" into ")
        
        list_name = line[13:idx_with].strip()
        replacer = resolve_value(line[idx_with + 6:idx_in].strip().strip('"').strip("'"))
        target_text = resolve_value(line[idx_in + 4:idx_into].strip())
        var_name = line[idx_into + 6:].strip()
        
        if list_name in variables and isinstance(variables[list_name], list):
            cleaned = target_text
            for bad_word in variables[list_name]:
                cleaned = cleaned.replace(str(bad_word), str(replacer))
            variables[var_name] = cleaned
        else:
            log_error(f"List container not found: {list_name}")
        return

    # SET
    elif line_lower.startswith("set "):
        parts = line.split(" ", 2)
        if len(parts) < 3:
            log_error("Invalid set command")
            return
        name = parts[1]
        value = parts[2]

        if value.lower().startswith("input(") and value.endswith(")"):
            prompt = value[6:-1]
            user_input = handle_input_flow(resolve_value(prompt) + ": ")
            variables[name] = user_input
        elif value.lower().startswith("random(") and value.endswith(")"):
            nums = value[7:-1].split(",")
            start = int(nums[0].strip())
            end = int(nums[1].strip())
            variables[name] = random.randint(start, end)
        else:
            variables[name] = resolve_value(value)

    # SAY
    elif line_lower.startswith("say(") and line.endswith(")"):
        text = process_escape_sequences(resolve_value(line[4:-1]))
        print(text)

    # ASK
    elif line_lower.startswith("ask(") and line.endswith(")"):
        handle_input_flow(resolve_value(line[4:-1]) + ": ")

    # SLEEP
    elif line_lower.startswith("sleep(") and line.endswith(")"):
        time.sleep(float(resolve_value(line[6:-1])))

    # CLEAR
    elif line_lower == "clear()":
        os.system("cls" if platform.system() == "Windows" else "clear")

    # EXIT
    elif line_lower == "exit()":
        print("Program ended.")
        exit()

    # LENGTH
    elif line_lower.startswith("length(") and line.endswith(")"):
        content = line[7:-1]
        if content.startswith("#"):
            print(len(str(variables.get(content[1:], ""))))

    # TYPE
    elif line_lower.startswith("type(") and line.endswith(")"):
        content = line[5:-1]
        if content.startswith("#"):
            print(type(variables.get(content[1:])).__name__)

    # SQRT (v0.76)
    elif line_lower.startswith("sqrt(") and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        value = resolve_value(line[5:idx_into].strip().rstrip(")"))
        var_name = line[idx_into + 6:].strip()
        variables[var_name] = builtin_sqrt(value)

    # ABS (v0.76)
    elif line_lower.startswith("abs(") and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        value = resolve_value(line[4:idx_into].strip().rstrip(")"))
        var_name = line[idx_into + 6:].strip()
        variables[var_name] = builtin_abs(value)

    # MAX (v0.76)
    elif line_lower.startswith("max(") and "," in line and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        params = line[4:idx_into].strip().rstrip(")").split(",")
        var_name = line[idx_into + 6:].strip()
        if len(params) == 2:
            variables[var_name] = builtin_max(resolve_value(params[0].strip()), resolve_value(params[1].strip()))

    # MIN (v0.76)
    elif line_lower.startswith("min(") and "," in line and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        params = line[4:idx_into].strip().rstrip(")").split(",")
        var_name = line[idx_into + 6:].strip()
        if len(params) == 2:
            variables[var_name] = builtin_min(resolve_value(params[0].strip()), resolve_value(params[1].strip()))

    # POWER (v0.76)
    elif line_lower.startswith("power(") and "," in line and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        params = line[6:idx_into].strip().rstrip(")").split(",")
        var_name = line[idx_into + 6:].strip()
        if len(params) == 2:
            variables[var_name] = builtin_power(resolve_value(params[0].strip()), resolve_value(params[1].strip()))

    # CALL TASK (with parameters - v0.76)
    elif line_lower.startswith("call "):
        call_part = line[5:].strip()
        
        # Check if has parameters
        if "(" in call_part and ")" in call_part:
            idx_paren = call_part.find("(")
            task_name = call_part[:idx_paren].strip()
            params_str = call_part[idx_paren+1:-1]
            params = [resolve_value(p.strip()) for p in params_str.split(",")]
            
            if task_name in tasks:
                execute_block(tasks[task_name])
            else:
                log_error(f"Task not found: {task_name}")
        else:
            task_name = call_part
            if task_name in tasks:
                execute_block(tasks[task_name])
            else:
                log_error(f"Task not found: {task_name}")

    # LIST CREATION
    elif line_lower.startswith("list "):
        list_name = line[5:].strip()
        variables[list_name] = []

    # PUSH
    elif " push " in line_lower and " to " in line_lower:
        idx_push = line_lower.find(" push ")
        idx_to = line_lower.rfind(" to ")
        
        val_part = line[:idx_push].strip()
        list_part = line[idx_to + 4:].strip()
        
        value = resolve_value(val_part)
        if list_part in variables and isinstance(variables[list_part], list):
            variables[list_part].append(value)
        else:
            log_error(f"List not found: {list_part}")

    # POP
    elif line_lower.startswith("pop ") and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        list_name = line[4:idx_into].strip()
        var_name = line[idx_into + 6:].strip()

        if list_name in variables and isinstance(variables[list_name], list):
            if len(variables[list_name]) > 0:
                variables[var_name] = variables[list_name].pop()
            else:
                log_error("List is empty")
        else:
            log_error(f"List not found: {list_name}")

    # SHOW LIST
    elif line_lower.startswith("show "):
        list_name = line[5:].strip()
        if list_name in variables:
            print(variables[list_name])
        else:
            log_error(f"Variable not found: {list_name}")

    # MATH: ADD
    elif " add " in line_lower and " to " in line_lower and " into " in line_lower:
        idx_add = line_lower.find(" add ")
        idx_to = line_lower.find(" to ")
        idx_into = line_lower.rfind(" into ")

        val1 = resolve_value(line[:idx_add].strip())
        val2 = resolve_value(line[idx_add + 5:idx_to].strip())
        var_name = line[idx_into + 6:].strip()

        try:
            variables[var_name] = float(val1) + float(val2)
        except:
            log_error("Cannot evaluate math addition parameters")

    # MATH: SUBTRACT
    elif " subtract " in line_lower and " from " in line_lower and " into " in line_lower:
        idx_sub = line_lower.find(" subtract ")
        idx_from = line_lower.find(" from ")
        idx_into = line_lower.rfind(" into ")

        val1 = resolve_value(line[:idx_sub].strip())
        val2 = resolve_value(line[idx_sub + 10:idx_from].strip())
        var_name = line[idx_into + 6:].strip()

        try:
            variables[var_name] = float(val2) - float(val1)
        except:
            log_error("Cannot evaluate math subtraction parameters")

    # MATH: MULTIPLY
    elif " multiply " in line_lower and " by " in line_lower and " into " in line_lower:
        idx_mul = line_lower.find(" multiply ")
        idx_by = line_lower.find(" by ")
        idx_into = line_lower.rfind(" into ")

        val1 = resolve_value(line[:idx_mul].strip())
        val2 = resolve_value(line[idx_mul + 10:idx_by].strip())
        var_name = line[idx_into + 6:].strip()

        try:
            variables[var_name] = float(val1) * float(val2)
        except:
            log_error("Cannot evaluate math multiplication parameters")

    # MATH: DIVIDE
    elif " divide " in line_lower and " by " in line_lower and " into " in line_lower:
        idx_div = line_lower.find(" divide ")
        idx_by = line_lower.find(" by ")
        idx_into = line_lower.rfind(" into ")

        val1 = resolve_value(line[:idx_div].strip())
        val2 = resolve_value(line[idx_div + 8:idx_by].strip())
        var_name = line[idx_into + 6:].strip()

        try:
            if float(val2) == 0: 
                log_error("Cannot divide by zero")
            else: 
                variables[var_name] = float(val1) / float(val2)
        except:
            log_error("Cannot evaluate math division parameters")

    # STRING: REPLACE
    elif " replace " in line_lower and " with " in line_lower and " into " in line_lower:
        idx_rep = line_lower.find(" replace ")
        idx_with = line_lower.find(" with ")
        idx_into = line_lower.rfind(" into ")
        
        original = resolve_value(line[:idx_rep].strip())
        old_sub = resolve_value(line[idx_rep + 9:idx_with].strip())
        new_sub = resolve_value(line[idx_with + 6:idx_into].strip())
        var_name = line[idx_into + 6:].strip()
        
        variables[var_name] = original.replace(old_sub, new_sub)

    # STRING MANIPULATIONS
    elif " uppercase " in line_lower and " into " in line_lower:
        idx_up = line_lower.find(" uppercase ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_up].strip())
        variables[line[idx_into + 6:].strip()] = text.upper()

    elif " lowercase " in line_lower and " into " in line_lower:
        idx_low = line_lower.find(" lowercase ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_low].strip())
        variables[line[idx_into + 6:].strip()] = text.lower()

    elif " combine " in line_lower and " and " in line_lower and " into " in line_lower:
        idx_comb = line_lower.find(" combine ")
        idx_and = line_lower.find(" and ")
        idx_into = line_lower.rfind(" into ")
        val1 = resolve_value(line[:idx_comb].strip())
        val2 = resolve_value(line[idx_comb + 9:idx_and].strip())
        variables[line[idx_into + 6:].strip()] = str(val1) + str(val2)

    # FILE HANDLERS
    elif line_lower.startswith("read file ") and " into " in line_lower:
        idx_into = line_lower.rfind(" into ")
        filename = resolve_value(line[10:idx_into].strip().strip('"'))
        var_name = line[idx_into + 6:].strip()
        try:
            with open(filename, "r") as f: 
                variables[var_name] = f.read()
        except Exception as e: 
            log_error(f"Error reading file: {str(e)}")

    elif line_lower.startswith("write ") and " to file " in line_lower:
        idx_to = line_lower.rfind(" to file ")
        text = resolve_value(line[6:idx_to].strip())
        filename = resolve_value(line[idx_to + 9:].strip().strip('"'))
        try:
            with open(filename, "w") as f: 
                f.write(text)
        except Exception as e: 
            log_error(f"Error writing file: {str(e)}")

    elif line_lower.startswith("append ") and " to file " in line_lower:
        idx_to = line_lower.rfind(" to file ")
        text = resolve_value(line[7:idx_to].strip())
        filename = resolve_value(line[idx_to + 9:].strip().strip('"'))
        try:
            with open(filename, "a") as f: 
                f.write(text + "\n")
        except Exception as e: 
            log_error(f"Error appending file: {str(e)}")

    # CRYPTOGRAPHY WRAPPERS
    elif " encrypt caesar " in line_lower and " with key " in line_lower and " into " in line_lower:
        idx_enc = line_lower.find(" encrypt caesar ")
        idx_key = line_lower.find(" with key ")
        idx_into = line_lower.rfind(" into ")
        
        text = resolve_value(line[:idx_enc].strip())
        key = resolve_value(line[idx_enc + 16:idx_key].strip())
        var_name = line[idx_into + 6:].strip()
        variables[var_name] = simple_encrypt(text, key)

    elif " decrypt caesar " in line_lower and " with key " in line_lower and " into " in line_lower:
        idx_dec = line_lower.find(" decrypt caesar ")
        idx_key = line_lower.find(" with key ")
        idx_into = line_lower.rfind(" into ")
        
        text = resolve_value(line[:idx_dec].strip())
        key = resolve_value(line[idx_dec + 16:idx_key].strip())
        var_name = line[idx_into + 6:].strip()
        variables[var_name] = simple_decrypt(text, key)

    elif " encrypt base64 " in line_lower and " into " in line_lower:
        idx_enc = line_lower.find(" encrypt base64 ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_enc].strip())
        variables[line[idx_into + 6:].strip()] = base64_encrypt(text)

    elif " decrypt base64 " in line_lower and " into " in line_lower:
        idx_dec = line_lower.find(" decrypt base64 ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_dec].strip())
        variables[line[idx_into + 6:].strip()] = base64_decrypt(text)

    elif " hash " in line_lower and " into " in line_lower:
        idx_hash = line_lower.find(" hash ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_hash].strip())
        hash_type = resolve_value(line[idx_hash + 6:idx_into].strip())
        variables[line[idx_into + 6:].strip()] = hash_encrypt(text, hash_type)

    elif " encrypt reverse " in line_lower and " into " in line_lower:
        idx_enc = line_lower.find(" encrypt reverse ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_enc].strip())
        variables[line[idx_into + 6:].strip()] = text[::-1]

    elif " decrypt reverse " in line_lower and " into " in line_lower:
        idx_dec = line_lower.find(" decrypt reverse ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_dec].strip())
        variables[line[idx_into + 6:].strip()] = text[::-1]

    elif " encrypt xor " in line_lower and " with key " in line_lower and " into " in line_lower:
        idx_enc = line_lower.find(" encrypt xor ")
        idx_key = line_lower.find(" with key ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_enc].strip())
        key = resolve_value(line[idx_enc + 13:idx_key].strip())
        variables[line[idx_into + 6:].strip()] = xor_encrypt(text, key)

    elif " decrypt xor " in line_lower and " with key " in line_lower and " into " in line_lower:
        idx_dec = line_lower.find(" decrypt xor ")
        idx_key = line_lower.find(" with key ")
        idx_into = line_lower.rfind(" into ")
        text = resolve_value(line[:idx_dec].strip())
        key = resolve_value(line[idx_dec + 13:idx_key].strip())
        variables[line[idx_into + 6:].strip()] = xor_decrypt(text, key)

    else:
        if debug_mode:
            log_error(f"Unknown command: {line}")


def run(code):
    lines = code.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        line_lower = line.lower()

        # TASK Creation BLOCK
        if line_lower.startswith("task "):
            task_name = line[5:].strip()
            i += 1
            block = []
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "done": break
                block.append(current)
                i += 1
            tasks[task_name] = block

        # FOR LOOP with RANGE (v0.76)
        elif line_lower.startswith("for ") and " from " in line_lower and " to " in line_lower:
            parts = line[4:].split(" from ")
            var_name = parts[0].strip()
            
            range_part = parts[1].split(" to ")
            start = int(resolve_value(range_part[0].strip()))
            
            # Check for step
            step_val = 1
            if " step " in range_part[1].lower():
                end_step = range_part[1].split(" step ")
                end = int(resolve_value(end_step[0].strip()))
                step_val = int(resolve_value(end_step[1].strip()))
            else:
                end = int(resolve_value(range_part[1].strip()))
            
            i += 1
            block = []
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "done": break
                block.append(current)
                i += 1
            
            current_val = start
            if step_val > 0:
                while current_val <= end:
                    variables[var_name] = current_val
                    execute_block(block)
                    current_val += step_val
            else:
                while current_val >= end:
                    variables[var_name] = current_val
                    execute_block(block)
                    current_val += step_val

        # FOR-EACH INTERATOR LOOP
        elif line_lower.startswith("loop ") and " into " in line_lower:
            idx_into = line_lower.rfind(" into ")
            list_name = line[5:idx_into].strip()
            item_name = line[idx_into + 6:].strip()

            i += 1
            block = []
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "done": break
                block.append(current)
                i += 1

            if list_name in variables and isinstance(variables[list_name], list):
                for item in variables[list_name]:
                    variables[item_name] = item
                    execute_block(block)

        # WHEN CONDITIONAL
        elif line_lower.startswith("when "):
            condition = line[5:].strip()
            result = eval_condition(condition)
            i += 1

            true_block = []
            false_block = []
            in_else = False

            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "else":
                    in_else = True
                    i += 1
                    continue
                if current.lower() == "done": break
                if not in_else: true_block.append(current)
                else: false_block.append(current)
                i += 1

            if result: execute_block(true_block)
            else: execute_block(false_block)

        # DURING LOOP
        elif line_lower.startswith("during "):
            condition = line[7:].strip()
            i += 1
            block = []
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "done": break
                block.append(current)
                i += 1
            while eval_condition(condition):
                execute_block(block)

        # REPEAT LOOP
        elif line_lower.startswith("repeat "):
            amount_str = line[7:].strip()
            try: amount = int(resolve_value(amount_str))
            except: amount = 0

            i += 1
            block = []
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "done": break
                block.append(current)
                i += 1

            for _ in range(amount):
                execute_block(block)

        # TRY/CATCH Error Handling (v0.76)
        elif line_lower.startswith("try"):
            i += 1
            try_block = []
            catch_block = []
            in_catch = False
            
            while i < len(lines):
                current = lines[i].strip()
                if current.lower() == "catch":
                    in_catch = True
                    i += 1
                    continue
                if current.lower() == "done": break
                if not in_catch: try_block.append(current)
                else: catch_block.append(current)
                i += 1
            
            try:
                error_messages.clear()
                execute_block(try_block)
                if error_messages and catch_block:
                    variables['error'] = error_messages[-1]
                    execute_block(catch_block)
                    error_messages.clear()
            except Exception as e:
                if catch_block:
                    variables['error'] = str(e)
                    execute_block(catch_block)

        else:
            execute_line(line)

        i += 1


if __name__ == "__main__":
    print(f"Lcode Language Interpreter v{VERSION} ({RELEASE_DATE})")
    print("=" * 50)
    try:
        with open("program.lc", "r") as f:
            source_file_content = f.read()
        run(source_file_content)
    except FileNotFoundError:
        print("Error: program.lc not found.")
        print("Usage: python 'Lcode 1.py' (requires program.lc in same directory)")
