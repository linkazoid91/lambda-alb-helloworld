#!/usr/bin/env python
import os
import sys
import pytest
import lambda_handler

def test_index() -> None:
    assert lambda_handler.hello_world()['message'] == 'Hello World'
