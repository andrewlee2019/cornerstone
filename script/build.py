#!/usr/bin/python
# -*- coding: utf-8 -*-

# 通过此脚本实现各种 project 的构建
import os
import sys
import argparse
import json
import subprocess
import shutil

_SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
_ROOT_PATH = os.path.abspath(os.path.join(_SCRIPT_PATH, '..'))

def parse_args():
  parser = argparse.ArgumentParser()

  parser.add_argument('-p', '--project', type=str, required=True)
  parser.add_argument('-r', '--rebuild', action="store_true")
  return parser.parse_args()

def run_cmake(option):
  build_out_path = '{}/build/{}'.format(_ROOT_PATH, option.project)
  if option.rebuild:
    shutil.rmtree(build_out_path)
  cmake_args = '-DPROJECT=' + option.project
  cmake_args += ' -B{}'.format(build_out_path)
  cmd = 'cmake {} {}'.format(_ROOT_PATH, cmake_args)
  subprocess.call(cmd, shell=True)

def run_make(option):
  os.chdir(os.path.join(_ROOT_PATH, 'build', option.project))
  cmd = 'make'
  subprocess.call(cmd, shell=True)

def main():
  # 先进行参数解析
  option = parse_args()

  run_cmake(option)

  run_make(option)

if __name__ == '__main__':
  main()
