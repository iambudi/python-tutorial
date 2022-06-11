"""
=========================================================================================
Implement asynchronous http GET request using aiohttp
1. Create asyncio tasks
2. Create aiohttp client session ctx manager
3. Pass the tasks to gather() method inside session ctx manager
4. Async io will proceed all the tasks until all done before 
5. Enumarete the http response to parse the result
=========================================================================================
"""

import asyncio
from asyncio.tasks import Task
import time
from typing import Any, Dict, List
import aiohttp
import json


from aiohttp.client_reqrep import ClientResponse

start: float = time.time()
names: List[str] = ["dian", "saitama", "john", "peter", "laura", "crystal", "asep", "wati", "python", "naruto"]


def get_tasks(session: aiohttp.client.ClientSession) -> List[Task[Any]]:
    url = "https://api.genderize.io?name={}"
    # tuple comprehension: use keyword tuple(), otherwise it becomes generator ()
    # which will be slower since it's lazy iterable
    # here just use list
    return [asyncio.create_task(session.get(url.format(id), ssl=False)) for id in names]


async def exec_request() -> None:
    # async func dan body nya
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # gather() means results aggregated from single event loop
        print("Please wait while processing requests...")
        responses = await asyncio.gather(*tasks)
        for idx, response in enumerate(responses):
            # print(isinstance(response, ClientResponse))
            r: ClientResponse = response  # trick to get the type recognized by vscode intelisense
            body: Dict[Any, Any] = await r.json()  # json is async, must use await
            # prettify the result with indentataion
            print(json.dumps(body, indent=4, sort_keys=False) if r.status == 200 else f"🔴 Error: Req {idx+1} {r.status} {body}")


# run coroutine event loop
asyncio.run(exec_request())

end = time.time()
total_time = end - start
print("It took %.2f secs for %d API calls" % (total_time, len(names)))
