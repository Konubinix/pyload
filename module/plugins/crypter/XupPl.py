# -*- coding: utf-8 -*-

from module.plugins.Crypter import Crypter


class XupPl(Crypter):
    __name__ = "XupPl"
    __type__ = "crypter"
    __pattern__ = r'https?://(?:[^/]*\.)?xup\.pl/.*'
    __version__ = "0.1"
    __description__ = """Xup.pl decrypter plugin"""
    __author_name__ = "z00nx"
    __author_mail__ = "z00nx0@gmail.com"

    def decrypt(self, pyfile):
        header = self.load(pyfile.url, just_header=True)
        if 'location' in header:
            self.core.files.addLinks([header['location']], pyfile.package().id)
        else:
            self.fail('Unable to find link')
