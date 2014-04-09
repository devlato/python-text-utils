#!/usr/bin/env python


import sys
import re


def render_left_aligned_line(line, viewport_width):
    lines = []
    width = 0
    current_line = []
    for word in line: 
        word_length = len(word)
        if word_length > viewport_width:
            # TODO split word
            pass
        elif (width + word_length + 1) < viewport_width:
            current_line.append(word)
            width += word_length + 1
        else: 
            lines.append(current_line)
            width = word_length
            current_line = [word]
    if current_line: 
        lines.append(current_line)
    return lines


def render_right_aligned_line(line, viewport_width):
    lines = []
    width = 0
    max_length = 0
    current_line = []
    for word in line: 
        word_length = len(word)
        if word_length > viewport_width:
            # TODO split word
            pass
        elif (width + word_length + 1) < viewport_width:
            current_line.append(word)
            width += word_length + 1
        else: 
            lines.append(current_line)
            if max_length < width:
                max_length = width
            width = word_length
            current_line = [word]
    if current_line: 
        lines.append(current_line)
    return [(([' '] * (max_length - __len(' '.join(line)))) + line) for line in lines]
            

def render_left_aligned_lines(lines, terminal_size, margins):
    viewport_width = get_viewport_width(terminal_size, margins) 
    prepared_lines = []
    for line in lines:
        prepared_lines += render_left_aligned_line(line, viewport_width)
    for line in prepared_lines: 
        print ' '.join(line)


def split_to_lines_by_newline(args):
    lines = []
    for arg in args:
        lines += map(lambda x: x.strip(), arg.split('\n'))
    return [re.split(r'\s+', line) for line in lines]

