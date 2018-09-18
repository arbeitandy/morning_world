#!/bin/bash
rm -rf morning_world_code
git clone git@github.com:arbeitandy/morning_world.git morning_world_code

rsync -avz morning_world_code ${WORKING_USER}@${REMOTE_IP}:~/
ssh ${WORKING_USER}@${REMOTE_IP} /home/interview/morning_world_code/run.sh
