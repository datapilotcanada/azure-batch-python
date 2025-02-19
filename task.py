"""
This module contains the code for scraping products of the loblaw.ca website
"""
""" Standard Library Imports """
import re
import sys
import time
import random
import logging
import json

logger = logging.getLogger(__name__)

""" Helper Functions """
def __get_storage_account_values_from_url(url:str) -> dict:
        """
        Extracts the storage account values from the URL of the blob storage path.

        Returns:
            dict: The extracted storage account values.
        """
        _url = url
        try:
            is_local = False
            pattern = r"https://(.*?)/"
            match = re.search(pattern, _url)
            if match:
                account_url = f"https://{match.group(1)}"
                logger.debug(f"Result: {account_url}")
            else:
                pattern = r"http://(.*?)/"
                match = re.search(pattern, _url)
                if match:
                    account_url = f"http://{match.group(1)}"
                    logger.debug(f"Result: {account_url}")
                    is_local = True
                else:
                    raise ValueError("No match found")

            if is_local:
                storage_account_pattern = r"http://(.*).blob.core.windows.net"
            else:
                storage_account_pattern = r"https://(.*).blob.core.windows.net"

            """ Get the storage account name from the URL """
            storage_account = re.search(storage_account_pattern, _url).group(1)

            if is_local:
                container_name_pattern = r"http://.*?\.blob\.core\.windows\.net/([^/]+)/"
            else:
                container_name_pattern = r"https://.*?\.blob\.core\.windows\.net/([^/]+)/"

            match = re.search(container_name_pattern, _url)
            if match:
                container = match.group(1)
            else:
                raise ValueError("No container found")

            """ Get the blob name from the URL """
            pattern = r'/([^/]+?\.[a-zA-Z0-9]+)$'
            match = re.search(pattern, _url)
            if match:
                blob_name = match.group(1)                
                file_type = re.search(r'\.([a-zA-Z0-9]+)$', blob_name).group(1).replace(".", "")
                blob_name = blob_name.replace(f".{file_type}", "")
            else:
                blob_name = None
                file_type = None

            """ Get the folder path from the URL """
            str1 = f"{account_url}/{container}/"
            str2 = f"{blob_name}.{file_type}"
            folder_path = url.replace(str1, "").replace(str2, "")
            if blob_name is None or blob_name.lower() in ["none", ""]:
                blob_path = f"{folder_path}"
                blob_name = ""
            else:
                blob_path = f"{folder_path}{blob_name}.{file_type}"

            return {
                "_url": url,
                "account_url": account_url,
                "storage_account": storage_account,
                "container": container,
                "blob_name": blob_name,
                "folder_path": folder_path,
                "blob_path": blob_path
            }
        except Exception as e:
            message = f"[[storage_account line 274 ==> Error: {e}"
            logger.error(message)
            raise ValueError(message)

def __get_user_agents(n: int) -> list:
    """
    Generate a list of user agents.

    Args:
        n (int): The number of user agents to generate.

    Returns:
        list: A list of user agents.
    """
    user_agents = []
    for _ in range(n):
        chrome_version = f"{random.randint(60, 90)}.0.0.{random.randint(3000, 4000)}"
        windows_version = f"{random.randint(6, 10)}.0"
        user_agent = f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
        user_agents.append(user_agent)
    return user_agents
user_agents = __get_user_agents(100)

""" Main Function """
def task_function() -> dict:
    """
    Scrape product details from the loblaw.ca website.

    Args:
        driver (webdriver): The Selenium webdriver instance.
        article_number (str): The article number of the product.
        timeout (int, optional): The timeout value in seconds. Defaults to 30.

    Returns:
        dict: A dictionary containing the scraped product details.
    """        
    return { "result" = "success" }

if __name__ == '__main__':
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    param3 = sys.argv[3]    
    batch_run = {}
    batch_run['params'] = {}
    batch_run['storage_account'] = {}
    batch_run['product_information'] = {}
    batch_run['params']['url'] = product_url
    batch_run['params']['article_number'] = product_number
    batch_run['storage_account'] = __get_storage_account_values_from_url(target_path)    
    result = task_function()
    batch_run['product_information'] = result
    # TODO: Upload to storage account
    
