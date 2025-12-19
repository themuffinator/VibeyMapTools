import os
import sys
import subprocess
import hashlib
import json
import argparse
from pathlib import Path

# Configuration
GOLDEN_FILE = Path("tests/golden_hashes.json")
MAPS_DIR = Path("tests/maps")
BIN_DIR = Path("bin/Release") # Default, can be overriden

def calculate_file_hash(filepath):
    """Calculates SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_tool(tool_name, args, cwd=None):
    """Runs a tool (qbsp/vis/light) and checks for errors."""
    # Find tool
    # Check current dir, then bin dir, then PATH
    tool_path = tool_name
    if (BIN_DIR / f"{tool_name}.exe").exists():
        tool_path = str(BIN_DIR / f"{tool_name}.exe")
    elif (BIN_DIR / tool_name).exists():
        tool_path = str(BIN_DIR / tool_name)
    
    cmd = [tool_path] + args
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {tool_name}:")
        print(result.stdout)
        print(result.stderr)
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="VibeyMapTools Regression Runner")
    parser.add_argument("--update", action="store_true", help="Update golden hashes")
    parser.add_argument("--bin-dir", type=str, help="Path to binaries")
    args = parser.parse_args()

    global BIN_DIR
    if args.bin_dir:
        BIN_DIR = Path(args.bin_dir)

    # Load golden hashes
    previous_hashes = {}
    if GOLDEN_FILE.exists():
        with open(GOLDEN_FILE, "r") as f:
            previous_hashes = json.load(f)
    
    current_hashes = {}
    failed = False

    # List test maps
    map_files = list(MAPS_DIR.glob("*.map"))
    if not map_files:
        print("No .map files found in tests/maps/")
        return

    for map_file in map_files:
        map_name = map_file.stem
        bsp_file = map_file.with_suffix(".bsp")
        
        print(f"--- Testing {map_name} ---")

        # 1. QBSP
        if not run_tool("qbsp", [str(map_file)]):
            failed = True
            continue

        # 2. Light
        # Using -extra for higher quality test, but maybe stick to fast for regression?
        # Use -extra4 to test supersampling
        if not run_tool("light", ["-extra4", str(bsp_file)]): 
            failed = True
            continue
        
        # 3. Hash
        if not bsp_file.exists():
            print(f"BSP file not generated for {map_name}")
            failed = True
            continue
            
        final_hash = calculate_file_hash(bsp_file)
        current_hashes[map_name] = final_hash
        
        print(f"Hash: {final_hash}")

        if args.update:
            previous_hashes[map_name] = final_hash
            print("Updated golden hash.")
        else:
            if map_name in previous_hashes:
                if previous_hashes[map_name] != final_hash:
                    print(f"FAIL: Hash mismatch! Expected {previous_hashes[map_name]}")
                    failed = True
                else:
                    print("PASS: Hash matches.")
            else:
                print("WARNING: No golden hash found. Use --update to set.")

    if args.update:
        with open(GOLDEN_FILE, "w") as f:
            json.dump(previous_hashes, f, indent=4)
        print(f"Saved golden hashes to {GOLDEN_FILE}")

    if failed:
        sys.exit(1)
    else:
        print("All tests passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
