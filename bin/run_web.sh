#!/usr/bin/env bash

uvicorn --reload --log-level info --host 0.0.0.0 --workers=2  server_app.app:app