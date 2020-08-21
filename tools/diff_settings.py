#!/usr/bin/env python3

def apply(config, args):
    config['arch'] = 'aarch64'
    config['baseimg'] = 'data/main.elf'
    config['myimg'] = 'build/uking'
    config['source_directories'] = ['src']
    config['objdump_executable'] = 'aarch64-linux-gnu-objdump'
