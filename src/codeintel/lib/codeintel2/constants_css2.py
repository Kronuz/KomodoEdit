"""
CSS 3 definitions - requires CSS 1 module.
"""

import textwrap

from codeintel2.constants_css1 import CSS_ATTR_DICT as CSS1_ATTR_DICT
from codeintel2.constants_css1 import CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT as CSS1_PROPERTY_ATTRIBUTE_CALLTIPS_DICT

CSS_PSEUDO_CLASS_NAMES = """first-letter first-line link active visited
        first-child focus hover lang before after left right first""".split()

CSS2_SPECIFIC_ATTRS_DICT = {
    'azimuth': [
        'behind',
        'center',
        'center-left',
        'center-right',
        'far-left',
        'far-right',
        'inherit',
        'left',
        'leftwards',
        'left-side',
        'right',
        'rightwards',
        'right-side',
        '!important',
    ],
    'border-bottom-color': [
        'inherit',
        'rgb(',
        '!important',
        '#',
    ],
    'border-bottom-style': [
        'dashed',
        'dotted',
        'double',
        'groove',
        'hidden',
        'inherit',
        'inset',
        'none',
        'outset',
        'ridge',
        'solid',
        '!important',
    ],
    'border-collapse': [
        'collapse',
        'inherit',
        'separate',
        '!important',
    ],
    'border-top-color': [
        'inherit',
        'rgb(',
        '!important',
        '#',
    ],
    'border-top-style': [
        'dashed',
        'dotted',
        'double',
        'groove',
        'hidden',
        'inherit',
        'inset',
        'none',
        'outset',
        'ridge',
        'solid',
        '!important',
    ],
    'bottom': [
        'auto',
        'inherit',
        '!important',
    ],
    'caption-side': [
        'bottom',
        'inherit',
        'left',
        'right',
        'top',
        '!important',
    ],
    'clip': [
        'auto',
        'inherit',
        'rect(',
        '!important',
    ],
    'content': [
        'close-quote',
        'counter(',
        'inherit',
        'no-close-quote',
        'no-open-quote',
        'open-quote',
        'url(',
        '!important',
    ],
    'counter-increment': [
        'inherit',
        'none',
        '!important',
    ],
    'counter-reset': [
        'inherit',
        'none',
        '!important',
    ],
    'cue': [
        'inherit',
        'none',
        'url(',
        '!important',
    ],
    'cue-after': [
        'inherit',
        'none',
        'url(',
        '!important',
    ],
    'cue-before': [
        'inherit',
        'none',
        'url(',
        '!important',
    ],
    'cursor': [
        'auto',
        'crosshair',
        'default',
        'e-resize',
        'help',
        'inherit',
        'move',
        'ne-resize',
        'nw-resize',
        'n-resize',
        'pointer',
        'se-resize',
        'sw-resize',
        's-resize',
        'text',
        'url(',
        'wait',
        'w-resize',
        '!important',
    ],
    'direction': [
        'inherit',
        'ltr',
        'rtl',
        '!important',
    ],
    'elevation': [
        'above',
        'below',
        'higher',
        'inherit',
        'level',
        'lower',
        '!important',
    ],
    'empty-cells': [
        'hide',
        'inherit',
        'show',
        '!important',
    ],
    'left': [
        'auto',
        'inherit',
        '!important',
    ],
    'marker-offset': [
        'auto',
        'inherit',
        '!important',
    ],
    'marks': [
        'crop',
        'cross',
        'inherit',
        'none',
        '!important',
    ],
    'max-height': [
        'inherit',
        'none',
        '!important',
    ],
    'max-width': [
        'inherit',
        'none',
        '!important',
    ],
    'min-height': [
        'inherit',
        '!important',
    ],
    'min-width': [
        'inherit',
        '!important',
    ],
    'orphans': [
        'inherit',
        '!important',
    ],
    'outline': [
        'dashed',
        'dotted',
        'double',
        'groove',
        'hidden',
        'inherit',
        'inset',
        'invert',
        'medium',
        'none',
        'outset',
        'rgb(',
        'ridge',
        'solid',
        'thick',
        'thin',
        '!important',
        '#',
    ],
    'outline-color': [
        'inherit',
        'invert',
        'rgb(',
        '!important',
        '#',
    ],
    'outline-style': [
        'dashed',
        'dotted',
        'double',
        'groove',
        'hidden',
        'inherit',
        'inset',
        'none',
        'outset',
        'ridge',
        'solid',
        '!important',
    ],
    'outline-width': [
        'inherit',
        'medium',
        'thick',
        'thin',
        '!important',
    ],
    'overflow': [
        'auto',
        'hidden',
        'inherit',
        'scroll',
        'visible',
        '!important',
    ],
    'page': [
        'auto',
    ],
    'page-break-after': [
        'always',
        'auto',
        'avoid',
        'inherit',
        'left',
        'right',
        '!important',
    ],
    'page-break-before': [
        'always',
        'auto',
        'avoid',
        'inherit',
        'left',
        'right',
        '!important',
    ],
    'page-break-inside': [
        'auto',
        'avoid',
        'inherit',
        '!important',
    ],
    'pause': [
        'inherit',
        'ms',
        's',
        '!important',
    ],
    'pause-after': [
        'inherit',
        'ms',
        's',
        '!important',
    ],
    'pause-before': [
        'inherit',
        'ms',
        's',
        '!important',
    ],
    'pitch': [
        'high',
        'Hz',
        'inherit',
        'kHz',
        'low',
        'medium',
        'x-high',
        'x-low',
        '!important',
    ],
    'pitch-range': [
        'inherit',
        '!important',
    ],
    'play-during': [
        'auto',
        'inherit',
        'none',
        'url(',
        '!important',
    ],
    'position': [
        'absolute',
        'fixed',
        'inherit',
        'relative',
        'static',
        '!important',
    ],
    'quotes': [
        'inherit',
        'none',
        '!important',
    ],
    'richness': [
        'inherit',
        '!important',
    ],
    'right': [
        'auto',
        'inherit',
        '!important',
    ],
    'size': [
        'auto',
        'inherit',
        'landscape',
        'portrait',
        '!important',
    ],
    'speak': [
        'inherit',
        'none',
        'normal',
        'spell-out',
        '!important',
    ],
    'speak-header': [
        'always',
        'inherit',
        'once',
        '!important',
    ],
    'speak-numeral': [
        'continuous',
        'digits',
        'inherit',
        '!important',
    ],
    'speak-punctuation': [
        'code',
        'inherit',
        'none',
        '!important',
    ],
    'speech-rate': [
        'fast',
        'faster',
        'inherit',
        'medium',
        'slow',
        'slower',
        'x-fast',
        'x-slow',
        '!important',
    ],
    'stress': [
        'inherit',
        '!important',
    ],
    'table-layout': [
        'auto',
        'fixed',
        'inherit',
        '!important',
    ],
    'text-shadow': [
        'inherit',
        'none',
        'rgb(',
        '!important',
        '#',
    ],
    'top': [
        'auto',
        'inherit',
        '!important',
    ],
    'unicode-bidi': [
        'bidi-override',
        'embed',
        'inherit',
        'normal',
        '!important',
    ],
    'visibility': [
        'collapse',
        'hidden',
        'inherit',
        'visible',
        '!important',
    ],
    'voice-family': [
        'child',
        'female',
        'inherit',
        'male',
        '!important',
    ],
    'volume': [
        'inherit',
        'loud',
        'medium',
        'silent',
        'soft',
        'x-loud',
        'x-soft',
        '!important',
    ],
    'widows': [
        'inherit',
        '!important',
    ],
    'z-index': [
        'auto',
        'inherit',
        '!important',
    ],
}

CSS2_SPECIFIC_CALLTIP_DICT = {
    'azimuth'               : """Audio: Spatial audio property for aural presentation""",
    'border-bottom-color'   : """Sets the color of the bottom border""",
    'border-bottom-style'   : """Specifies the line style of a box's bottom border (solid, double, dashed, hidden, etc.)""",
    'border-collapse'       : """This property selects a table's border model.""",
    'border-left-color'     : """Sets the color of the left border""",
    'border-left-style'     : """Specifies the line style of a box's left border (solid, double, dashed, hidden, etc.)""",
    'border-right-color'    : """Sets the color of the right border""",
    'border-right-style'    : """Specifies the line style of a box's right border (solid, double, dashed, hidden, etc.)""",
    'border-spacing'        : """The lengths specify the distance that separates adjacent cell borders. If one length is specified, it gives both the horizontal and vertical spacing. If two are specified, the first gives the horizontal spacing and the second the vertical spacing. Lengths may not be negative.""",
    'border-top-color'      : """Sets the color of the top border""",
    'border-top-style'      : """Specifies the line style of a box's top border (solid, double, dashed, hidden, etc.)""",
    'bottom'                : """Specifies how far a box's bottom content edge is offset above the bottom of the box's containing block""",
    'caption-side'          : """Specifies the position of the caption box with respect to the table box""",
    'clip'                  : """A clipping region defines what portion of an element's rendered content is visible""",
    'content'               : """This property is used with the :before and :after pseudo-elements to generate content in a document""",
    'counter-increment'     : """Indicates by how much the counter is incremented for every occurrence of the element. The default increment is 1. Zero and negative integers are allowed.""",
    'counter-reset'         : """Specifies the value that the counter is set to on each occurrence of the element""",
    'cue'                   : """Audio: Shorthand for setting 'cue-before' and 'cue-after'. If two values are given, the first value is 'cue-before' and the second is 'cue-after'. If only one value is given, it applies to both properties.""",
    'cue-after'             : """Audio: Sound to be played after the element to delimit it""",
    'cue-before'            : """Audio: Sound to be played before the element to delimit it""",
    'cursor'                : """Specifies the type of cursor to be displayed for the pointing device""",
    'direction'             : """Specifies the base writing direction of blocks and the direction of embeddings and overrides (see 'unicode-bidi') for the Unicode bidirectional algorithm.""",
    'elevation'             : """Audio: Spatial elevation direction for aural presentation.""",
    'empty-cells'           : """Controls the rendering of borders around cells that have no visible content""",
    'left'                  : """This property specifies how far a box's left content edge is offset to the right of the left edge of the box's containing block""",
    'marker-offset'         : """Specifies the distance between the nearest border edges of a marker box and its associated principal box""",
    'marks'                 : """Specifies whether cross marks or crop marks or both should be rendered just outside the page box edge. Crop marks indicate where the page should be cut. Cross marks (also known as register marks or registration marks) are used to align sheets""",
    'max-height'            : """Maximum height of the containing box""",
    'max-width'             : """Maximum width of the containing box""",
    'min-height'            : """Minimum height of the containing box""",
    'min-width'             : """Minimum width of the containing box""",
    'orphans'               : """Specifies the minimum number of lines of a paragraph that must be left at the bottom of a page""",
    'outline'               : """Shorthand for setting 'outline-style', 'outline-width', and 'outline-color' at the same place in the style sheet""",
    'outline-color'         : """Outline color around visual object""",
    'outline-style'         : """Specifies the line style of the outline (solid, double, dashed, etc.)""",
    'outline-width'         : """Specifies the width of the outline around the element""",
    'overflow'              : """Specifies whether the content of a block-level element is clipped when it overflows the element's box (which is acting as a containing block for the content)""",
    'page'                  : """Specifies a particular type of page where an element should be displayed""",
    'page-break-after'      : """Indicate the user agent should break the page after here""",
    'page-break-before'     : """Indicate the user agent should break the page before here""",
    'page-break-inside'     : """Indicate the user agent should break the page within here""",
    'pause'                 : """Audio: Shorthand for setting 'pause-before' and 'pause-after'. If two values are given, the first value is 'pause-before' and the second is 'pause-after'. If only one value is given, it applies to both properties""",
    'pause-after'           : """Audio: Specifies a pause to be observed after speaking an element's content""",
    'pause-before'          : """Audio: Specifies a pause to be observed before speaking an element's content""",
    'pitch'                 : """Audio: Specifies the average pitch (a frequency) of the speaking voice""",
    'pitch-range'           : """Audio: Specifies variation in average pitch""",
    'play-during'           : """Audio: Similar to the 'cue-before' and 'cue-after' properties, this property specifies a sound to be played as a background while an element's content is spoken""",
    'position'              : """Specifies which of the CSS2 positioning algorithms is used to calculate the position of a box""",
    'quotes'                : """Specifies quotation marks for any number of embedded quotations""",
    'richness'              : """Audio: Specifies the richness, or brightness, of the speaking voice. A rich voice will "carry" in a large room, a smooth voice will not""",
    'right'                 : """This property specifies how far a box's right content edge is offset to the left of the right edge of the box's containing block""",
    'size'                  : """Specifies the size and orientation of a page box""",
    'speak'                 : """Audio: Specifies whether text will be rendered aurally and if so, in what manner""",
    'speak-header'          : """Audio: Specifies whether table headers are spoken before every cell, or only before a cell when that cell is associated with a different header than the previous cell""",
    'speak-numeral'         : """Audio: Controls how numerals are spoken""",
    'speak-punctuation'     : """Audio: Specifies how punctuation is spoken""",
    'speech-rate'           : """Audio: Specifies the speaking rate. Note that both absolute and relative keyword values are allowed""",
    'stress'                : """Audio: Specifies the height of "local peaks" in the intonation contour of a voice""",
    'text-shadow'           : """A comma-separated list of shadow effects to be applied to the text of the element""",
    'top'                   : """This property specifies how far a box's top content edge is offset below the top edge of the box's containing block""",
    'unicode-bidi'          : """Specifies the level of embedding with respect to the bidirectional algorithm""",
    'visibility'            : """Specifies whether the boxes generated by an element are rendered. Invisible boxes still affect layout (set the 'display' property to 'none' to suppress box generation altogether)""",
    'voice-family'          : """Audio: Value is a comma-separated, prioritized list of voice family names""",
    'volume'                : """Audio: Refers to the median volume of the audio""",
    'widows'                : """Specifies the minimum number of lines of a paragraph that must be left at the top of a page""",
    'z-index'               : """For a positioned box, specifies the stack level of the box in the current stacking context and also whether the box establishes a local stacking context.""",
}


# Everything that was in CSS1 is also in CSS2.
CSS_ATTR_DICT = CSS1_ATTR_DICT.copy()
CSS_ATTR_DICT.update(CSS2_SPECIFIC_ATTRS_DICT)
CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT = CSS1_PROPERTY_ATTRIBUTE_CALLTIPS_DICT.copy()
CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT.update(CSS2_SPECIFIC_CALLTIP_DICT)

for property, calltip in CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT.items():
    if property not in CSS2_SPECIFIC_CALLTIP_DICT:
        calltip += " (CSS1, CSS2)"
    else:
        calltip += " (CSS2)"
    CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT[
        property] = "\n".join(textwrap.wrap(calltip, 40))


# Note: The System Colors below are not used yet.
css2_system_colors = {
    'ActiveBorder'           : """Active window border""",
    'ActiveCaption'          : """Active window caption""",
    'AppWorkspace'           : """Background color of multiple document interface""",
    'Background'             : """Desktop background""",
    'ButtonFace'             : """Face color for three-dimensional display elements""",
    'ButtonHighlight'        : """Dark shadow for three-dimensional display elements (for edges facing away from the light source)""",
    'ButtonShadow'           : """Shadow color for three-dimensional display elements""",
    'ButtonText'             : """Text on push buttons""",
    'CaptionText'            : """Text in caption, size box, and scrollbar arrow box""",
    'GrayText'               : """Grayed (disabled) text. This color is set to #000 if the current display driver does not support a solid gray color""",
    'Highlight'              : """Item(s) selected in a control""",
    'HighlightText'          : """Text of item(s) selected in a control""",
    'InactiveBorder'         : """Inactive window border""",
    'InactiveCaption'        : """Inactive window caption""",
    'InactiveCaptionText'    : """Color of text in an inactive caption""",
    'InfoBackground'         : """Background color for tooltip controls""",
    'InfoText'               : """Text color for tooltip controls""",
    'Menu'                   : """Menu background""",
    'MenuText'               : """Text in menus""",
    'Scrollbar'              : """Scroll bar gray area""",
    'ThreeDDarkShadow'       : """Dark shadow for three-dimensional display elements""",
    'ThreeDFace'             : """Face color for three-dimensional display elements""",
    'ThreeDHighlight'        : """Highlight color for three-dimensional display elements""",
    'ThreeDLightShadow'      : """Light color for three-dimensional display elements (for edges facing the light source)""",
    'ThreeDShadow'           : """Dark shadow for three-dimensional display elements""",
    'Window'                 : """Window background""",
    'WindowFrame'            : """Window frame""",
    'WindowText'             : """Text in windows""",
}

# Add the css2 system colors.
#from codeintel2.util import CompareNPunctLast
# for attr, values in CSS_ATTR_DICT.items():
#    if '#' in values or 'rbg(' in values:
#        CSS_ATTR_DICT[attr] = sorted(values + css2_system_colors.keys(),
#                                     cmp=CompareNPunctLast)
