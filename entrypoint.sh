#!/bin/sh -l

echo "Hello World!";
echo $1;
echo $2;

ls -l;
ls $1 -l;
ls $2 -l;
