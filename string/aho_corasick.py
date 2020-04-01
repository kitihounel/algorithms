"""Aho-Corasick string matching algorithm.

Code from https://iq.opengenus.org/aho-corasick-algorithm/.
"""

from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suffixLink = None
        self.outputLink = None
        self.patternIndex = -1

def build_trie(root, words):
    for j, word in enumerate(words):
        current = root
        for c in word:
            child = current.children.get(c, None)
            if child is None:
                child = TrieNode()
                current.children[c] = child
            current = child
        current.patternIndex = j

def build_suffix_and_output_links(root):
    root.suffixLink = root

    q = deque()
    for node in root.children.values():
        node.suffixLink = root
        q.append(node)

    while len(q) != 0:
        current = q.popleft()
        for c, child in current.children.items():
            tmp = current.suffixLink
            while c not in tmp.children and tmp != root:
                tmp = tmp.suffixLink
            child.suffixLink = tmp.children[c] if c in tmp.children else root
            q.append(child)

        i = current.suffixLink.patternIndex
        current.outputLink = current.suffixLink if i >= 0 else current.suffixLink.outputLink

def aho_corasick(text, patterns):
    root = TrieNode()
    build_trie(root, patterns)
    build_suffix_and_output_links(root)

    matchIndexes = defaultdict(list)
    parent = root
    j = 0
    while j < len(text):
        c = text[j]
        if c in parent.children:
            parent = parent.children[c]
            p = parent.patternIndex
            if p >= 0:
                matchIndexes[patterns[p]].append(j - len(patterns[p]) + 1)
            tmp = parent.outputLink
            while tmp is not None:
                p = tmp.patternIndex
                matchIndexes[patterns[p]].append(j - len(patterns[p]) + 1)
                tmp = tmp.outputLink
        else:
            while parent != root and c not in parent.children:
                parent = parent.suffixLink
            if c in parent.children:
                continue
        j += 1
    return matchIndexes
