# WafSFMLTest

## Synopsis

Simple test case to run Waf on a not that simple project, but simple enough to see what appends.

It uses Google Waf [a link](https://waf.io/).

And libSFML to test the link with a local thirdParty library [a link](http://www.sfml-dev.org/).

## Motivation

I was not familiar with Waf build system [a link](https://waf.io/). But it looks for me like a very simple and light build environment.

I was stuck trying to compile with a fresh compiled version of a library.

So I configured this micro test case to solve my problem first.

## Point of interest

All wscript files. At root and recursively in each path containing sources.

## Make it build

First, test if the compilation by command line works:

    ./build_test_ok.sh  (it runs g++)

If it works you can use Waf with success:

    ./waf configure  (once)
    ./waf  (each time you compile)
