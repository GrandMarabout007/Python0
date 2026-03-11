import importlib
import importlib.metadata


def analyze_matrix_data():
    import numpy as np
    import pandas
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    raw_data = np.random.rand(1000) * 100

    df = pandas.DataFrame(raw_data, columns=['Signal_Strength'])

    df['Moving_Average'] = df['Signal_Strength'].rolling(window=50).mean()
    print(f'\n{df}\n')
    return df


def print_mat(df):
    print("Generating visualization...")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['Signal_Strength'], label="Signal strengh",
            color="black", alpha=0.3)
    ax.plot(df.index, df['Moving_Average'], label="Moving_Average",
            color="blue", linewidth=2)
    ax.set(xlabel="data points", ylabel="Signal strengh",
           title="Data analysis")
    ax.legend()
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():

    packages = {
        "pandas": 'Data manipulation ready',
        "matplotlib": 'Visualization ready',
        "numpy": 'numerical computations ready'
        }
    print('\nLOADING STATUS: Loading programs...\n')
    print('Checking dependencies:')
    i = 0
    for pack in packages.keys():
        if importlib.util.find_spec(pack) is not None:
            print("[OK]", pack, f"({importlib.metadata.version(pack)}) -",
                  packages[pack])
            i += 1
        elif importlib.util.find_spec(pack) is None:
            print('[KO]', f'{pack}')

    if i == len(packages.items()):
        df = analyze_matrix_data()
        print_mat(df)
    else:
        print("\nDependency Error: You need to load the required programs.")
        print("Choose your package manager to enter the Matrix:\n")

        print("1. Using pip (Standard dependencies):")
        print("   $> pip install -r requirements.txt")
        print("   $> python3 loading.py\n")

        print("2. Using Poetry (Strict virtual environment):")
        print("   $> poetry install")
        print("   $> poetry run python loading.py")


if __name__ == "__main__":
    main()
