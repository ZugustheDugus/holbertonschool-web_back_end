#!/usr/bin/env python3
"""Program to filter messages and encrypt certain data
"""


import re
from typing import List

def filter_datum(fields: List[str],
                redaction: str,
                message: str,
                separator: str) -> str:
    ''' Returns a message with sensitive data redacted '''
    for x in fields:
        message = re.sub(f'{x}=.+?{separator}',
                        f'{x}={redaction}{separator}', message)
    return message
