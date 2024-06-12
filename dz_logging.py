import requests as rq
import logging
import requests.exceptions

sayts = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://www.mignews.com',
     'https://amazon.com',
     'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com',
    'https://www.wildberries.ru/'
]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filemode='a',
    filename='website_checker.log',
    encoding='utf8'
)

success_log = open('success_responses.log', 'w')
bad_responses_log = open('bad_responses.log', 'w')
blocked_responses_log = open('blocked_responses.log', 'w')



for url in sayts:
    try:
        response = rq.get(url)
        if response.status_code == 200:
            logging.info(f'INFO: {url}.response - {response}')
            success_log.write(f'INFO: {url}.response - {response}\n')
        else:
            logging.info(f'WARNING: {url}.response - {response}')
            bad_responses_log.write(f'WARNING: {url}.response - {response}\n')
    except requests.exceptions.RequestException:
        logging.info(f'ERROR: {url}, NO CONNECTION')
        blocked_responses_log.write(f'ERROR: {url}, NO CONNECTION\n')

success_log.close()
bad_responses_log.close()
blocked_responses_log.close()