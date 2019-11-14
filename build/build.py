#!/usr/bin/env python3

import sys

from Actions.ActionsEngine import ActionsEngine

if __name__ == '__main__':
    environment_name = sys.argv[1]
    environment_path = sys.argv[2]
    template_path = sys.argv[3]
    output_filename = sys.argv[4]

    template = ActionsEngine.generate(
        environment_name=environment_name,
        environment_path=environment_path,
        template_path=template_path
    )

    file = open(output_filename, 'wt')
    file.write(template)
    file.close()

    print('CloudFormation Template Generated: {output_filename}'.format(output_filename=output_filename))
