import re

def get_ct_time(self, md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=region).isoformat()

def get_md_time(self, md_file):
    return arrow.get(md_file.stat().st_mtime, tzinfo=region).isoformat()
