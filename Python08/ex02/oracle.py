import os
from dotenv import load_dotenv


def main():
    print()

    load_dotenv()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(script_dir, '.env')
    infos = {
            'mode': ['MATRIX_MODE', None],
            'db_url': ['DATABASE_URL', None],
            'api_key': ['API_KEY', None],
            'log_level': ['LOG_LEVEL', None],
            'zion_url': ['ZION_ENDPOINT', None]
        }
    for key in infos:
        env_var_name = infos[key][0]
        infos[key][1] = os.getenv(env_var_name)

    for info in infos.values():
        if info[1] is not None:
            print(f'{info[0]}: {info[1]}')
        else:
            print('[error]: [Missing] -', info[0])

    print()
    if os.path.exists(dotenv_path):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing, using system env only")


if __name__ == "__main__":
    main()
