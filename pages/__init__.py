import arrow
from config import REGION, TIME_FORMAT

def get_ct_time(md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=REGION).format(TIME_FORMAT)

def get_md_time(md_file):
    return arrow.get(md_file.stat().st_mtime, tzinfo=REGION).format(TIME_FORMAT)
