from scrapper.main import main as scrapper_main
from scrapper.m_configs import MERCARI_IT_BOOK_URL, QUANTITY

def main():   
    print('''
 __  __                         _    ____                    _
|  \/  | ___ _ __ ___ __ _ _ __(_)  / ___|_ __ __ ___      _| | ___ _ __
| |\/| |/ _ \ '__/ __/ _` | '__| | | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
| |  | |  __/ | | (_| (_| | |  | | | |___| | | (_| |\ V  V /| |  __/ |
|_|  |_|\___|_|  \___\__,_|_|  |_|  \____|_|  \__,_| \_/\_/ |_|\___|_|

''')  
    scrapper_main(main_url=MERCARI_IT_BOOK_URL, quantity=QUANTITY)


if __name__ == '__main__':
    main()