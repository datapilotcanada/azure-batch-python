from azure.batch.models import BatchErrorException, TaskAddParameter, ApplicationPackageReference, PoolInformation
from azure.batch import BatchServiceClient as BatchClient
from azure.identity import DefaultAzureCredential
import logging

_BATCH_ACCOUNT_NAME = ''
_BATCH_ACCOUNT_KEY = ''
_BATCH_ACCOUNT_URL = ''
_STORAGE_ACCOUNT_NAME = ''
_STORAGE_ACCOUNT_KEY = ''
_POOL_ID = 'LinuxFfmpegPool'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 5
_POOL_VM_SIZE = 'STANDARD_A1_v2'
_JOB_ID = 'LinuxFfmpegJob'
_APP_PACKAGE_ID = 'skuscraper'
_APP_PACKAGE_VERSION = '1.0'
DEBUG = True

""" Set up logging """
formatter           = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger              = logging.getLogger(__name__)
console_handler     = logging.StreamHandler()
if DEBUG:
    console_handler.setLevel(logging.DEBUG)
else:
    console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class Batch():
    def submit_task(self, client: BatchClient, job_id: str):
        try:
            param1 = ""
            param2 = ""
            param3 = ""          
            task_id = f"task_01"
            cmd = f"python task.py {param1} {param1} {param1}"
            # set up parameters for a batch task
            task_content = TaskAddParameter(
                id=task_id,
                command_line=cmd,
                application_package_references=[
                    ApplicationPackageReference(
                        application_id=_APP_PACKAGE_ID,
                        version=_APP_PACKAGE_VERSION
                    )
                ]
            )
            client.task.add(job_id=job_id, task=task_content)
        except Exception as e:
            print(e)
    
        
if __name__ =='__main__':
    pool_id = "poolbatchtaxskuce001"
    job_id = "testaxsku001"
    batchAccountEndpoint = _BATCH_ACCOUNT_URL
    target_path = sys.argv[1]
    product_url = sys.argv[2]
    product_number = sys.argv[3]
    credentials = DefaultAzureCredential()
    client = BatchClient(batchAccountEndpoint, credentials)
    batch = SKUBatch()    
    batch.submit_task(client=client, job_id=job_id)



