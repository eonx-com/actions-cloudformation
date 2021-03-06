from jinja2 import Template, Environment, FileSystemLoader

import base64


class ActionsTemplate:
    last_data = None
    template_path = None

    @staticmethod
    def template_render(template_path, content, data) -> str:
        """
        Render the supplied Jinja2 content with the supplied data

        :type template_path: str
        :param template_path: Template root path

        :type content: str
        :param content: Jinja2 content

        :type data: dict
        :param data: Data to provide to the template

        :return: Rendered template
        """
        ActionsTemplate.template_path = template_path

        environment = Environment(loader=FileSystemLoader('./'))
        template = environment.from_string(content)
        template.globals['to_camel'] = ActionsTemplate.to_camel
        template.globals['to_title'] = ActionsTemplate.to_title
        template.globals['to_upper'] = ActionsTemplate.to_upper
        template.globals['to_lower'] = ActionsTemplate.to_lower
        template.globals['to_csv'] = ActionsTemplate.to_csv
        template.globals['len'] = ActionsTemplate.len
        template.globals['coalesce'] = ActionsTemplate.coalesce
        template.globals['is_empty'] = ActionsTemplate.is_empty
        template.globals['is_list'] = ActionsTemplate.is_list
        template.globals['is_dict'] = ActionsTemplate.is_dict
        template.globals['read_file'] = ActionsTemplate.read_file
        template.globals['strip'] = ActionsTemplate.strip
        template.globals['base64_encode'] = ActionsTemplate.base64_encode
        template.globals['base64_decode'] = ActionsTemplate.base64_decode
        template.globals['load_template'] = ActionsTemplate.load_template

        ActionsTemplate.last_data = data
        return template.render(data)

    @staticmethod
    def load_template(filename, indent=0, indent_width=1, indent_first=False, indent_character=' '):
        filename = '{template_path}/{filename}'.format(
            template_path=ActionsTemplate.template_path,
            filename=filename
        )
        print('Loading Template: {filename}'.format(filename=filename))

        # Read the file and return its content
        file_object = open(filename, 'rt')
        template_content = file_object.read()
        file_object.close()

        rendered_content = ActionsTemplate.template_render(
            template_path=ActionsTemplate.template_path,
            content=template_content,
            data=ActionsTemplate.last_data
        )

        if indent > 0:
            lines = rendered_content.split('\n')
            rendered_content = ''
            first = True
            for line in lines:
                for i in range(0, indent * indent_width):
                    if indent_first is True or first is False:
                        line = indent_character + line
                    first = False
                rendered_content += line + '\n'

        return rendered_content

    @staticmethod
    def coalesce(value_a, value_b):
        """
        Return value A unless it is empty (from left to right)

        :param value_a:
        :param value_b:
        :return:
        """
        if ActionsTemplate.is_empty(value_a):
            return value_b

        return value_a

    @staticmethod
    def is_empty(value):
        """
        Check if value is empty

        :return:
        """
        if value is None:
            return True

        if isinstance(value, str):
            if len(value.strip()) == 0:
                return True

        if value:
            return False

        return True

    @staticmethod
    def to_csv(value):
        """
        Convert list to CSV string
        :param value:
        :return: CSV string
        """
        if isinstance(value, str) is True:
            return value

        result = ''
        for item in value:
            result += '"{item}",'.format(item=item.replace('"', '\\"'))

        return result[:-1]

    @staticmethod
    def len(value):
        """
        Return length of supplied value

        :param value: Value to test

        :return: Length
        """
        return len(value)

    @staticmethod
    def is_list(value):
        """
        Return boolean indicating whether the supplied value is a list

        :param value: Value to test

        :return: Boolean flag
        """
        return isinstance(value, list)

    @staticmethod
    def is_dict(value):
        """
        Return boolean indicating whether the supplied value is a dictionary

        :param value: Value to test

        :return: Boolean flag
        """
        return isinstance(value, dict)

    @staticmethod
    def strip(value):
        """
        Strip whitespace from value

        :type value: str
        :param value:

        :return: Stripped value
        """
        return value.strip()

    @staticmethod
    def read_file(filename):
        """
        :type filename: str
        :param filename:

        :return: The files contents
        """
        file = open(filename, 'rt')
        content = str(file.read())
        file.close()

        return content

    @staticmethod
    def to_title(value):
        """
        Convert value to title case

        :type value: str
        :param value:

        :return: The value in title case
        """
        return str(value).title()

    @staticmethod
    def to_camel(value, separator='-', include_first=True):
        """
        Convert 'dash-value' to 'CamelValue'

        :type value: str
        :param value:

        :type separator: str
        :param separator: The dashes used as separator

        :type include_first: bool
        :param include_first:

        :return: Camel case variant of string
        """
        components = value.split(separator)

        if include_first is True:
            return ''.join(x.title() for x in components)

        return components[0] + ''.join(x.title() for x in components[1:])

    @staticmethod
    def to_upper(value):
        """
        Convert value to upper case

        :type value: str
        :param value:

        :return: The value in upper case
        """
        return str(value).upper()

    @staticmethod
    def to_lower(value):
        """
        Convert value to lower case

        :type value: str
        :param value:

        :return: The value in lower case
        """
        return str(value).lower()

    @staticmethod
    def base64_encode(value):
        """
        Base 64 encode the specified value

        :type value: str
        :param value:

        :return: The Base 64 encoded value
        """
        return base64.encodebytes(bytes(value, 'utf-8')).decode('ascii').strip()

    @staticmethod
    def base64_decode(value):
        """
        Base 64 decode the specified value

        :type value: str
        :param value:

        :return: The Base 64 decoded value
        """
        return base64.decodebytes(value.encode('utf-8'))
