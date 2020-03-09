from module import Module
from pathlib import Path
import os
from .leaf_finder.leaf_finder import LeafFinder
from .leaf_aimer.leaf_aimer import LeafAimer


class RuneAimer(Module):
    def __init__(self, parent, **config):
        self.wd = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(self.wd, parent, config)

        self.leaf_finder = LeafFinder(self)
        self.leaf_aimer = LeafAimer(self)

    def process(self, frame):
        # todo: return gimbal angles to aim at rune
        pass