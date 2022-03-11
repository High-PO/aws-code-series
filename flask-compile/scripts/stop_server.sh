#!/bin/bash
kill -9 $(ps -ef | grep app.cpython-38.pyc | awk '{print $2}')
echo 'Stop Server'