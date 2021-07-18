# from pyspark.sql.functions import column
# import spark

# spark.conf.set("spark.sql.shuffle.partitions")#, sc.defaultParallelism)



# yr = 2012
# # if yr % 4 == 0:
# #     print("Hey")
# # else:
# #     print("Hmmm")
# if yr % 400 == 0 :
# C:\Users\Admin\DataEngineering
# import os
# path = 'C:/Users/Admin/DataEngineering/tables'
# os.chdir(path)

a = 10
x = lambda a,b : a + 10 +b 
print(x(5))


def get_dashboard(title: str) -> Optional[models.Dashboard]:
    """Get a dashboard by title."""
    title = title.lower()
    dashboard = next(iter(sdk.search_dashboards(title=title)), None)
    if not dashboard:
        raise sdk_exceptions.NotFoundError(f'dashboard "{title}" not found')
    assert isinstance(dashboard, models.Dashboard)
    return dashboard


def download_dashboard(
    dashboard: models.Dashboard,
    style: str = "tiled",
    width: int = 545,
    height: int = 842,
    filters: Optional[Dict[str, str]] = None,
):


result = sdk.render_task_results(task.id)
    filename = f"{dashboard.title}.pdf"
    with open(filename, "wb") as f:
        f.write(result)
    print(f'Dashboard pdf saved to "{filename}"')


assert dashboard.id
    id = int(dashboard.id)
    task = sdk.create_dashboard_render_task(
        id,
        "pdf",
        models.CreateDashboardRenderTask(
            dashboard_style=style,
            dashboard_filters=urllib.parse.urlencode(filters) if filters else None,
        ),
        width,
        height,
    )


import json
import urllib
import sys
import textwrap
import time
from typing import cast, Dict, Optional

import looker_sdk
from looker_sdk import models

import sdk_exceptions