
.. _pages/toolkit/txt2po#txt2po_and_po2txt:

txt2po and po2txt
*****************

txt2po allows you to use the same principles of PO files with normal text
files.  In PO only items that change are marked fuzzy and only new items need
to be translated, unchanged items remain unchanged for the translation.

.. _pages/toolkit/txt2po#usage:

Usage
=====

::

  txt2po [options] <foo.txt> <foo.po>
  po2txt [options] [-t <foo.txt>] <XX.po> <foo-XX.txt>

Where:

| foo.txt    | is the input plain text file   |
| foo.po     | is an empty PO file that may be translated   |
| XX.po      | is a PO file translated into the XX language   |
| foo-XX.txt  | is the foo.txt file translated into language XX   |

Options (txt2po):

| --version            | show program's version number and exit   |
| -h, --help           | show this help message and exit   |
| --manpage            | output a manpage based on the help   |
| :doc:`--progress=progress <option_progress>`  | show progress as: dots, none, bar, names, verbose   |
| :doc:`--errorlevel=errorlevel <option_errorlevel>`   | show errorlevel as: none, message, exception, traceback   |
| -iINPUT, --input=INPUT    | read from INPUT in \*, txt formats   |
| -xEXCLUDE, --exclude=EXCLUDE   | exclude names matching EXCLUDE from input paths   |
| -oOUTPUT, --output=OUTPUT  | write to OUTPUT in po, pot formats   |
| :doc:`--psyco=MODE <option_psyco>`         | use psyco to speed up the operation, modes: none, full, profile   |
| -P, --pot            | output PO Templates (.pot) rather than PO files (.po)   |
| --flavour=FLAVOUR      | The flavour of text file: plain (default), dokuwiki, mediawiki  |
| --encoding           | encoding of the input file  |

Options (po2txt):

| --version            | show program's version number and exit   |
| -h, --help           | show this help message and exit   |
| --manpage            | output a manpage based on the help   |
| :doc:`--progress=progress <option_progress>`  | show progress as: dots, none, bar, names, verbose   |
| :doc:`--errorlevel=errorlevel <option_errorlevel>`   | show errorlevel as: none, message, exception, traceback   |
| -iINPUT, --input=INPUT    | read from INPUT in po, pot formats   |
| -xEXCLUDE, --exclude=EXCLUDE   | exclude names matching EXCLUDE from input paths   |
| -oOUTPUT, --output=OUTPUT   | write to OUTPUT in txt format   |
| -tTEMPLATE, --template=TEMPLATE   | read from TEMPLATE in txt format   |
| :doc:`--psyco=MODE <option_psyco>`         | use psyco to speed up the operation, modes: none, full, profile   |
| -wWRAP, --wrap=WRAP  | set number of columns to wrap text at   |
| --fuzzy              | use translations marked fuzzy  |
| --nofuzzy            | don't use translations marked fuzzy (default)  |
| --encoding           | encoding of the template file  |

.. _pages/toolkit/txt2po#a_roundtrip_example:

A roundtrip example
===================

.. _pages/toolkit/txt2po#preparing_input_files:

Preparing input files
---------------------

With **txt2po** a text file is broken down into sections.  Each section is
separated by a line of whitespace.  Each section will appear as a msgid in the
PO file.  Because of this simple method of breaking up the input file it might
be necessary to alter the layout of your input file.  For instance you might
want to separate a heading from a paragraph by using whitespace.

For steps in a process you would want to leave a blank line between each step
so that each step can be translated independently.

For a list of items you might want to group them together so that a translator
could for example place them in alphabetic order for their translation.

Once the input file is prepared you can proceed to the next step.

.. _pages/toolkit/txt2po#creating_the_pot_files:

Creating the POT files
----------------------

This is simple::

  txt2po -P TEXT_FILE text_file.pot

A translator would copy the POT file to their own PO file and then create translations of the entries.
If you wish to create a PO file and not a POT file then leave off the *-P* option.

You might want to manually edit the POT file to remove items that should not be
translated.  For instance if part of the document is a license you might want
to remove those if you do not want the license translated for legal reasons.

.. _pages/toolkit/txt2po#translating:

Translating
-----------

Translate as normal.  However translators should be aware that writers of the
text file may have used spaces, dashes, equals, underscores and other aids to
indicate things such as::

        * Headings and sub-headings
        * Code examples, command lines examples
        * Various lists
        * etc

They will need to adapt these to work in their language being aware of how they
will appear once they are merged with the original text document.

.. _pages/toolkit/txt2po#creating_a_translated_text_file:

Creating a translated text file
-------------------------------

With the translations complete you can create a translated text file like this::

  po2txt -w 75 -t TEXT_FILE translated.po TEXT_FILE.translated

This uses the original text file as a template and creates a new translated text
file using the translations found in the PO file.

The *-w* command allows you to reflow the translated text to *N* number of
characters, otherwise the text will appear as one long line.

.. _pages/toolkit/txt2po#help_with_wiki_syntax:

Help with Wiki syntax
=====================

.. _pages/toolkit/txt2po#dokuwiki:

dokuwiki
--------

To retrieve the raw syntax for your dokuwiki page add '?do=export_raw' to you URL.  The following would retrieve this current page in raw dokuwiki format http://translate.sourceforge.net/wiki/toolkit/txt2po?do=export_raw::

  wget http://translate.sourceforge.net/wiki/toolkit/txt2po?do=export_raw -O txt2po.txt
  txt2po --flavour=dokuwiki -P txt2po.txt txt2po.pot
  # edit txt2po.pot
  po2txt -t txt2po.txt fr.po fr.txt

First we retrieve the file in raw dokuwiki format, then we create a POT file for editing.  We created a French translation and using po2txt plus the original file as a template we output fr.txt which is a French version of the original txt2po.txt.  This file can now be uploaded to the wiki server.

.. _pages/toolkit/txt2po#mediawiki:

MediaWiki
---------

To retrieve the raw media wiki syntax add '?action=raw' to you wiki URL.  The following retrieves the Translate Toolkit page from Wikipedia in raw MediaWiki format http://en.wikipedia.org/wiki/Translate_Toolkit?action=raw or http://en.wikipedia.org/w/index.php?title=Pootle&action=raw.

To process follow the instructions above but substituting the MediaWiki retrieval method.