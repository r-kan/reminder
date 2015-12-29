#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from base.setting.utility import Rank, RankArbitrator as Arbitrator
from util.json_load import JsonLoader

import sys
reload(sys)
sys.setdefaultencoding('UTF8')  # need this for str(pattern_of_type_unicode) can work


class Sentence(object):

    def __init__(self, rank, restrict, default_values):
        self.rank = rank
        self.__restrict = restrict
        self.__default_values = default_values

    def get_default_value(self, var_name):
        assert var_name in self.__default_values
        return self.__default_values[var_name]

    def satisfy(self, pattern_name, pattern_group_name):
        if not self.__restrict:
            return True
        return self.__restrict in [pattern_name, pattern_group_name]

    def print(self):
        self.rank.print('\t\t')
        if self.__restrict:
            print('\t\t', self.__restrict)

    @staticmethod
    def create(data):
        assert isinstance(data, dict)
        rank = Rank.create(
            data["rank"]) if "rank" in data else Rank.create_default()
        restrict = str(data["restrict"]) if "restrict" in data else None
        default_values = {}
        if "default_arg_value" in data:
            raw_data = data["default_arg_value"]
            assert isinstance(raw_data, dict)
            for var_name in raw_data:
                default_values[var_name] = raw_data[var_name]
        return Sentence(rank, restrict, default_values)


class PhraseGroup(object):

    def __init__(self, name, targets, sentences, rank):
        assert isinstance(targets, list)
        assert isinstance(sentences, dict)
        self.name = str(name)  # raw pattern is of type 'unicode'
        self.targets = targets
        self.sentences = sentences
        self.rank = rank

    def get_default_value(self, sentence, var_name):
        assert sentence in self.sentences
        return self.sentences[sentence].get_default_value(var_name)

    def select_sentence(self, pattern, group_name):
        assert group_name in self.targets
        satisfied_sentences = []
        sentence_arbitrator = Arbitrator()
        for sentence in self.sentences:
            if self.sentences[sentence].satisfy(pattern, group_name):
                satisfied_sentences.append(sentence)
                sentence_arbitrator.add_rank(sentence, self.sentences[sentence].rank)
        sentence_arbitrator.finalize_rank()
        return sentence_arbitrator.arbitrate()

    def print(self):
        print(self.name)
        for target in self.targets:
            print('\t', target)
        self.rank.print()
        for sentence in self.sentences:
            print('\t', sentence)
            self.sentences[sentence].print()

    @staticmethod
    def create(name, data, global_rank):
        assert isinstance(data, dict)
        targets = []
        sentences = {}
        rank = Rank.create(data["rank"]) if "rank" in data else None
        if not rank:
            rank = Rank.create(global_rank)
        if "target" in data:
            raw_data = data["target"]
            assert isinstance(raw_data, list)
            for target in raw_data:
                targets.append(target)
        if "sentence" in data:
            raw_data = data["sentence"]
            assert isinstance(raw_data, dict)
            for sentence in raw_data:
                sentences[sentence] = Sentence.create(raw_data[sentence])
        return PhraseGroup(name, targets, sentences, rank)


class SettingLoader(object):
    """load the phrase setting from json files"""

    def __init__(self, in_file):
        self.__json_loader = JsonLoader(in_file)
        self.__global_rank = None
        self.phrases = {}
        self.load_setting()

    def load_setting(self):
        self.__global_rank = self.__json_loader.get_root_obj("rank")
        root = self.__json_loader.get_root_obj("phrase")
        if not root:
            return
        assert isinstance(root, dict)
        for phrase_group_name in root:
            self.phrases[phrase_group_name] = PhraseGroup.create(phrase_group_name, root[phrase_group_name],
                                                                 self.__global_rank)

    def print(self):
        for phrase_group_name in self.phrases:
            self.phrases[phrase_group_name].print()

if __name__ == '__main__':
    OBJ = SettingLoader("test_phrase.json")
    OBJ.print()
