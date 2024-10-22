import logging

def main(default_config=True):
    if not default_config:
        logging.basicConfig(filename='my_logging_example.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    logging.debug(msg='Уровень debug для теста логгирования в logging')
    logging.info(msg='Уровень info для теста логгирования в logging')
    logging.warning(msg='Уровень warning для теста логгирования в logging')
    logging.error(msg='Уровень error для теста логгирования в logging')
    logging.critical(msg='Уровень critical error для теста логгирования')

if __name__ == '__main__':
    # main()
    main(default_config=False)