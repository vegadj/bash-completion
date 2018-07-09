import fnmatch
import os

import pytest


class TestUpgradepkg(object):

    @pytest.mark.complete("upgradepkg -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("upgradepkg --")
    def test_2(self, completion):
        assert completion.list == "--dry-run --install-new --reinstall " \
            "--verbose".split()

    @pytest.mark.complete("upgradepkg ", cwd="slackware/home")
    def test_4(self, completion):
        expected = sorted([
            "%s/" % x for x in os.listdir("slackware/home")
            if os.path.isdir("./%s" % x)
        ] + [
            x for x in os.listdir("slackware/home")
            if os.path.isfile("./%s" % x) and fnmatch.fnmatch(x, "*.t[bglx]z")
        ])
        assert completion.list == expected
