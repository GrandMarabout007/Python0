# import requests
# import matplotlib
# import numpy
import sys
import importlib
import importlib.metadata

# def check_pandas() -> bool:
#     try:
#         import pandas
#         return True
#     except ModuleNotFoundError:
#         print('pandas not install: pip install pandas')
#         return False

# def check_matplotlib() -> bool:
#     try:
#         import matplotlib
#         return True
#     except ModuleNotFoundError:
#         print('matplotlib not install: pip install pandas')
#         return False

def main():
    # print('Checking dependencies:')
    # panda_access = check_pandas()
    # matplotlib_access = check_matplotlib()

    # if panda_access is True:
    #     print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    # if matplotlib_access is True:
    #     print(f"[OK] matplotlib {matplotlib.__version__} - Visualization ready")

    # print(pandas.__version__)
    # # print(matplotlib._version__)

    packages = {
        "pandas": 'Data manipulation ready',
        "matplotlib": 'Visualization ready',
        "numpy": 'numerical computations ready'
        }
    for pack in packages.keys():
        if importlib.util.find_spec(pack) is not None:
            print("[OK]", pack, f"({importlib.metadata.version(pack)}) -", packages[pack])
        elif importlib.util.find_spec(pack) is None:
            print('[KO]', pack)








if __name__ == "__main__":
    main()
