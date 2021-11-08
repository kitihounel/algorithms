"""Aho-Corasick string matching algorithm.

Code from https://iq.opengenus.org/aho-corasick-algorithm/.
"""
from collections import deque, defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.output_link = None
        self.pattern_index = -1


def build_trie(root, words):
    for j, word in enumerate(words):
        current = root
        for c in word:
            child = current.children.get(c, None)
            if child is None:
                child = TrieNode()
                current.children[c] = child
            current = child
        current.pattern_index = j


def build_suffix_and_output_links(root):
    root.suffix_link = root

    q = deque()
    for node in root.children.values():
        node.suffix_link = root
        q.append(node)

    while len(q) != 0:
        current = q.popleft()
        for c, child in current.children.items():
            tmp = current.suffix_link
            while c not in tmp.children and tmp != root:
                tmp = tmp.suffix_link
            child.suffix_link = tmp.children[c] if c in tmp.children else root
            q.append(child)

        i = current.suffix_link.pattern_index
        current.output_link = current.suffix_link if i >= 0 else current.suffix_link.output_link


def aho_corasick(text, patterns):
    root = TrieNode()
    build_trie(root, patterns)
    build_suffix_and_output_links(root)

    match_indexes = defaultdict(list)
    parent = root
    j = 0
    while j < len(text):
        c = text[j]
        if c in parent.children:
            parent = parent.children[c]
            p = parent.pattern_index
            if p >= 0:
                match_indexes[patterns[p]].append(j - len(patterns[p]) + 1)
            tmp = parent.output_link
            while tmp is not None:
                p = tmp.pattern_index
                match_indexes[patterns[p]].append(j - len(patterns[p]) + 1)
                tmp = tmp.output_link
        else:
            while parent != root and c not in parent.children:
                parent = parent.suffix_link
            if c in parent.children:
                continue
        j += 1
    return match_indexes
