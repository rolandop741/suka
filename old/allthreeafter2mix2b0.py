import subprocess
import argparse

def run_script(script_name, *arguments):
    try:
        command = ['python', script_name] + [str(arg) for arg in arguments if arg is not None]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")
    except FileNotFoundError:
        print(f"File {script_name} not found.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run scripts with optional arguments")
    parser.add_argument("argument1", type=int, help="First argument to pass")
    parser.add_argument("argument2", type=float, help="Second argument to pass")
    args = parser.parse_args()

    scripts = ['ummpyfinal22.py', 'mixlistsfinal.py', '3thingsfinal2.py']
    arguments_list = [
        (args.argument1, args.argument2),  # Pass two arguments to ummpyfinal2.py
        (None,),  # No arguments to mixlistsfinal.py
        (None,)   # No arguments to 3thingsfinal2.py
    ]

    for script, arguments in zip(scripts, arguments_list):
        run_script(script, *arguments)
