#!/usr/bin/env python3

import os
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

    output_path = os.path.dirname(output_filename)

    if os.path.exists(output_path) is False:
        print('Creating Output Path: {output_path}'.format(output_path=output_path))
        os.makedirs(output_path)

    file = open(output_filename, 'wt')
    file.write(template)
    file.close()

    print('CloudFormation Template Generated: {output_filename}'.format(output_filename=output_filename))
