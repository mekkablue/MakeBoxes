# MakeBoxes.glyphsFilter

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/) by Georg Seifert.

*Filter > Make Boxes* turns the glyph into a box reaching from LSB to RSB, and from descender to ascender, as set in *Font Info > Masters.* Useful as custom parameter for making a backdrop instance.

![All boxes created reach from ascender to descender.](MakeBoxes.png "Make Boxes Screenshot")

After installation, it will add the menu item *Filter > Make Boxes*.
You can set a keyboard shortcut in System Preferences.

### Installation

1. *Window > Plugin Manager.*
2. Click the *Install* button next to the Make Boxes entry.
3. Restart Glyphs.

### Usage Instructions

1. Select any number of glyphs in Font or Edit view.
2. Use *Filter > Make Boxes* to bring up the Make Boxes window.

### Custom Parameter

In *File > Font Info > Instances*, add a new Custom Parameter to an instance. You can trigger the filter with the value `MakeBoxes`:

    Property: Filter
    Value: MakeBoxes

### Requirements

The plugin needs Glyphs 2.5 or higher. It probably does not work in earlier versions.

### License

Copyright 2018 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
