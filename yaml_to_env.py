# s script converts an everyconfig YAML fileset into a list of
# environment variables.
# Inspired by https://gist.github.com/SteveBenner/588fff3e54636f3d8297 without the Ruby
# Depends on everyconfig and visitor packages
#

import argparse
from visitor import Visitor
import yaml
from pathlib import Path
import sys 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='YAML file which needs to be parsed and turned into environment vars', required=True)
parser.add_argument('-t', '--type', choices=['export', 'dockerenv'], default='export')
parser.add_argument('--cmd-prefix', type=str, default=None, help="Command prefix (e.g. export). It will override predefined types in --type option")
parser.add_argument('-e', '--env-var-prefix', default="", help='Prefix that is added to every env variable name (e.g. "DW_"')
arguments = parser.parse_args()
varsYaml = arguments.file
if not Path(varsYaml).exists():
    print("Provided YAML path does not exist!")
    sys.exit(8)

cp_dict = {'export' : 'export ', 'dockerenv' : ''}
cmd_prefix = cp_dict[arguments.type]
if arguments.cmd_prefix is not None:
    cmd_prefix = arguments.cmd_prefix

var_prefix = arguments.env_var_prefix

class EnvEncoder(Visitor):
    def __init__(self):
        self.parentKey = ""
    
    def visit_str(self, node):
        print(f"{cmd_prefix}{var_prefix}{self.parentKey}='{node}'")

    def visit_int(self, node):
        # no quotes on integers
        print(f"{cmd_prefix}{var_prefix}{self.parentKey}={node}")
    
    def visit_bool(self, node):
        # not sure if there will be problem with true, True, TRUE
        return self.visit(str(node))

    def visit_list(self, node):
        if len(node) > 0:
            baseParentKey = self.parentKey+("" if self.parentKey =="" else "_")
            print(f'{cmd_prefix}{var_prefix}{baseParentKey}COUNT={len(node)}')
            for index, item in enumerate(node):
                self.parentKey = baseParentKey+str(index)
                self.visit(item)

    def visit_dict(self, node):
        prevParent = self.parentKey
        for key, value in sorted(node.items()):
            self.parentKey = prevParent+("" if prevParent =="" else "_")+key.upper()
            if type(value) == str:
                print(f"{cmd_prefix}{var_prefix}{self.parentKey}='{value}'")
            else:
                self.visit(value)
        # Pop the last known key
        self.parentKey = prevParent

encoder = EnvEncoder() 

with open(varsYaml, 'r') as stream:
    try:
        yaml_file = yaml.safe_load(stream)
        encoder.visit(yaml_file)
    except yaml.YAMLError as exc:
        print(exc)


