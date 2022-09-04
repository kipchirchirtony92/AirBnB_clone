#!/usr/bin/python3
"""_init_ for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
