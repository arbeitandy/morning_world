#!/bin/bash
git clone git@github.com:arbeitandy/morning_world.git morning_world_code

rsync -avz morning_world_code ${WORKING_USER}@${REMOTE_IP}:~/

