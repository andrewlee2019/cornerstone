#!/usr/bin/python
# -*- coding: utf-8 -*-

# 通过此脚本实现各种 project 的构建
import os
import sys
import argparse
import json
import subprocess

_SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
_ROOT_PATH = os.path.abspath(os.path.join(_SCRIPT_PATH, '..'))

def parse_args():
  parser = argparse.ArgumentParser()

  parser.add_argument('-p', '--project', type=str, required=True)
  return parser.parse_args()

def run_cmake(option):
  cmake_args = '-DPROJECT=' + option.project
  cmake_args += ' -B{}/build/{}'.format(_ROOT_PATH, option.project)
  cmd = 'cmake {} {}'.format(_ROOT_PATH, cmake_args)
  subprocess.call(cmd, shell=True)

def main():
  # 先进行参数解析
  option = parse_args()

  run_cmake(option)

if __name__ == '__main__':
  main()
