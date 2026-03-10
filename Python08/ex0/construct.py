import sys
import os
import site


def main():
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print('Current Python:', sys.executable)
        print('Virtual Environment: None detected')
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        if os.name == 'posix':
            print("source matrix_env/bin/activate")
        if os.name == "nt":
            print("matrix_env\nScripts\nactivate")

        print("\nThen run this program again.")
    else:
        print('\nMATRIX STATUS: Welcome to the construct\n')

        print('Current Python:', sys.executable)
        print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
        print('Environment Path:', sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
