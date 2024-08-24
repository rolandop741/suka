import subprocess
import argparse

def run_script(script_name, argument=None):
    try:
        if argument:
            subprocess.run(['python', script_name, str(argument)], check=True)
        else:
            subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")
    except FileNotFoundError:
        print(f"File {script_name} not found.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run scripts with optional arguments")
    parser.add_argument("argument", type=int, help="Value to pass as an argument")
    args = parser.parse_args()

    scripts = ['ummpyfinal2.py', 'mixlistsfinal.py', '3thingsfinal.py']
    arguments = [args.argument, None, None]  # Modify this list with the arguments you want to pass
    for script, argument in zip(scripts, arguments):
        run_script(script, argument)
