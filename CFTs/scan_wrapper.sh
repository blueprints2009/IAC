#!/bin/sh
image=$1
curl -d @${image} -X POST https://scanapi.redlock.io/v1/iac | jsonpp
