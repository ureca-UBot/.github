#!/usr/bin/env python3
"""Scaffolding-only deterministic example; NOT a product API example."""
import json
import sys


def main():
    request = json.loads(sys.argv[1])
    items = request["items"]
    if not isinstance(items, list) or not all(isinstance(x, int) and not isinstance(x, bool) for x in items):
        raise ValueError("items must be an array of integers")
    print(json.dumps({"count": len(items), "sum": sum(items)}, separators=(",", ":"), sort_keys=True))


if __name__ == "__main__":
    main()
