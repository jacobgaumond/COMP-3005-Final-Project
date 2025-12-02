#!/bin/bash
if [ ! -d "container-volume" ]; then
    mkdir container-volume/
else
	rm container-volume/*
fi

cat sql/DDL.sql sql/DML.sql > container-volume/setup.sql

podman compose up -d
