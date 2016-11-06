#! /usr/bin/env python
# encoding: utf-8

import os

VERSION = "0.2"
APPNAME = "wafTest"

def options(opt):
	opt.load('compiler_cxx')

def configure(cfg):
	cfg.load('compiler_cxx')
	cfg.env.LIB_SFML = ['sfml-graphics', 'sfml-system', 'sfml-window']
	cfg.env.LIBPATH_SFML   = [os.path.join(os.getcwd(), 'thirdParty/SFML-2.2/lib')]
	cfg.env.INCLUDES_SFML  = [os.path.join(os.getcwd(), 'thirdParty/SFML-2.2/include')]
	cfg.check(
		features='cxx cxxprogram', 
		cxxflags=['-std=c++11', '-Wall']
	)

def build(bld):
	bld.recurse('src')

