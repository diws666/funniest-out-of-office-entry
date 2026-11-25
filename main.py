#!/usr/bin/env python3
"""Writes the Funniest Out-of-Office entry to /output/entry.txt."""

import os

REPLY = "Currently out of office. If this is urgent, please define urgent, then wait until Monday anyway."  # 96 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(REPLY)
