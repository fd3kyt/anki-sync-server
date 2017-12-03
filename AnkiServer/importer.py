
# AnkiServer - A personal Anki sync server
# Copyright (C) 2013 David Snopek
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from anki.importing.csvfile import TextImporter
from anki.importing.apkg import AnkiPackageImporter
from anki.importing.anki1 import Anki1Importer
from anki.importing.supermemo_xml import SupermemoXmlImporter
from anki.importing.mnemo import MnemosyneImporter
from anki.importing.pauker import PaukerImporter

from anki import version as anki_version
from distutils.version import StrictVersion

__all__ = ['get_importer_class', 'import_file']

importers = {
  'text': TextImporter,
  'apkg': AnkiPackageImporter,
  'anki1': Anki1Importer,
  'supermemo_xml': SupermemoXmlImporter,
  'mnemosyne': MnemosyneImporter,
  'pauker': PaukerImporter,
}

def get_importer_class(type):
    global importers
    return importers.get(type)

def import_file(importer_class, col, path, allow_update = True):
    importer = importer_class(col, path)
    importer.allowUpdate = allow_update

    if importer.needMapper:
        importer.open()

    importer.run()
