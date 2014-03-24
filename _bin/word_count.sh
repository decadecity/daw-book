#!/bin/bash
find . -name '*.md' -not -path "./.SyncArchive/*" -not -path "./_lib/*" | xargs wc -w
