#!/bin/bash
find . -name '*.md' -not -path "./.SyncArchive/*" -not -path "./_lib/*" -not -path "./_homework/*" | xargs wc -w
